import chainlit as cl
from src.llm import ask_order
from src.prompt import system_instruction

# Initialize messages list here
messages = [("system", system_instruction)]

@cl.on_message
async def main(message: cl.Message):
    global messages
    # Append the user's message to the list of messages
    messages.append(("human", message.content))
    
    # Call ask_order with the updated messages (including user input)
    response = ask_order(messages)
    
    # Append the assistant's response to the list of messages
    messages.append(("assistant", response))

    # Send the response back to the Chainlit frontend
    await cl.Message(
        content=response
    ).send()

