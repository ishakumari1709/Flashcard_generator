# 🧠 LLM-Powered Flashcard Generator

This is a lightweight yet powerful **Flashcard Generator** that uses a Hugging Face Large Language Model to convert educational content into **question-answer flashcards**. Built using **Python** and **Streamlit**, it supports `.txt` / `.pdf` input, auto-generates 15 flashcards, allows editing, and offers export to **CSV** and **JSON** formats.

---

## 🔍 Project Overview

Many students and educators need an efficient way to revise key concepts from long academic texts. This tool reads textbook or lecture content and turns it into editable flashcards — saving time, improving retention, and making study smarter.

---

## ✅ Features

- Upload `.txt` or `.pdf` documents
- Paste raw educational text directly
- Generate up to **15 question-answer flashcards**
- Each flashcard includes:
  - **Question**
  - **Answer**
  - **Difficulty Level** (Easy, Medium, Hard)
- Edit questions & answers before exporting
- Export to:
  - CSV
  - JSON

---

## 📸 Screenshot

![Screenshot 2025-06-17 151923](https://github.com/user-attachments/assets/19c6512b-d0c8-4ebe-8b8d-db65880797a9)
![Screenshot 2025-06-17 152240](https://github.com/user-attachments/assets/c141fee3-81c8-4e98-9c81-1e6ec72247ac)



---

## 📦 Folder Structure
flashcard_generator/
├── app.py # Streamlit main app
├── flashcard_generator.py # Flashcard generation logic
├── utils.py # File reading + export functions
├── prompt_template.txt # Optional template for LLMs
├── requirements.txt # Project dependencies
└── README.md # This documentation

---

## 🧠 How It Works

1. The app uses Hugging Face’s `valhalla/t5-small-qa-qg-hl` model.
2. It highlights sentences to generate questions using a special prompt.
3. Each flashcard is tagged with a difficulty level based on sentence length.
4. Flashcards can be edited in the browser.
5. Final cards are exported as `.csv` or `.json`.

---




