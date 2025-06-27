from transformers import TFAutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "stefan-it/german-gpt2-larger"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForCausalLM.from_pretrained(model_name)

chat = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

conversation_history = []

def respond(input_text):
    print(conversation_history)

    
    response = chat(input_text, max_new_tokens=50)[0]["generated_text"]
    
    bot_response = response.split("assistant:")[-1].strip()
    
    print("Bot:", bot_response)
    
    conversation_history.append({"role": "assistant", "content": bot_response})

    return bot_response
