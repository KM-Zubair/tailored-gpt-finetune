#!/bin/bash

echo "============================="
echo "Fine-Tuning Project Workflow"
echo "============================="

# Step 1: Set up the environment
echo "Step 1: Setting up the environment..."
python setup.py
if [ $? -ne 0 ]; then
    echo "Error during environment setup. Exiting..."
    exit 1
fi

# Step 2: Prepare the data
echo "Step 2: Creating and preparing the data file..."
python data_prep.py
if [ $? -ne 0 ]; then
    echo "Error during data preparation. Exiting..."
    exit 1
fi

bash prepare_data.sh
if [ $? -ne 0 ]; then
    echo "Error during data preparation with OpenAI CLI. Exiting..."
    exit 1
fi

# Step 3: Fine-tune the model
echo "Step 3: Fine-tuning the model..."
python fine_tune.py
if [ $? -ne 0 ]; then
    echo "Error during fine-tuning. Exiting..."
    exit 1
fi

# Step 4: List available models
echo "Step 4: Listing available fine-tuned models..."
python list_models.py
if [ $? -ne 0 ]; then
    echo "Error during listing models. Exiting..."
    exit 1
fi

# Step 5: Analyze fine-tuned model
echo "Step 5: Analyzing the fine-tuned model..."
echo "Please enter the fine-tune job ID to analyze:"
read JOB_ID
python analyze_model.py $JOB_ID
if [ $? -ne 0 ]; then
    echo "Error during model analysis. Exiting..."
    exit 1
fi

# Step 6: Test the fine-tuned model
echo "Step 6: Testing the fine-tuned model..."
echo "Please enter the fine-tuned model name:"
read MODEL_NAME
python use_model.py $MODEL_NAME
if [ $? -ne 0 ]; then
    echo "Error during model testing. Exiting..."
    exit 1
fi

echo "============================="
echo "Workflow completed successfully!"
echo "============================="
