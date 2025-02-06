import requests, os
from dotenv import load_dotenv

load_dotenv()

# For Text Extraction:
url = "https://llmwhisperer-api.unstract.com/v1/whisper"
headers = {
    "Content-Type": "application/octet-stream",
    "unstract-key": f"{os.getenv('UNSTRACT_API_KEY')}" # Primary Key
}

params = {
    "force_text_processing": "true",
    "processing_mode": "text",
    "output_mode": "line-printer",
    "store_metadata_for_highlighting": "true" # Enabling for Highlighting the 'search term'
}

with open("sample_doc.pdf", "rb") as file: # Open the PDF file in binary mode
    response = requests.post(url, headers=headers, params=params, data=file)
    whis_hash = response.headers['whisper-hash']
print(response.text) # Printing the extracted texts!


# Highlighting the text with some metadetails:
url = "https://llmwhisperer-api.unstract.com/v1/highlight-data"
headers = {
    "Content-Type": "text/plain",
    "unstract-key": f"{os.getenv('UNSTRACT_API_KEY')}" # Primary Key
}

params = {
    "whisper-hash": whis_hash
}

data = "deposito"  # The search term

response = requests.post(url, headers=headers, params=params, data=data)
print(response.json()) # Printing the searched term metadetails!