import pyautogui
import time
import pyperclip
from groq import Groq
from dotenv import load_dotenv
import os

pyautogui.FAILSAFE = True

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
whatsapp_icon = (1330,1050)
pyautogui.click(*whatsapp_icon)           #click to open whatsapp
time.sleep(1)

pyautogui.moveTo(670,222)                                   #select chat
pyautogui.dragTo(1680,918, duration=1.2, button="left")

pyautogui.hotkey('ctrl','c')            #copy chat

pyautogui.click(1280,540)
time.sleep(1)

text = pyperclip.paste()                

print(text)             #paste the copied chat

completion = client.chat.completions.create(                #response from ai
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Yash who speaks hindi as well as english. He is from India and is a 19yr old student. you analyse the chat history and respond like Yash with mix hindi and english, just like used by this generation, hinglish language.Don't respond too long, just reply to what is asked"   
        },
        
        {
            "role": "user",
            "content": text
        }
    ]
)
response = (completion.choices[0].message.content) #response generayed by ai

print(response)           #checking ai response


pyperclip.copy(response)                #create a copy of ai response to paste in whatsapp
time.sleep(0.5)                                

pyautogui.click(1365,970)                   #pasting the copy of ai response and sending it.
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
