from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import openai
import subprocess

app = Flask(__name__)

# Path to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Global variable for OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        api_key = request.form['api_key']
        os.environ['OPENAI_API_KEY'] = api_key
        return render_template('setup.html', success=True)
    return render_template('setup.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'json_file' not in request.files:
            return render_template('upload.html', error="No file selected!")
        
        file = request.files['json_file']
        if file.filename == '':
            return render_template('upload.html', error="No file selected!")

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return render_template('upload.html', success=True, filepath=filepath)
    return render_template('upload.html')


@app.route('/fine_tune', methods=['POST'])
def fine_tune():
    data_file = request.form['file_path']
    model = request.form.get('model', 'curie')
    cmd = f"openai api fine_tunes.create -t {data_file} -m {model}"
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)

    if result.returncode != 0:
        return jsonify({'status': 'error', 'message': result.stderr})

    return jsonify({'status': 'success', 'message': result.stdout})


@app.route('/test', methods=['GET', 'POST'])
def test_model():
    if request.method == 'POST':
        model_name = request.form['model_name']
        prompt = request.form['prompt']
        try:
            response = openai.Completion.create(
                model=model_name,
                prompt=prompt,
                max_tokens=100,
                temperature=0.7,
                stop=["\n"]
            )
            return render_template('test.html', response=response["choices"][0]["text"].strip())
        except Exception as e:
            return render_template('test.html', error=str(e))
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
