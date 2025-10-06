# AI Agent using Hugging Face Transformers

A lightweight AI agent built using Hugging Face Transformers for natural language processing tasks like **sentiment analysis** and **text summarization**. Run it directly from the terminal or Google Colab.

---

## Features

- **Sentiment Analysis:** Detects the sentiment of your input text (Positive, Negative, Neutral) and provides a confidence score.  
- **Text Summarization:** Summarizes long text inputs into concise summaries.  
- Simple and interactive terminal-based interface.  

---

## Requirements

- Python 3.8+  
- [Transformers](https://huggingface.co/docs/transformers/index) library  
- Optional: [Torch](https://pytorch.org/) for model backend  

Install dependencies using pip:

```bash
pip install -r requirements.txt
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/ai-huggingface-agent.git
cd ai-huggingface-agent
Run the AI agent:

bash
Copy code
python ai_agent.py
Follow the menu in the terminal:

markdown
Copy code
=== AI Agent using Hugging Face ===
1. Sentiment Analysis
2. Summarization
0. Exit
Enter your text and get instant results.

Example
Sentiment Analysis:

yaml
Copy code
Enter text for sentiment analysis: I love this product!
Sentiment: POSITIVE | Confidence: 99.5%
Summarization:

pgsql
Copy code
Enter text for summarization: <paste long text here>
Summary: <generated summary>
Notes
Ensure your text isn’t too long for the summarization model; extremely long text may need to be chunked.

You can use this script in Google Colab for easier GPU acceleration.
