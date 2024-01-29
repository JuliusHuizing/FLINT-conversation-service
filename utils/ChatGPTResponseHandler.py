import openai
from openai import OpenAI
from enum import Enum
from dotenv import load_dotenv, find_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# The OPENAI_SECRET key env var needs to be set for the OpenAI API to work.
load_dotenv(find_dotenv())
OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

class Model(Enum):
    gpt35turbo = "gpt-3.5-turbo-1106" 
    gpt4preview = "gpt-4-1106-preview"  # this is expensive

class ChatGPTResponseHandler:
    def __init__(self, model: Model, prompt: str, prompt_id: str):
        logger.info("Initializing ChatGPTResponseHandler")
        self._seed = 42  # ensure reproducible results
        self._temperature = 0.0  # ensure deterministic results
        self._client = OpenAI()
        self._model = model.value
        self._prompt_id = prompt_id
        self.system_prompt = prompt

    def id(self):
        logger.info("Generating id")
        return f"model:{self._model}:seed:{self._seed}:temperature:{self._temperature}:prompt:{self._prompt_id}"

    def request_full_response(self, input: str) -> str:
        logger.info(f"Requesting full response for input: {input}")
        response = self._computeReponse(input)
        message = self._extract_message_from_response(response)
        return message

    def request_chat_response(self, messages: list) -> str:
        logger.info(f"Requesting chat response for messages: {messages}")
        response = self._chat(messages)
        message = self._extract_message_from_response(response)
        logger.info(f"Chat response unpacked: {message}")
        return message

    def _computeReponse(self, sentence):
        logger.info(f"Computing response for sentence: {sentence}")
        response = self._client.chat.completions.create(
            seed=self._seed,
            temperature=self._temperature,
            model=self._model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": sentence},
            ],
        )
        return response

    def _chat(self, messages: list):
        logger.info("Creating chat completion")
        chat_history = [{"role": "system", "content": "You are a friendly chatbot."}]
        chat_history = chat_history + messages
        logger.info(f"Chat history: {chat_history}")
        response = self._client.chat.completions.create(
            seed=self._seed,
            temperature=self._temperature,
            model=self._model,
            messages=chat_history)
        logger.info(f"Chat response: {response}")
        return response

    def _extract_message_from_response(self, response) -> str:
        logger.info("Extracting message from response")
        return response.choices[0].message.content

    def _extract_final_line(self, message: str) -> str:
        logger.info("Extracting final line from message")
        message.split("```\n")[-1]
        message = message.split("```\n")[-1].replace("\n```", "")
        return message
