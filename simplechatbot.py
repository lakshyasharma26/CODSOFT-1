# Importing the necessary libraries
import random

# Predefined rules for user queries and responses
rules = {
    "What is your name?": "My name is Chatbot.",
    "How are you?": "I'm doing well, thank you!",
    "What is the weather today?": "I'm sorry, I don't have access to weather information.",
    "Tell me a joke.": "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!",
    "Goodbye": "Goodbye! Have a great day!"
}

# Function to generate responses based on user inputs
def generate_response(user_input):
    for pattern, response in rules.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't understand that."

# Main function to run the chatbot
def main():
    print("Welcome to Chatbot!")
    print("You can start chatting with me. Type 'Goodbye' to exit.")

    while True:
        user_input = input("User: ")
        response = generate_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() == "goodbye":
            break

if __name__ == "__main__":
    main()
