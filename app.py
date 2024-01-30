from flask import Flask, request, Response, stream_template, json, jsonify
import requests
import sseclient
from system_prompts.base_prompt import prompt
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

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages')
    if not messages:
        return jsonify({"error": "Message is required"}), 400
    
    
    output = handler.request_chat_response(messages=messages)
    sub_responses = split_response_by_delimiters(output, delimiters=[("$$$", "$$$"), ("```", "```")])
    print("sub1:", sub_responses[0])
    print("sub2:", sub_responses[1])
    # make json out of sub_response 1
    message_response = sub_responses[0]
    latent_response = sub_responses[1]
    latent_response = json.loads(latent_response)
    # print("json:", json_response)
    

    # sub_responses = split_response_by_delimiters(output, delimiters=[("$$$", "$$$"), ("```", "```")])
    # json_string = sub_responses[1]
    # act_frame_response = json.loads(json_string)

    return jsonify({"message": {"role": "system", "content": message_response},
        "latentResponse": latent_response,
                   "actFrames": []})

@app.route('/computeActFrame', methods=['POST'])
def compute_act_frame():
    
    # Extract the message from the request (not used in this hardcoded example)
    data = request.json
    message = data.get('messages')

    if not message:
        return jsonify({"error": "Message is required"}), 400


    output = handler.request_full_response(input=message)
    sub_responses = split_response_by_delimiters(output, delimiters=[("$$$", "$$$"), ("```", "```")])
    json_string = sub_responses[1]
    act_frame_response = json.loads(json_string)

    return jsonify(act_frame_response)

@app.route('/stream_reasoning', methods=['POST'])
def stream_reasoning():
    def send_message(message):
        return openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are an unhelpful assistant that speaks in half baked sentences."},
                          {"role": "user", "content": message}],            stream=True
        )
    if request.method == 'POST':
        message = request.json['message']
        def event_stream():
            for line in send_message(message=message):
                print(line)
                text = line.choices[0].delta.content
                if len(text): 
                    yield text

        return Response(event_stream(), mimetype='text/event-stream')
    else:
        return stream_template('./chat.html')

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