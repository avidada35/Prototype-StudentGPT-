import json
import os

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data/dialogue_data.json")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("✅ JSON file is valid and correctly formatted.")
except json.JSONDecodeError as e:
    print(f"❌ JSON Error: {e}")
except FileNotFoundError:
    print(f"❌ File not found. Make sure dialogue_data.json exists in the 'data' folder.")
