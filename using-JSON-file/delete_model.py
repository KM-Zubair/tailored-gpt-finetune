# delete_model.py
import os

def delete_model(model_id):
    os.system(f"openai api models.delete -i {model_id}")

if __name__ == "__main__":
    model_id = input("Enter the fine-tuned model ID to delete: ")
    delete_model(model_id)
