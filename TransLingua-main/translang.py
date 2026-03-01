# ======================================
# TransLingua – AI Powered Translator
# (Supports Multiple Languages)
# ======================================

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# --------------------------------------
# Load API key
# --------------------------------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY not found in .env file")
    st.stop()

# --------------------------------------
# Configure Gemini
# --------------------------------------
genai.configure(api_key=API_KEY)

# --------------------------------------
# Auto-detect a usable model (IMPORTANT)
# --------------------------------------
available_model = None
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        available_model = m.name
        break

if not available_model:
    st.error("❌ No text-generation model available for this API key.")
    st.stop()

model = genai.GenerativeModel(available_model)

# --------------------------------------
# Streamlit UI
# --------------------------------------
st.set_page_config(
    page_title="TransLingua – AI Translator",
    page_icon="🌐"
)

st.title("🌐 TransLingua – AI Powered Language Translator")
st.caption(f"Using model: {available_model}")

# --------------------------------------
# Language List (EXTENDED)
# --------------------------------------
languages = [
    "English",
    "Hindi",
    "Tamil",
    "Telugu",
    "Kannada",
    "Malayalam",
    "Marathi",
    "Bengali",
    "Urdu",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Russian",
    "Arabic",
    "Chinese",
    "Japanese",
    "Korean"
]

# --------------------------------------
# Translation function
# --------------------------------------
def translate_text(text, source_language, target_language):
    prompt = f"""
    Translate the following text from {source_language} to {target_language}.
    Return ONLY the translated text.

    Text:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# --------------------------------------
# User Inputs
# --------------------------------------
text = st.text_area("✍️ Enter text to translate")

source_language = st.selectbox("🌍 Source Language", languages)
target_language = st.selectbox("🌐 Target Language", languages)

# --------------------------------------
# Translate Button
# --------------------------------------
if st.button("🔁 Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Translating..."):
            translated_text = translate_text(
                text, source_language, target_language
            )

        st.subheader("📘 Translated Text")
        st.success(translated_text)
