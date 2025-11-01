# 📄 PDF CHATBOT

> Ask questions about any PDF effortlessly using this.


## Features

* 📂 Upload any PDF file.
* ❓ Ask questions and get answers based on PDF content.
* ⚡ Fast, context-aware responses using **LangChain**.
* 📚 Handles large PDFs by intelligently splitting text into chunks.

---

## 🚀 Installation

```bash
git clone https://github.com/immanuel-krish11/PDF-chatbot.git
cd pdf-qa
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate 
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage

1. Run the app:

   ```bash
   python app.py
   ```
2. Upload your PDF file through the interface.
3. Ask any questions about your PDF.
4. Receive accurate, context-aware answers.

---

## 🧠 How It Works

1. The PDF is **parsed and split** into manageable text chunks.
2. LangChain **indexes the content** for easy querying.
3. When you ask a question, the model **retrieves relevant chunks** and generates an answer.

---

## Here's a demo of this - 
I've used the pdf - Hands-On Machine Learning with Scikit-Learn & TensorFlow book

<img width="1464" height="823" alt="Screenshot 2025-11-01 at 10 55 35 PM" src="https://github.com/user-attachments/assets/03c1bc43-78d5-4b4f-a565-7e82289f3538" />



<img width="1417" height="799" alt="Screenshot 2025-11-01 at 11 11 02 PM" src="https://github.com/user-attachments/assets/5f079d96-bc09-4276-bf47-707478ebd659" />
After Uploading...


<img width="1469" height="837" alt="Screenshot 2025-11-01 at 11 13 30 PM" src="https://github.com/user-attachments/assets/46aa2fcf-8092-467e-82b5-d8640b72443b" />
Screenshot of the chat...
