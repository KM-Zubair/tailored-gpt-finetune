# Fine-Tuning with OpenAI Models

This project demonstrates how to fine-tune OpenAI models using a structured, step-by-step approach. It includes a web-based user interface (UI) built with Flask for an intuitive and interactive workflow.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Workflow Details](#workflow-details)
  - [Step 1: Setup Environment](#step-1-setup-environment)
  - [Step 2: Prepare Dataset](#step-2-prepare-dataset)
  - [Step 3: Fine-Tune Model](#step-3-fine-tune-model)
  - [Step 4: Test Fine-Tuned Model](#step-4-test-fine-tuned-model)
  - [Step 5: Analyze and Manage Models](#step-5-analyze-and-manage-models)
- [Dependencies](#dependencies)

---

## Overview

This repository provides two approaches to fine-tuning OpenAI models:
1. A **command-line workflow** with modular Python scripts.
2. A **Flask-based web application** for an interactive and user-friendly experience.

---

## Features

- **Data Preparation**: Convert data into JSONL format and preprocess it.
- **Model Fine-Tuning**: Use OpenAI API to fine-tune models with a custom dataset.
- **Testing**: Interact with the fine-tuned model using Python or the UI.
- **Automation**: Automate the workflow with a single script (`run.sh`).
- **Web UI**: Intuitive interface to upload datasets, set up API keys, and test models.

---

## Project Structure

```
fine-tuning-project/
├── app.py               # Flask-based UI backend
├── setup.py             # Environment setup script
├── data_prep.py         # Script to create JSONL dataset
├── prepare_data.sh      # CLI script to preprocess data
├── fine_tune.py         # Script to fine-tune the model
├── use_model.py         # Script to test the fine-tuned model
├── analyze_model.py     # Script to analyze model results
├── list_models.py       # Script to list available models
├── delete_model.py      # Script to delete a fine-tuned model
├── run.sh               # Script to run the workflow sequentially
├── templates/           # HTML templates for Flask UI
│   ├── index.html       # Main dashboard
│   ├── setup.html       # API key setup page
│   ├── upload.html      # Dataset upload page
│   ├── test.html        # Model testing page
└── uploads/             # Directory to store uploaded files
```

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fine-tuning-project.git
   cd fine-tuning-project
   ```

2. Install required dependencies:
   ```bash
   pip install flask openai
   ```

3. Set your OpenAI API key manually (for scripts):
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

---

## How to Run

### Running the Web Application
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser at `http://127.0.0.1:5000/`.

3. Use the UI for:
   - Setting up the API key.
   - Uploading a dataset (JSONL format).
   - Testing the fine-tuned model.

### Running the Command-Line Workflow
Execute the `run.sh` script to automate the workflow:
```bash
./run.sh
```

---

## Workflow Details

### Step 1: Setup Environment
- **Command Line**: Run `setup.py` to set up the environment and configure the OpenAI API key.
- **UI**: Navigate to the "Setup OpenAI API Key" page.

### Step 2: Prepare Dataset
- **Command Line**: Use `data_prep.py` and `prepare_data.sh` to prepare the dataset.
- **UI**: Upload the dataset via the "Upload Dataset" page.

### Step 3: Fine-Tune Model
- **Command Line**: Run `fine_tune.py` to start fine-tuning.
- **UI**: Use the "Fine-Tune Model" functionality (coming soon for UI).

### Step 4: Test Fine-Tuned Model
- **Command Line**: Run `use_model.py` to interact with the fine-tuned model.
- **UI**: Use the "Test Fine-Tuned Model" page.

### Step 5: Analyze and Manage Models
- **Command Line**:
  - Analyze results: `analyze_model.py`
  - List models: `list_models.py`
  - Delete models: `delete_model.py`

---

## Dependencies

- [Python 3.7+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenAI Python Library](https://pypi.org/project/openai/)

Install dependencies:
```bash
pip install flask openai
```


## Contributions

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or additional features.

---
