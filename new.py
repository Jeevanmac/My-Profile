import asyncio
import websockets
from transformers import pipeline

# List of harmful words (can be used in combination with NLP model if needed)
harmful_words = ["bomb", "attack", "fire"]

# Load the NLP model for toxic language detection
nlp_toxic = pipeline("text-classification", model="unitary/toxic-bert")

# Function to detect harmful content using both predefined harmful words and the NLP model
def detect_harmful_words(message):
    # Check for predefined harmful words
    for word in harmful_words:
        if word in message.lower():
            return True
    
    # Check using the transformer NLP model
    result = nlp_toxic(message)
    return any(res['label'] == 'TOXIC' for res in result)

# WebSocket server handling messages
async def chat_server(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")

        # Check for harmful content in the message
        if detect_harmful_words(message):
            await websocket.send("Danger: Harmful content detected!")
        else:
            await websocket.send(message)

# Start WebSocket server on localhost:8080
start_server = websockets.serve(chat_server, "localhost", 8080)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
