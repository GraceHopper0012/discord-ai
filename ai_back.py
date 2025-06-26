from transformers import TFAutoModelForCausalLM, AutoTokenizer, pipeline

name = "microsoft/DialoGPT-small"
tok = AutoTokenizer.from_pretrained(name)
model = TFAutoModelForCausalLM.from_pretrained(name)

chat = pipeline("text-generation", model=model, tokenizer=tok, framework="tf", device=-1)
while True:
    print("Bot: " + chat(input("Du:"), max_length=50)[0]["generated_text"])

"""
pipe = pipeline(model="microsoft/DialoGPT-small", framework="tf")
"""