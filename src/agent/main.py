import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Configure the API key
# Make sure to set the GOOGLE_API_KEY environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

genai.configure(api_key=api_key)

from src.agent.tools import execute_graphql_query

# Define the tools that the agent can use.
# We provide the function directly to the model.
tools = [execute_graphql_query]

# Create the generative model with the defined tools
model = genai.GenerativeModel(model_name="gemini-2.5-flash", tools=tools)


def run_agent(prompt: str):
    """
    Runs the agent with a given prompt.

    Args:
        prompt (str): The user's request in natural language.

    Returns:
        str: The agent's response.
    """
    print(f"User prompt: {prompt}")

    # Start a chat session
    chat = model.start_chat(enable_automatic_function_calling=True)

    # Send the prompt to the model
    response = chat.send_message(prompt)

    # The model will automatically call the necessary functions.
    # The response will contain the final result after the function calls.

    # We just need to get the text part of the final response.
    final_response = ""
    for chunk in response:
        if chunk.text:
            final_response += chunk.text

    print(f"Agent response: {final_response}")
    return final_response


if __name__ == "__main__":
    # Example of how to run the agent
    # This prompt should trigger the agent to use the GraphQL tool
    user_request = "Quiero un listado de todas las especialidades médicas disponibles."
    run_agent(user_request)
