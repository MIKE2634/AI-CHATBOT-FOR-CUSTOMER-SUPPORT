import json
import random
import re

# Define the correct file path
file_path = 'C:/Users/Admin/Desktop/chatbot/intents.json'

# Load the JSON data
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(f"Successfully loaded {len(data['intents'])} intents.")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please check the file path.")
    exit()
except json.JSONDecodeError:
    print(f"Error decoding JSON. Please check the format of the file.")
    exit()

# Extract intents
intents = data['intents']

# Create a dictionary to store patterns and responses
patterns_responses = {}

# Populate patterns and responses from the intents
for intent in intents:
    tag = intent['tag']
    patterns = intent['patterns']
    responses = intent['responses']
    
    # Add patterns and responses to the dictionary
    for pattern in patterns:
        patterns_responses[pattern.lower()] = responses

# Function to get a response based on user input
def get_response(user_input):
    # Normalize user input
    user_input = user_input.lower()
    
    # Check if user input matches any pattern
    for pattern, responses in patterns_responses.items():
        if re.search(re.escape(pattern), user_input):  # Simple match without regex
            return random.choice(responses)  # Return a random response from the matching patterns

    # Default response if no pattern matches
    return "I'm sorry, I don't understand that."

# Main chatbot loop
print("Chatbot: Hi! How can I help you?")
while True:
    user_input = input("You: ")
    
    if 'bye' in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    response = get_response(user_input)
    print(f"Chatbot: {response}")
