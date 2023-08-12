from flask import Flask, render_template, jsonify, request


import os
from os.path import exists, join, isdir
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, GenerationConfig
from peft import PeftModel
from peft.tuners.lora import LoraLayer

#generation configs
max_new_tokens = 32
top_p = 0.9
temperature = 0.9

#Base model
model_name_or_path = "huggyllama/llama-7b"

#adapter
adapter_path = "./models/checkpoint-9750"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(
     model_name_or_path,
     torch_dtype=torch.bfloat16,
     device_map={"": 0},
     load_in_4bit=True,
     quantization_config=BitsAndBytesConfig(
         load_in_4bit=True,
         bnb_4bit_compute_dtype=torch.bfloat16,
         bnb_4bit_use_double_quant=True,
         bnb_4bit_quant_type='nf4',
     )
)

model = PeftModel.from_pretrained(model, adapter_path)

prompt = (
    "This is a conversation between a human and an AI assistant. "
    "You the AI assistant will reply to the messages of the human in a helpful way. "
    "### Human: {} "
    "### AI Assistant: "
)

def generate(model, inpt, max_new_tokens=max_new_tokens, top_p=top_p, temperature=temperature):
    inputs = tokenizer(inpt, return_tensors="pt").to('cuda')

    outputs = model.generate(
        **inputs,
        generation_config=GenerationConfig(
            do_sample=True,
            max_new_tokens=max_new_tokens,
            top_p=top_p,
            temperature=temperature,
        )
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text




app = Flask(__name__)



@app.route("/")
def handle_home():
    return render_template("index.html")

@app.route("/chat", methods = ["POST"])
def handle_chat():
    data = request.json
    
    message = data["message"]
    
    inpt = prompt.format(message)
    response = generate(model, inpt)

    response = response[len(inpt): len(response)]

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
