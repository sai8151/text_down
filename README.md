# Text Summarizer Web Application

This is a simple web application built using Flask that allows users to pdf and generate a ppt using Gensim's text summarization techniques.
<br>
Tested in linux 5.15.0-86-generic #96~20.04.1-Ubuntu SMP Thu Sep 21 13:23:37 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
## Prerequisites

Before running the application, ensure you have the following installed:

- Python
- Flask
- Gensim
- tempfile
- pptx
- pdfplumber
- gensim==3.6.0
- ignore re.txt

You can install Flask and Gensim using pip:

```bash
pip install Flask
pip install gensim
pip install tempfile
pip install pptx
pip install pdfplumber
pip install gensim==3.6.0
```

## Getting Started

Clone the repository to your local machine:

bash
Copy code

```bash
git clone https://github.com/sai8151/text_down
cd text_down
```

Run the Flask application:

bash
Copy code

```bash
python app.py
```

The application will be accessible at http://127.0.0.1:5000/ in your web browser.
change port to your desired one.

## Usage

Access the web application by opening a web browser and visiting http://127.0.0.1:5000/.

You will see a simple input form where you can paste or type the text you want to summarize.

Click the "Summarize" button.

The application will generate a summary of the provided text using Gensim's summarization techniques.

The summary will be displayed on the webpage.
