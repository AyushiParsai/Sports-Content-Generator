
from google import genai
import os
api_key = '+'
client = genai.Client(api_key=api_key)
print("--genAI tester-- type exit to quit")
while True:
   user_prompt = input("\nUser:")
   if user_prompt.lower() in ['exit','quit']:
      break
   try:
      response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = user_prompt
      )
      print(f"Ai:{response.text}" )
   except Exception as e:
      print(f"Error:{e}")