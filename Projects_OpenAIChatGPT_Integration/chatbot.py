#Import openai, os, spacy and dotenv libraries

import openai
import os
import spacy
from dotenv import load_dotenv

# Instantiate load_dotenv() function
load_dotenv()

'''Use os.getenv is a method to return value of environment variable. Environment variable value is "OPEN_API_KEY"
and variable name is "api_key"'''

api_key = os.getenv("OPENAI_API_KEY")

# Openai.api_key is used to authenticate request to the openAI api
openai.api_key = api_key

'''Create empty variables previous questions and previous answers for chatbot to 
keep track of all the questions and answers to keep track of context'''

prev_questions = []
prev_answers = []

'''Define a function that takes a prompt as an input and returns response 
from openai Completion API from a specified model'''

def ask_chat_gpt(prompt, model = "text_davinci_002"):
    response = openai.Completion.create(
        engine = model,
        prompt = prompt,
        temperature = 1,
        max_tokens = 500,
        n=1
    )

    return response.choices[0].text.strip()


# Define a welcome message for the contextual chatbot

print("Welcome to Asif Virani's Chatbot. Please type exit to end the chat")

# Define dynamic user input and chatgpt answer

while True:
#Create an empty history variable to put inside all the previous questions and answers
    history = ""
    user_input = input("\nuser:")
    if user_input == "exit":
        break


'''# We store all prev questions and answers under history variable and 
# We use zip method that takes two parameters prev_questions and Prev_answers and 
we iterate in the loop to keep track of all questions and answers'''

for questions, answers in zip(prev_questions, prev_answers):
    history += f"The user asks : {questions}"
    history += f"The chat_gpt_answers : {answers}"

prompt = f"The user asks : {user_input}\n"
history += prompt
chat_gpt_answers = ask_chat_gpt(history)
print(f"{chat_gpt_answers}")

prev_questions.append(user_input)
prev_answers.append(chat_gpt_answers)


