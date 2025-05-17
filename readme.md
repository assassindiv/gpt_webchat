# 🧠 Chat with Groq - Flask Web App

This is a simple Flask web application that allows users to chat with a powerful LLM (LLaMA 3) using the [Groq API](https://console.groq.com/). Messages are exchanged via a web interface and handled on the backend using Python and Flask.

## 🚀 Features

- Chat interface powered by LLaMA 3 via Groq
- Memory of chat history during a session
- Clean, minimal HTML interface
- Easy to run locally

## 🛠️ Technologies Used

- Python 3.x
- Flask
- Groq Python SDK
- HTML (Jinja2 templates)

## 📂 Project Structure

```
chat-with-groq/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## 🔑 Prerequisites

- Python 3.8+
- A Groq API key (get one at https://console.groq.com/)

## ⚙️ Setup Instructions

1. **Clone this repository**:

```bash
git clone https://github.com/your-username/chat-with-groq.git
cd chat-with-groq
```

2. **Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set your API key (recommended via `.env` file)**

Create a `.env` file in the root directory:

```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

Or directly in the code (not recommended for production):

```python
from groq import Groq
client = Groq(api_key="your_api_key_here")
```

5. **Run the application**:

```bash
python app.py
```

6. **Open in browser**:

```
http://127.0.0.1:5000/
```

## 📝 Example `.env` file

```
GROQ_API_KEY=gsk_your_real_api_key
```

## 📦 Example `requirements.txt`

```
Flask
groq
python-dotenv
```

## 💡 Future Improvements

- Add user authentication
- Save chat history to a database
- Stream typing responses (real-time updates)
- Add modern UI with TailwindCSS or Bootstrap

## 🤝 Contributing

Feel free to fork this repo and open a pull request to suggest improvements!

## 📄 License

MIT License