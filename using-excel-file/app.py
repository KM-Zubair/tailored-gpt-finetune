import os
import openai
from flask import Flask, request, render_template

app = Flask(__name__)



openai.api_key = os.environ.get("API_KEY")
openai.organization = os.environ.get("ORG_ID")


# Define model ID
model = "ada:ft-learninggpt:drug-malady-data-2023-02-21-20-36-07"

# Malady map
class_map = {
    0: "Acne",
    1: "ADHD",
    2: "Allergies",
    # Add more mappings if necessary
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_drug():
    drug_name = request.form.get('drug_name')
    prompt = f"Drug: {drug_name}\nMalady:"

    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=1,
            max_tokens=1,
        )
        result = response.choices[0].text.strip()
        malady = class_map.get(int(result), "Unknown")
        return render_template('index.html', drug_name=drug_name, malady=malady)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
