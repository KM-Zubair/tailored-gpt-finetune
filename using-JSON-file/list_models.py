# list_models.py
import os

def list_fine_tuned_models():
    os.system("openai api fine_tunes.list")

if __name__ == "__main__":
    list_fine_tuned_models()
