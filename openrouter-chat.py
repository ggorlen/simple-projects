# To run this, get a key from https://openrouter.ai, then run:
# OPENROUTER_API_KEY=sk-or-v1-4f...f8 python3 openrouter-test.py
#
# TODO: stream responses
# TODO: have it write code to draw on canvas given english instructions

from openrouter import OpenRouter
import os

api_key = os.getenv("OPENROUTER_API_KEY")
messages = []

with OpenRouter(api_key) as client:
    while True:
        try:
            message = input("> ")
        except:
            break

        messages.append({"role": "user", "content": message})
        response = client.chat.send(
            model="nvidia/nemotron-3.5-lightning:free",
            messages=messages,
        )
        ai_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": ai_message})
        print(ai_message)
