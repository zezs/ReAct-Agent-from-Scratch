import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


class Agent:
    def __init__(self, client, system):
        self.client = client
        self.system = system
        self.messages = []

        if self.system is not None:
            self.messages.append({"role": "system", "content": self.system})