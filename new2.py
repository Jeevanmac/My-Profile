from transformers import pipeline

# Load the NLP model for toxic language detection
nlp_toxic = pipeline("text-classification", model="unitary/toxic-bert")

# Function to detect harmful content using the model
def detect_harmful_content_with_model(message):
    result = nlp_toxic(message)
    return any(res['label'] == 'TOXIC' for res in result)

# Modify the detect_harmful_words function to use the model
def detect_harmful_words(message):
    return detect_harmful_content_with_model(message)
