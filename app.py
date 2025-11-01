from flask import Flask, render_template, request, jsonify
from modules.pdf_loader import extract_text_from_pdf
from modules.vector_store import create_chunks, create_embeddings, build_vector_store
from modules.chat_engine import create_qa_chain 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
qa_chain = None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods = ['POST'])
def upload_pdf():
    global qa_chain
    file = request.files['pdf']
    path = f"./uploads/{file.filename}" # saving the uploaded pdf in uploads file
    file.save(path)
    text = extract_text_from_pdf(path) # calling the pdf_loader.py
    chunks = create_chunks(text)
    vector_store = build_vector_store(chunks)
    qa_chain = create_qa_chain(vector_store)
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    global qa_chain
    question = request.json['question']
    # answer = qa_chain.invoke({"input": question})
    answer = qa_chain(question) 
    print(answer)
    return jsonify({'answer': answer.get('answer')})


if __name__ == '__main__':
    app.run(debug=True)