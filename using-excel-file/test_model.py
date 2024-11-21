import os
import openai

# Step 1: Load API keys from environment
def init_api():
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")

init_api()

# Step 2: Define the model
model = "ada:ft-learninggpt:drug-malady-data-2023-02-21-20-36-07"

# Step 3: Test with sample drugs
drugs = [
    "A CN Gel(Topical) 20gmA CN Soap 75gm",  # Class 0
    "Addnok Tablet 20'S",                    # Class 1
    "ABICET M Tablet 10's",                  # Class 2
]

class_map = {
    0: "Acne",
    1: "ADHD",
    2: "Allergies",
}

for drug_name in drugs:
    prompt = f"Drug: {drug_name}\nMalady:"
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )
    result = response.choices[0].text.strip()
    print(f"{drug_name} is used for {class_map.get(int(result), 'Unknown')}.")
