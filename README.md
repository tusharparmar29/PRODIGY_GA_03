# 🚀 Task-03: Text Generation with Markov Chains
---

## 📌 Project Overview

This project demonstrates **text generation** using a **Markov Chain**-based language model. The algorithm learns word sequences from a training dataset and generates new text that mimics the structure and style of the original input.

---

## 🧠 What is a Markov Chain?

A Markov Chain is a statistical model where the next state (word) depends only on a fixed number of previous states. In this case, the model uses **2-word sequences (bigrams)** to predict the next word.

---

## 📁 Folder Structure

├── markov_text_gen.py # Main Python script
├── sample.txt # Training text file (input)
└── README.md # Project documentation


---

## ⚙️ How It Works

1. **Input**: A text file (`sample.txt`) containing training sentences
2. **Processing**:
   - Text is cleaned and tokenized
   - A dictionary of word pairs is created
   - A Markov Chain is built using bigrams
3. **Output**: Generated text with a similar pattern and vocabulary

---

## ▶️ How to Run

### 🧑‍💻 Requirements
- Python 3.x (no external libraries required)
- VS Code or any Python IDE

### 🔧 Setup Instructions

1. Clone or download this repository
2. Add or edit the file `sample.txt` with your custom training text
3. Run the program:

python markov_text_gen.py
