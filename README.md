# English Text Summarizer App

## Project Overview

This project is a simple text summarizer built using Python and Streamlit. It allows users to input English text, specify the desired summary length, and receive a concise summary generated using natural language processing techniques.

## Features

**Text Summarization:**
- The app analyzes the input text and generates a summary based on word frequencies.
- Users can adjust the summary length using an intuitive slider.

**Natural Language Processing:**
- Tokenizes text into sentences and words for better analysis.
- Removes common stopwords and punctuation to focus on meaningful words.
- Scores sentences based on the significance of their words to determine their importance.

**Interactive User Interface:**
- Built with Streamlit for a clean and user-friendly experience.
- Includes input fields, sliders, and real-time summarization output.

## Technologies Used

- **Languages**: Python
- **Libraries**:
    - **NLTK** for tokenization, stopword removal, and word frequency analysis.
    - **Streamlit** For building an interactive web application to visualize data and make predictions
    - **SpaCy** for efficient NLP operations.

## Installation

To set up the environment and run the project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/jamleston/summary-app
cd summary-app
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
streamlit run app.py
```

## Usage

- Enter the text you want to summarize in the provided text area.
- Adjust the slider to control the summary length (from 10% to 50% of the original text).
- Click the "Summarize" button to generate and view the summary.

## Repository Structure

```
├── app.py                   # Streamlit application for text summarization
├── nltk-summarizer.ipynb    # Initial Jupyter Notebook attempt for text summarization
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

## Developed by
- [Valeriia Alieksieienko](https://github.com/jamleston)