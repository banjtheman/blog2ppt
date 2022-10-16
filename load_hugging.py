# Python imports
import os
os.environ['TRANSFORMERS_CACHE'] = '/tmp/' # Set tmp as transformers cache

# 3rd party imports
from transformers import pipeline

# Huggingface summarizer
summarizer = pipeline(
    "summarization", model="facebook/bart-large-cnn"
) 

print("All done")