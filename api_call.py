from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

command = "how r u"
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Yash who speaks hindi as well as english. He is from India and is a 19yr old student. you analyse the chat history and respond like Yash with mix hindi and english, just like used by this generation, hinglish language.Don't respond too long, just reply to what is asked"   
        },

        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)