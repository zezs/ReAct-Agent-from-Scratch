import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-70b-8192", # 70b is better for agentic behaviour
)

print(chat_completion.choices[0].message.content)


# if __name__ == "__main__":
#     print("ReAct!")