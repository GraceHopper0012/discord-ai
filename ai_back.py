from transformers import TFAutoModelForCausalLM, AutoTokenizer, pipeline

# Modellname anpassen
model_name = "stefan-it/german-gpt2-larger"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForCausalLM.from_pretrained(model_name)

chat = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

# Liste für den Gesprächskontext
conversation_history = []

while True:
    user_input = input("Du: ")
    
    # Füge die neue Nachricht zur Konversation hinzu
    conversation_history.append(f"Du: {user_input}")
    
    # Behalte nur die letzten 10 Nachrichten
    conversation_history = conversation_history[-10:]
    
    # Kombiniere alle Nachrichten zu einem Eingabetext
    input_text = "\n".join(conversation_history)
    
    # Generiere die Antwort
    response = chat(input_text, max_length=150)[0]["generated_text"]
    
    # Extrahiere die Antwort des Bots
    bot_response = response.split("Bot:")[-1].strip()
    
    print("Bot:", bot_response)
    
    # Füge die Antwort des Bots zur Konversation hinzu
    conversation_history.append(f"Bot: {bot_response}")
