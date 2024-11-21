#!/bin/bash

# Step 1: Prepare the data
openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl

# Step 2: Train the model
openai api fine_tunes.create \
  -t "drug_malady_data_prepared_train.jsonl" \
  -v "drug_malady_data_prepared_valid.jsonl" \
  --compute_classification_metrics \
  --classification_n_classes 3 \
  -m ada \
  --suffix "drug_malady_data"
