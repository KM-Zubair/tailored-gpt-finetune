# data_prep.py
import json

def create_jsonl_file():
    examples = [
        {"prompt": "When do I have to start the heater?", "completion": " Every day in the morning at 7AM. You should stop it at 2PM.\n"},
        {"prompt": "Where is the garage remote control?", "completion": " Next to the yellow door, on the key ring.\n"},
        {"prompt": "Is it necessary to program the scent diffuser every day?", "completion": " The scent diffuser is already programmed, you just need to recharge it when its battery is low.\n"}
    ]

    with open("data.jsonl", "w") as f:
        for example in examples:
            f.write(json.dumps(example) + "\n")
    print("JSONL file created: data.jsonl")

if __name__ == "__main__":
    create_jsonl_file()
