# AI Agent using Hugging Face Transformers

A lightweight AI agent built using Hugging Face Transformers for natural language processing tasks such as **sentiment analysis** and **text summarization**. The agent runs locally via terminal and provides an interactive menu.

---

## Features

- **Sentiment Analysis**: Analyze the sentiment of any text input.
- **Text Summarization**: Generate concise summaries of long texts.
- Easy to run locally using Python.

---

## Python Script (ai_agent.py)

Create a file named `ai_agent.py` with the following content:

```python
"""
AI Agent using Hugging Face Transformers
Author: Vinay Kumar R
Description:
A lightweight AI agent built using Hugging Face for natural language processing tasks
like summarization and sentiment analysis. Run locally via terminal.
"""

from transformers import pipeline

# Load pre-trained NLP pipelines
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_text():
    print("=== AI Agent using Hugging Face ===")
    print("1. Sentiment Analysis")
    print("2. Summarization")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            text = input("Enter text for sentiment analysis: ")
            result = sentiment_analyzer(text)[0]
            print(f"Sentiment: {result['label']} | Score: {result['score']:.2f}")

        elif choice == "2":
            text = input("Enter text for summarization: ")
            summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
            print(f"Summary: {summary[0]['summary_text']}")

        elif choice == "0":
            print("Exiting AI Agent.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    analyze_text()
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/huggingface-ai-agent.git
cd huggingface-ai-agent
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Dependencies (requirements.txt)
Create a file named requirements.txt with the following content:

shell
Copy code
transformers>=4.35.0
torch>=2.0.0
sentencepiece>=0.1.99
These are required for the Hugging Face pipelines and summarization models.

Usage
Run the AI agent:

bash
Copy code
python ai_agent.py
You will see an interactive menu:

Sentiment Analysis: Input text to get its sentiment (Positive, Negative, Neutral).

Summarization: Input text to get a concise summary.

Exit: Close the program.

Example
vbnet
Copy code
=== AI Agent using Hugging Face ===
1. Sentiment Analysis
2. Summarization
0. Exit

Enter your choice: 1
Enter text for sentiment analysis: I love using Python!
Sentiment: POSITIVE | Score: 0.99
