# 🤖 AI Agent Journey — Task Tracker

> Built from scratch in 3 days as part of my journey to become an AI Engineer.

---

## 📌 What This Is

A natural language task tracker powered by real AI. Instead of picking numbers from a menu, you just type what you want in plain English and the AI understands you.

```
You: add buy groceries high priority
You: show me my tasks
You: I finished learning python
You: delete replying
You: quit
```

---

## 🚀 How It Works

```
User types → Groq AI reads it → returns a command → Python executes the action
```

The AI acts as the brain — it reads what you type and decides whether you want to ADD, VIEW, COMPLETE, DELETE, or QUIT. The Python code then handles the action.

---

## ✨ Features

- ✅ Add tasks with priority (High / Medium / Low)
- ✅ View all tasks with progress summary
- ✅ Complete a task
- ✅ Delete a task
- ✅ Tasks saved to `tasks.json` — persists between sessions
- ✅ Natural language input powered by Groq AI (LLaMA 3.1)

---

## 🗓️ Day by Day Progress

### Day 1 — Python Basics + First Agent
- Learned: variables, lists, dictionaries, loops, JSON, user input
- Built: basic task tracker with menu (add, view, complete, delete, save to file)

### Day 2 — Leveling Up
- Learned: list of dictionaries, remove(), del, try/except
- Built: added priority system, progress tracker, delete feature

### Day 3 — Adding Real AI
- Learned: Groq API, prompt engineering, connecting AI to Python code
- Built: replaced menu with natural language AI understanding

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Groq API | AI understanding (LLaMA 3.1 8B) |
| JSON | Task storage |

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/ai-agent-journey
cd ai-agent-journey
```

**2. Install dependencies**
```bash
pip install groq
```

**3. Add your Groq API key**

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Or add it directly in the code (not recommended for production).

**4. Run the agent**
```bash
python day3taskagent.py
```

---

## 📁 File Structure

```
ai-agent-journey/
├── day1tasktracker.py   # Day 1 & 2 — menu based task tracker
├── day3taskagent.py     # Day 3 — AI powered task tracker
├── tasks.json           # Auto-generated task storage
├── .env                 # API key (never push to GitHub)
├── .gitignore           # Excludes .env and sensitive files
└── README.md            # This file
```

---

## 🔒 Important

Never push your API key to GitHub. Add a `.gitignore` file with:
```
.env
tasks.json
```

---

## 🗺️ What's Next

- [ ] Day 4 — AI extracts task name and priority from natural language (no follow-up questions)
- [ ] Day 5 — Add memory so AI remembers context across messages
- [ ] Month 2 — LangChain integration
- [ ] Month 3 — Deploy online

---

## 👩‍💻 About

**Maisha Rahman Chowdhury** — documenting my journey to become an AI Engineer, one day at a time.

> "Built from scratch. Bugs and all."
