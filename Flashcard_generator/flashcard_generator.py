from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "valhalla/t5-small-qa-qg-hl"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_flashcards(text, max_cards=15):
    sentences = [s.strip() for s in text.strip().split('.') if len(s.strip().split()) > 5]
    flashcards = []

    for sent in sentences[:max_cards]:
        if not sent:
            continue
        hl_context = text.replace(sent, f"<hl> {sent} <hl>")
        prompt = f"generate question: {hl_context}"

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=64,
                num_beams=4,
                do_sample=False
            )

        question = tokenizer.decode(outputs[0], skip_special_tokens=True)
        difficulty = "Easy" if len(sent.split()) < 10 else "Medium" if len(sent.split()) < 20 else "Hard"
        flashcards.append({
            "Question": question.strip(),
            "Answer": sent,
            "Difficulty": difficulty
        })

    return flashcards

