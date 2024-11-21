# use_model.py
import openai

def use_fine_tuned_model(model_name, prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model=model_name,
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        stop=["\n"]
    )
    print("Response:", response["choices"][0]["text"].strip())

if __name__ == "__main__":
    model_name = input("Enter your fine-tuned model name: ")
    prompt = input("Enter your prompt: ")
    use_fine_tuned_model(model_name, prompt)
