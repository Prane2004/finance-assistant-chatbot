# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro-exp-03-25"
    conversation_history = []  # To store the conversation history

    while True:
        user_input = input("Enter your question (type 'end' to exit): ")
        if user_input.lower() == 'end':
            print("Goodbye! Have a great day!")
            break

        # Add user's message to conversation history
        conversation_history.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_input)],
            )
        )

        # Create the contents list with conversation history
        contents = conversation_history

        generate_content_config = types.GenerateContentConfig(
            response_mime_type="text/plain",
            system_instruction=[
                types.Part.from_text(text="""You are a highly knowledgeable and professional Finance Assistant.
Your role is to help users manage their personal finances, provide investment education, explain financial concepts clearly, and answer questions about budgeting, saving, credit, insurance, taxation, and financial planning.
Use clear, concise, and jargon-free language, but also explain terms when necessary.
You should never provide personalized investment advice, tax filing decisions, or legal recommendations.
If a user asks a question requiring licensed financial or legal expertise, respond with a disclaimer and suggest consulting a certified professional.
Always prioritize financial literacy, risk awareness, and responsible decision-making.
When relevant, provide examples, comparisons (e.g., ETFs vs. mutual funds), or suggest useful budgeting methods (e.g., 50/30/20 rule).
Maintain a friendly, professional, and informative tone at all times."""),
            ],
        )

        print("\nAssistant: ", end="")
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            print(chunk.text, end="")
        
        print("\n")  # Add a newline for better readability

if __name__ == "__main__":
    generate()
