import json

# Load dataset
with open("data/dialogue_data.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

print(f"Loaded {len(dataset)} conversations from dataset.")


