# Fine-Tuning with OpenAI Models

This project demonstrates how to fine-tune OpenAI models using a structured, step-by-step approach. It covers preparing a dataset, fine-tuning a model, and using the fine-tuned model for specific tasks.

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
  - [Step 4: Use the Fine-Tuned Model](#step-4-use-the-fine-tuned-model)
  - [Step 5: Analyze and Manage Models](#step-5-analyze-and-manage-models)
- [Dependencies](#dependencies)

---

## Overview

This repository provides a complete workflow for fine-tuning OpenAI models with your custom dataset. The steps include data preparation, fine-tuning using OpenAI's API, and testing the fine-tuned model.

### Key Highlights:
- Create and preprocess datasets in JSONL format.
- Fine-tune OpenAI models such as `curie` or `davinci`.
- Test the model with a user-friendly script.
- Manage and analyze fine-tuned models.

---

## Features

- **Data Preparation**: Convert data into JSONL format and preprocess it.
- **Model Fine-Tuning**: Use OpenAI API to fine-tune models with a custom dataset.
- **Testing**: Interact with the fine-tuned model using Python.
- **Automation**: Automate the workflow with a single script (`run.sh`).

---

## Project Structure

```
fine-tuning-project/
├── setup.py               # Environment setup script
├── data_prep.py           # Script to create JSONL dataset
├── prepare_data.sh        # CLI script to preprocess data
├── fine_tune.py           # Script to fine-tune the model
├── use_model.py           # Script to test the fine-tuned model
├── analyze_model.py       # Script to analyze model results
├── list_models.py         # Script to list available models
├── delete_model.py        # Script to delete a fine-tuned model
├── run.sh                 # Script to run the workflow sequentially
├── data.jsonl             # Initial dataset (example)
└── data_prepared.jsonl    # Processed dataset for fine-tuning
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
   pip install openai
   ```

3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

---

## How to Run

To run the entire workflow sequentially, execute the `run.sh` script:
```bash
./run.sh
```

Alternatively, you can run individual scripts for specific steps.

---

## Workflow Details

### Step 1: Setup Environment
- Run `setup.py` to set up the Python environment and configure the OpenAI API key.
- Prompts you to enter your OpenAI API key.

### Step 2: Prepare Dataset
- Use `data_prep.py` to create a JSONL file for fine-tuning.
- Preprocess the dataset with `prepare_data.sh` to make it compatible with OpenAI's fine-tuning requirements.

### Step 3: Fine-Tune Model
- Run `fine_tune.py` to fine-tune the model with the processed dataset.
- Outputs the name of the fine-tuned model.

### Step 4: Use the Fine-Tuned Model
- Use `use_model.py` to test the fine-tuned model.
- Input a prompt to generate responses from the model.

### Step 5: Analyze and Manage Models
- Use `analyze_model.py` to analyze the fine-tuning process and results.
- List all fine-tuned models with `list_models.py`.
- Delete models no longer needed using `delete_model.py`.

---

## Dependencies

- [Python 3.7+](https://www.python.org/)
- [OpenAI Python Library](https://pypi.org/project/openai/)

Install dependencies:
```bash
pip install openai
```

---


## Contributions

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or additional features.

---

