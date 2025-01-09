import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
from heapq import nlargest
import spacy

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load SpaCy language model
nlp = spacy.load('en_core_web_sm')

text = "Hello world! This is a test to verify NLTK setup."
print(sent_tokenize(text))

# Function to summarize text
def summarize_text(text, summary_ratio=0.3):
    # Tokenize the text into words and sentences
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Load stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    punctuation_set = set(punctuation + '\n')

    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word.isalnum() and word not in stop_words and word not in punctuation_set:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Normalize word frequencies
    max_freq = max(word_frequencies.values(), default=1)
    word_frequencies = {word: freq / max_freq for word, freq in word_frequencies.items()}

    # Score sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Select top sentences for the summary
    summary_length = int(len(sentences) * summary_ratio)
    summary_sentences = nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# Streamlit app layout
st.title("English Text Summarizer")
st.write("Paste your text below ⬇️")

# Text input
text_input = st.text_area("Enter Text to Summarize", height=300)

# Slider for summary ratio
summary_ratio = st.slider("Summary Ratio (0.1 = very short, 0.5 = longer)", 0.1, 0.5, 0.3, step=0.1)

# Summarize button
if st.button("Summarize"):
    if len(text_input.strip()) == 0:
        st.warning("Please enter some text to summarize!")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_input, summary_ratio)
        st.success("Summary:")
        st.write(summary)


