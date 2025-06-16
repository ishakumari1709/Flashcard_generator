import streamlit as st
from flashcard_generator import generate_flashcards
from utils import extract_text_from_file, save_as_csv, save_as_json
import pandas as pd

st.set_page_config(page_title="LLM Flashcard Generator", layout="wide")
st.title("🧠 Flashcard Generator with FLAN-T5")

uploaded_file = st.file_uploader("📄 Upload .txt or .pdf", type=["txt", "pdf"])
text_input = st.text_area("Or paste educational content here", height=200)
subject = st.selectbox("📘 Subject (optional)", ["General", "Biology", "History", "Computer Science"])

input_text = extract_text_from_file(uploaded_file) if uploaded_file else text_input

if st.button("⚡ Generate Flashcards") and input_text:
    flashcards = generate_flashcards(input_text)

    if flashcards:
        st.success(f"✅ Generated {len(flashcards)} flashcards")
        edited_data = []

        for i, card in enumerate(flashcards, 1):
            st.markdown(f"### Flashcard {i}")
            q = st.text_input(f"Question {i}", value=card["Question"])
            a = st.text_input(f"Answer {i}", value=card["Answer"])
            d = st.selectbox(f"Difficulty {i}", ["Easy", "Medium", "Hard"], index=["Easy", "Medium", "Hard"].index(card["Difficulty"]))
            edited_data.append({"Question": q, "Answer": a, "Difficulty": d})
            st.markdown("---")

        st.subheader("📤 Export Flashcards")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Export as CSV"):
                csv_file = save_as_csv(edited_data)
                st.download_button("Download CSV", open(csv_file, "rb"), file_name="flashcards.csv")
        with col2:
            if st.button("Export as JSON"):
                json_file = save_as_json(edited_data)
                st.download_button("Download JSON", open(json_file, "rb"), file_name="flashcards.json")
    else:
        st.error("No flashcards could be generated. Try a different input.")
