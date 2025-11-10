import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "j-hartmann/emotion-english-distilroberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


label_names = ['anger','disgust','fear','joy','neutral','sadness','surprise']

st.title("🎭 EmotionSense AI")
st.write("Enter text and I will detect the emotion!")

user_input = st.text_input("Type something:")

if user_input:
    inputs = tokenizer(user_input, return_tensors="pt")
    logits = model(**inputs).logits
    pred = torch.argmax(logits).item()
    emotion = label_names[pred]
    st.success(f"**Emotion:** {emotion}")
