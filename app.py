from flask import Flask, render_template, request, jsonify
import os
from google import genai
from google.genai import types

app = Flask(__name__)

def serialize_content(content):
    return {
        'role': content.role,
        'parts': [{'text': part.text} for part in content.parts]
    }

def deserialize_content(content_dict):
    return types.Content(
        role=content_dict['role'],
        parts=[types.Part(text=part['text']) for part in content_dict['parts']]
    )

def get_gemini_response(conversation_history, user_input):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    model = "gemini-2.5-pro-exp-03-25"

    # Add user's message to conversation history
    conversation_history.append(
        types.Content(
            role="user",
            parts=[types.Part(text=user_input)],
        )
    )

    contents = conversation_history

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part(text="""You are a highly knowledgeable and professional Finance Assistant.
Your role is to help users manage their personal finances, provide investment education, explain financial concepts clearly, and answer questions about budgeting, saving, credit, insurance, taxation, and financial planning.
Use clear, concise, and jargon-free language, but also explain terms when necessary.
You should never provide personalized investment advice, tax filing decisions, or legal recommendations.
If a user asks a question requiring licensed financial or legal expertise, respond with a disclaimer and suggest consulting a certified professional.
Always prioritize financial literacy, risk awareness, and responsible decision-making.
When relevant, provide examples, comparisons (e.g., ETFs vs. mutual funds), or suggest useful budgeting methods (e.g., 50/30/20 rule).
Maintain a friendly, professional, and informative tone at all times."""),
        ],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    # Add assistant's response to conversation history
    conversation_history.append(
        types.Content(
            role="model",
            parts=[types.Part(text=response_text)],
        )
    )

    return response_text, conversation_history

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    
    # Convert the received history back to Content objects
    conversation_history = [deserialize_content(item) for item in data.get('history', [])]
    
    response, updated_history = get_gemini_response(conversation_history, user_input)
    
    # Convert the updated history to a serializable format
    serialized_history = [serialize_content(item) for item in updated_history]
    
    return jsonify({
        'response': response,
        'history': serialized_history
    })

if __name__ == '__main__':
    app.run(debug=True) 