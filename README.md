
# 🗣️ Grammar Error Correction System – “Error Ears”

A real-time, voice-enabled grammar correction web application that leverages **Google Web Speech API**, **Flask**, and **fine-tuned Transformer-based models** (T5 variants). This project, named **Error Ears**, empowers users to speak naturally and receive grammatically corrected text instantly on a webpage.

---

## 🔍 Overview

Grammatical errors hinder clarity in communication, especially in spontaneous speech. **Error Ears** introduces an intelligent solution using **fine-tuned T5 models** to correct spoken input. The system listens to speech, converts it to text, detects grammar issues, and displays corrected sentences—all in real-time within a web app.

---

## 🧠 Core Features

- 🎙️ **Voice Input**: Integrated with **Google Web Speech API** (JavaScript) to capture live speech.
- 📝 **Grammar Correction**: Fine-tuned **T5-Base** and **T5-Small** models for real-time correction.
- 🌐 **Web Interface**: Built using **Flask**, **HTML**, **CSS**, and **JavaScript**.
- 📊 **Accuracy-Focused**: Evaluated with **Levenshtein similarity score** and **BLEU score**.
- 🔁 **Real-Time Feedback**: Corrected output displayed instantly on the web interface.

---

## 🧰 Technologies Used

- **Python**
- **Flask**
- **HuggingFace Transformers (T5)**
- **Google Web Speech API (JavaScript)**
- **HTML/CSS/JavaScript**
- **Dataset**: Subset of **C4 200M**, along with **JFLEG**, **ASSET**, and **DISCOFUSE**

---

## 🗂️ Project Structure

```bash
📁 grammar-error-correction/
 ┣ 📂static/
 ┃ ┗ 📄 style.css
 ┣ 📂templates/
 ┃ ┗ 📄 index.html
 ┣ 📄 app.py
 ┣ 📄 model_inference.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 📊 Dataset Summary

| Dataset        | Description                                            |
|----------------|--------------------------------------------------------|
| **C4 200M**    | Clean, large-scale grammar error dataset (Google)     |
| **JFLEG**      | Fluency corrections for learner English               |
| **ASSET**      | Text simplification and fluency for easy comprehension|
| **DISCOFUSE**  | Discourse-based sentence rewriting                    |

---

## 🧪 Models Compared

| Model              | Type        | Similarity Score | BLEU Score |
|-------------------|-------------|------------------|------------|
| **T5-Base**        | Fine-tuned  | 0.85             | 0.60       |
| **T5-Small**       | Fine-tuned  | 0.84             | 0.56       |
| CoEdIT             | Pretrained  | 0.74             | 0.44       |
| Custom T5-Large    | Pretrained  | 0.73             | 0.435      |

✅ Fine-tuned models **outperformed pretrained counterparts** in both accuracy metrics.

---

## 🧪 Evaluation Metrics

- **Levenshtein Similarity Score**  
  Measures edit distance between predicted and correct sentences.

- **BLEU Score**  
  Measures closeness to reference corrections (ideal: 0.6–0.7+).

---

## 🔄 Workflow

1. 🎤 **Voice Input**: Captured via browser using Web Speech API.
2. 🗣️ **Text Transcription**: JavaScript converts speech to text.
3. 📤 **Send to Flask**: Transcribed text sent to Flask backend.
4. 🔍 **Grammar Correction**: Inference done using fine-tuned T5 model.
5. 🖥️ **Output**: Corrected sentence returned and displayed.

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Prakharjain007/grammar-error-correction.git
cd grammar-error-correction
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 🌍 Applications

- 🔸 Virtual Assistants
- 🔸 Language Learning Tools
- 🔸 Voice Bots
- 🔸 Accessibility Tools
- 🔸 Smart Classrooms

---

## 📚 References

- [T5: Exploring the Limits of Transfer Learning](https://arxiv.org/abs/1910.10683)
- [CoEdIT Grammar Model](https://huggingface.co/google/flan-t5-large)
- JFLEG, ASSET, DISCOFUSE datasets

---

## 📬 Contact

**Prakhar Jain**  
📧 jainprakhar0712@gmail.com 
🔗 [GitHub](https://github.com/Prakharjain007)

---

## 📄 License

This project is for academic and research purposes. For commercial use, please contact the author.
