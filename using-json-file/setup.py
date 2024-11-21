# setup.py
import os

def setup_environment():
    openai_key = input("Enter your OpenAI API key: ")
    os.environ['OPENAI_API_KEY'] = openai_key
    print("Environment setup complete. API key configured.")

if __name__ == "__main__":
    setup_environment()
