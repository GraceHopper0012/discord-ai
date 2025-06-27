from transformers import TFAutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "stefan-it/german-gpt2-larger"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForCausalLM.from_pretrained(model_name)

chat = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)


def respond(input_text):

    
    response = chat(input_text, max_new_tokens=50)[0]["generated_text"]

    return response
