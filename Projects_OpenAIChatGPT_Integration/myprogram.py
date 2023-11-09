import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

'''models = openai.Model.list()
print(models)'''

model = "text-davinci-002"
prompt = "write a short story regarding the trip to european country"

response = openai.Completion.create(
    prompt=prompt,
    engine=model,
    temperature=1,
    n=1
)

# Define a welcome message for the contextual chatbot

print("Welcome to Asif Virani's Chatbot. Please type exit to end the chat")

# Define dyanamic user input and chatgpt answer

while True:
    user_input = input("\nuser:")
    if user_input == "exit":
        break

    prompt = f"The user asks : {user_input}\n chatgpt answers:"
    ChatGPT_Answers = f"Chatbot Answers : {prompt}"




# If we provide parameter "n=1", then we need to write the code as shown below

generated_text = response.choices[0].text.strip()
print(generated_text)
print("***")

spacy_model = spacy.load("en_core_web_md")
analysis = spacy_model(generated_text)

# To derive text tokens (words) and Pos tags etc from the chatgpt response. Use the below codes for text and Pos tags
'''for token in analysis:
    print(token.text, token.pos_)'''

# To Derive entity text and its entities from the chatGPT response. Use the below codes for
for ent in analysis.ents:
    print(ent.text, ent.label_)

# If we provide the parameter "n=5", we need loop over all the response choices and get the answers. Below code will loop over the responses and provide accurate answers.
'''for idx, option in enumerate(response.choices):
    generated_text = option.text.strip()
    print(f"Answer {idx+1} : {generated_text}\n")
'''


