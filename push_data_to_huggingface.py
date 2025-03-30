import os
import json

from datasets import Dataset
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()

with open("dataset.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

adapted_data = []
for conversation in raw_data:
    adapted_data.append({
        "messages": conversation,
        "language": "Moroccan Darija",
    })

dataset = Dataset.from_list(adapted_data)
hf_token = os.environ.get("HF_TOKEN")
api = HfApi(token=hf_token)
dataset.push_to_hub(
    "ImadSaddik/BoDmaghDataset",
    token=hf_token,
    commit_message="Update dataset from GitHub repository"
)
