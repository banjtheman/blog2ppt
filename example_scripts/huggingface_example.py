from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """
I used Python to develop the business logic needed for GitGallery and used the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework to encode the API endpoints. The 4 major endpoints needed for the application are login, verify, mint, and get items.
"""
print(summarizer(ARTICLE, max_length=150, min_length=30, do_sample=False))
