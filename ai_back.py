from transformers import TFAutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "stefan-it/german-gpt2-larger"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForCausalLM.from_pretrained(model_name)

chat = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

conversation_history = []

while True:
    user_input = input("Du: ")
    
    # Füge die neue Nachricht zur Konversation hinzu
    conversation_history.append({"role": "user", "content": user_input})
    
    # Behalte nur die letzten 10 Nachrichten
    conversation_history = conversation_history[-10:]
    
    # Erstelle die Eingabe für das Modell
    input_text = ""
    for message in conversation_history:
        input_text += f"{message['role']}: {message['content']}\n"
    
    # Generiere die Antwort
    response = chat(input_text, max_length=150)[0]["generated_text"]
    
    # Extrahiere die Antwort des Bots
    bot_response = response.split("assistant:")[-1].strip()
    
    print("Bot:", bot_response)
    
    # Füge die Antwort des Bots zur Konversation hinzu
    conversation_history.append({"role": "assistant", "content": bot_response})
