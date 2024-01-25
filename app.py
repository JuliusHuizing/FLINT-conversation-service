from flask import Flask, request, Response, stream_with_context, json, jsonify
import requests
import sseclient
from system_prompts.system_base_prompt import prompt
import openai
from utils.ChatGPTResponseHandler import ChatGPTResponseHandler, Model
from utils.split_response_by_delimiters import split_response_by_delimiters
import json
from dotenv import load_dotenv, find_dotenv
import os

# The OPENAI_SECRET key env var needs to be set for the OpenAI API to work.
load_dotenv(find_dotenv())
OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY


handler = ChatGPTResponseHandler(model=Model.gpt4preview, prompt=prompt, prompt_id=1)

app = Flask(__name__)



@app.route('/computeActFrame', methods=['POST'])
def compute_act_frame():
    
    # Extract the message from the request (not used in this hardcoded example)
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({"error": "Message is required"}), 400


    output = handler.request_full_response(input=message)
    sub_responses = split_response_by_delimiters(output, delimiters=[("$$$", "$$$"), ("```", "```")])
    json_string = sub_responses[1]
    act_frame_response = json.loads(json_string)

    return jsonify(act_frame_response)

@app.route('/stream_reasoning', methods=['POST'])
def stream_reasoning():
    def generate():
        # Capture the data outside of the generator
        input_string = request.data.decode('utf-8')
        response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",  # adjust the model as needed
                    messages=[{"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": input_string}],
                    stream=True
                )
        client = sseclient.SSEClient(response)
        for event in client.events():
            if event.data != '[DONE]':
                try:
                    text = json.loads(event.data)['choices'][0]['delta']['content']
                    yield(text)
                except:
                    yield('')

    return Response(stream_with_context(generate()))

    def generate(input_str):
        try:
            # Use the captured data in the streaming logic
            # Streaming call to OpenAI API, etc.
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # adjust the model as needed
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": input_str}],
                stream=True
            )

            for message in response:
                yield message['choices'][0]['message']['content']

        except Exception as e:
            yield f"Error occurred: {str(e)}"

    return Response(generate(input_string), mimetype='text/plain')

if __name__ == "__main__":
    app.run(port=8000, debug=True)