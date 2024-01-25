from flask import Flask
from dotenv import load_dotenv, find_dotenv
import os

# The OPENAI_SECRET key env var needs to be set for the OpenAI API to work.
load_dotenv(find_dotenv())
OPENAI_SECRET_KEY = os.getenv('OPENAI_SECRET_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_SECRET_KEY

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"