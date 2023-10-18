from flask import Flask, render_template, request
from flask import Flask, request, render_template
from gensim.summarization import summarize

# path in server is /home/u900843168/.local/bin/
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['text']
    summary = summarize(text)
    return render_template('summary.html', summary=summary, original_text=text)

if __name__ == '__main__':
    app.run(debug=True)
