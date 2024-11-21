# analyze_model.py
import os

def analyze_model(job_id):
    os.system(f"openai api fine_tunes.results -i {job_id}")

if __name__ == "__main__":
    job_id = input("Enter your fine-tune job ID: ")
    analyze_model(job_id)
