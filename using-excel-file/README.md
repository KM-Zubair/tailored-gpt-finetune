# **Drug Classification Using OpenAI Fine-Tuning**

This project demonstrates how to fine-tune an OpenAI model for drug classification using a dataset of 2000 drugs and their associated maladies. The system provides a user-friendly web interface for testing the model and classifying new drug names.

---

## [Presentation Slides](https://docs.google.com/presentation/d/1G_auwClcmFBywkF_b6q9nEMuqgu5s6uMwc2bDyyppmM/edit?usp=sharing)


## **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
  - [Dependencies](#dependencies)
  - [Data Preparation](#data-preparation)
  - [Fine-Tuning](#fine-tuning)
  - [Running the Web Application](#running-the-web-application)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)

---

## **Project Overview**

The goal of this project is to fine-tune OpenAI's `ada` model to classify drugs into their corresponding maladies based on their names. The dataset contains 2000 samples of drugs and their descriptions, making it ideal for fine-tuning a classification model.

---

## **Features**

- **Data Preparation**: Converts Excel data into JSONL format for fine-tuning.
- **Fine-Tuning**: Uses OpenAI's API to fine-tune the `ada` model.
- **Web Interface**: A responsive web application for drug classification.
- **Error Handling**: Provides user-friendly feedback for invalid inputs or API errors.

---

## **Technologies Used**

- **Backend**: Flask
- **Frontend**: HTML, Bootstrap 5
- **Data Processing**: Pandas
- **API**: OpenAI API for fine-tuning and classification

---

## **Setup Instructions**

### **Dependencies**

Ensure the following are installed:
- Python 3.8 or later
- Required Python packages:
  ```bash
  pip install flask openai pandas
  ```

---

### **Data Preparation**

1. Place the Excel file (`Medicine_description_2000.xlsx`) in the project directory.
2. Run the `prepare_data.py` script to convert the data into JSONL format:
   ```bash
   python prepare_data.py
   ```

---

### **Fine-Tuning**

1. Prepare the data for fine-tuning:
   ```bash
   openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl
   ```
2. Fine-tune the model:
   ```bash
   openai api fine_tunes.create \
     -t "drug_malady_data_prepared_train.jsonl" \
     -v "drug_malady_data_prepared_valid.jsonl" \
     --compute_classification_metrics \
     --classification_n_classes 3 \
     -m ada \
     --suffix "drug_malady_data"
   ```

---

### **Running the Web Application**

1. Ensure your API key and organization ID are set as environment variables on your PC:
   - **Windows**:
     Set the variables via `Environment Variables` in the System Properties or use:
     ```bash
     setx API_KEY your_openai_api_key
     setx ORG_ID your_openai_organization_id
     ```
   - **Linux/Mac**:
     Add the following to your shell configuration file (e.g., `.bashrc` or `.zshrc`):
     ```bash
     export API_KEY=your_openai_api_key
     export ORG_ID=your_openai_organization_id
     ```

2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Open the browser and go to `http://127.0.0.1:5000`.

---

## **Usage**

1. Enter a drug name in the input field.
2. Submit the form to classify the drug.
3. View the result, which displays the corresponding malady.

---

## **Folder Structure**

```
project/
│
├── app.py                       # Flask application
├── prepare_data.py              # Script for data preparation
├── fine_tune.sh                 # Shell script for fine-tuning
├── templates/
│   └── index.html               # Frontend HTML template
├── static/                      # Optional folder for additional CSS or JS
├── Medicine_description_2000.xlsx  # Excel dataset with 2000 samples
├── drug_malady_data.jsonl       # Prepared JSONL file for fine-tuning
└── README.md                    # Project documentation
```

---

## **Future Enhancements**

- Add support for batch classification of multiple drugs.
- Improve the classification accuracy with a larger dataset.
- Integrate more robust error handling and logging.
- Deploy the application on a cloud platform (e.g., AWS, Azure, or Heroku).

---
