# 🎤 AI Mock Interviewer

An AI-powered web application that simulates real interview scenarios by asking role-based questions and evaluating user responses in real time.

---

## 🚀 Features

- 🎯 Role-based interview (Frontend Developer, Data Analyst, ML Engineer)
- 📊 Difficulty selection (Easy, Medium, Hard)
- 🤖 AI-generated interview questions
- 💬 Chat-style interaction (AI vs User)
- 📈 Answer evaluation after interview
- 🧠 Feedback with suggestions for improvement
- 🔄 Restart interview option

---

## 🛠️ Tech Stack

- Python
- Streamlit (Frontend UI)
- OpenRouter API (AI Model)
- Requests
- Python-dotenv

---

## 📂 Project Structure

```
mock-interviewer/
│
├── app.py              # Main application (UI & flow)
├── interviewer.py      # Generates interview questions
├── evaluator.py        # Evaluates answers
├── requirements.txt    # Dependencies
├── .gitignore          # Protects sensitive files
└── README.md           # Project documentation
```

---

## ▶️ How to Run Locally

1. Clone the repository:
```
git clone https://github.com/Archisahu27/mock-interviewer.git
```

2. Navigate to the project:
```
cd mock-interviewer
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Create a `.env` file and add your API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

5. Run the application:
```
streamlit run app.py
```

---

## 📌 Limitations

- AI evaluation may not always be perfectly accurate
- Requires internet connection for API calls

---

## 👨‍💻 Author

Archi Sahu

---

## ⭐ If you found this project useful, consider giving it a star!