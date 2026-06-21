# Gemini Image Extraction App

A simple Streamlit-based web application that uses Google's Gemini AI multi-model to extract and analyze information from images.

---

## 🚀 Features

* Upload images (JPG, JPEG, PNG)
* Ask questions about the image
* Get response

---



## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API (`google-genai`)
* Pillow (PIL)
* python-dotenv

---

## Screenshot

![alt text](<Screenshot 2026-06-21 180806.png>)

![alt text](<Screenshot 2026-06-21 180742.png>)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-image-app.git
cd gemini-image-app
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

Get your API key from:
https://aistudio.google.com/apikey

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---


## 📌 Future Improvements

* Add PDF support
* Add chat history
* Export extracted results
* Multi-image support

---

## 👨‍💻 Author

Mohd Maaz
Built as a mini project using Google Gemini API and Streamlit.
