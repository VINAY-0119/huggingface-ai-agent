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
    print("AI Agent using Hugging Face")
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
