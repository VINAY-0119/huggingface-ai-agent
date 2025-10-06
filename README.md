AI Agent using Hugging Face Transformers

A lightweight AI agent built with Hugging Face Transformers for natural language processing tasks such as sentiment analysis and text summarization. Designed for ease of use, it runs directly from the terminal or in Google Colab.

Features

Sentiment Analysis – Detects whether text is Positive, Negative, or Neutral, along with a confidence score.

Text Summarization – Condenses long texts into concise summaries.

Interactive Interface – Simple menu-driven terminal interaction.

Requirements

Python 3.8 or higher

Transformers
 library

Optional: PyTorch
 for model backend

Install dependencies:

pip install -r requirements.txt

Usage

Clone the repository:

git clone https://github.com/your-username/ai-huggingface-agent.git
cd ai-huggingface-agent


Run the AI agent:

python ai_agent.py


Follow the terminal menu:

=== AI Agent using Hugging Face ===
1. Sentiment Analysis
2. Summarization
0. Exit


Input your text and view instant results.

Example

Sentiment Analysis:

Enter text for sentiment analysis: I love this product!
Sentiment: POSITIVE | Confidence: 99.5%


Text Summarization:

Enter text for summarization: <paste long text here>
Summary: <generated summary>

Notes

Extremely long text may need to be chunked for summarization.

Google Colab can be used to leverage GPU acceleration for faster processing.

Repository Structure
ai-huggingface-agent/
│
├── ai_agent.py          # Main AI agent script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
