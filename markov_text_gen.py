import re
import random
from collections import defaultdict

# Step 1: Clean the text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# Step 2: Build a 2-word-based Markov chain
def build_markov_chain(words):
    markov_chain = defaultdict(list)
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        markov_chain[key].append(words[i + 2])
    return markov_chain

# Step 3: Generate new text
def generate_text(chain, length=150):
    start_key = random.choice(list(chain.keys()))
    word1, word2 = start_key
    result = [word1, word2]
    
    for _ in range(length - 2):
        next_words = chain.get((word1, word2))
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        word1, word2 = word2, next_word
    
    return ' '.join(result)

# Step 4: Main execution
if __name__ == "__main__":
    try:
        with open("sample.txt", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("❌ sample.txt not found. Please add it in the same folder.")
        exit()

    words = preprocess_text(text)
    chain = build_markov_chain(words)
    generated = generate_text(chain, length=200)

    print("\n📢 Generated Text:\n")
    print(generated)
