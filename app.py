from flask import Flask, request, jsonify
from system_prompts.system_base_prompt import prompt
from utils.ChatGPTResponseHandler import ChatGPTResponseHandler, Model
from utils.split_response_by_delimiters import split_response_by_delimiters
import json

handler = ChatGPTResponseHandler(model=Model.gpt4preview, prompt=prompt, prompt_id=1)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


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
