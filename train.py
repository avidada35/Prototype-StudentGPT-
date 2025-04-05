from datasets import load_dataset

dataset = load_dataset("json", data_files="data/dialogue_data.json")  # Load your JSON file
#print(dataset["train"][0])  # Print the first conversation

from transformers import AutoTokenizer, AutoModelForCausalLM

# Load a small, beginner-friendly model (like GPT-2)
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# If you want to use DeepSeek later, replace "gpt2" with "deepseek-ai/deepseek-llm"


def tokenize_function(examples):
    return tokenizer(examples["user"] + " " + examples["ai"])  # Combine user + AI response

tokenized_dataset = dataset.map(tokenize_function, batched=True)


from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./results",  # Where to save the model
    per_device_train_batch_size=1,  # Reduce if your GPU runs out of memory
    num_train_epochs=3,  # How many times to go through your data
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
)

trainer.train()  # This starts the training!