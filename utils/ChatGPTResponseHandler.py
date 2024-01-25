
import openai
from openai import OpenAI
from enum import Enum
from dotenv import load_dotenv, find_dotenv
import os

# The OPENAI_SECRET key env var needs to be set for the OpenAI API to work.
load_dotenv(find_dotenv())
OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

class Model(Enum):
    gpt35turbo = "gpt-3.5-turbo-1106" 
    gpt4preview = "gpt-4-1106-preview" # this is expensive

class ChatGPTResponseHandler:
  def __init__(self, model: Model, prompt: str, prompt_id: str):
    self._seed = 42 # ensure reproducable results
    self._temperature = 0.0 # ensure deterministic results
    self._client = OpenAI() 
    self._model = model.value
    self._prompt_id = prompt_id
    # self._model="gpt-4-1106-preview", # this is expensive
    self.system_prompt = prompt   

    
  def id(self):
    return f"model:{self._model}:seed:{self._seed}:temperature:{self._temperature}:prompt:{self._prompt_id}"
    
  def request_full_response(self, input: str) -> str:
    response = self._computeReponse(input)
    message = self._extract_message_from_response(response)
    return message
        
        
  # MARK: - Private Methods
  def _computeReponse(self, sentence):
     response = self._client.chat.completions.create(
      seed=self._seed, 
      temperature=self._temperature, 
      model=self._model,
      # response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": self.system_prompt},
        {"role": "user", "content": sentence},
      ],
      # stream=True,
    )
     return response
  
     
  def _extract_message_from_response(self, response) -> str:
    return response.choices[0].message.content
  
  def _extract_final_line(self, message: str) -> str:
    message.split("```\n")[-1]
    # remove trailing \n```
    message = message.split("```\n")[-1].replace("\n```", "")
    return message
    
    

