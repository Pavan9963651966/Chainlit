from langchain_groq import ChatGroq
from src.prompt import system_instruction
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Initialize ChatGroq client with your API key
client = ChatGroq(api_key=api_key,
                  model="llama-3.1-70b-Versatile",
                  temperature=0.7)

def ask_order(messages):
    # Convert messages to the expected input format
    input_text = messages

    # Call the invoke method with correctly formatted input
    response = client.invoke(
        messages=input_text
    )
    
    # Extract and return the content of the response
    return response["choices"][0]["message"]["content"]
