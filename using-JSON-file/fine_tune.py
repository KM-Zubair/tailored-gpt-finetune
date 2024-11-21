# fine_tune.py
import os

def fine_tune_model():
    data_file = "data_prepared.jsonl"
    model = "curie"
    os.system(f"openai api fine_tunes.create -t {data_file} -m {model}")

if __name__ == "__main__":
    fine_tune_model()
