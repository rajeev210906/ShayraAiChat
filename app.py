from flask import Flask, request, jsonify, render_template
import os
import sys
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__)

# Set the environment variable for the API key
os.environ['GOOGLE_API_KEY'] = "YOUR_API_KEY"

# Initialize the ChatGoogleGenerativeAI class
llm = ChatGoogleGenerativeAI(model="gemini-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.form['message']
    response = llm.invoke(msg)
    return jsonify({'response': response.content})

if __name__ == "__main__":
    app.run(debug=True)
