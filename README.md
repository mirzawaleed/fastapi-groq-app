# FastAPI User Persona App

This app allows you to generate and search user personas using background information. It integrates with the Groq API for persona generation and stores results in a PostgreSQL database.

## Features

- Generate user personas via Groq AI based on background data.
- Prevent duplicate persona entries.
- Search stored personas by keyword.
- SQLAlchemy + Alembic migrations.
- Structured FastAPI project layout.

---

## 🧰 Requirements

- Python 3.10+
- PostgreSQL
- [Groq API Key](https://console.groq.com/)
- Poetry or pip (your choice)
- `virtualenv` or similar environment manager

---

## 🚀 Getting Started

### Clone and enter project
```bash
git clone https://github.com/mirzawaleed/fastapi-groq-app.git
cd fastapi-groq-app
```

### Create and activate venv
```bash
python -m venv .venv
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Create .env file with credentials
Manually create a .env file in your project root.

### Add DATABASE_URL and GROQ_API_KEY
```bash
DATABASE_URL=postgresql://your_username:your_password@localhost/db_name
GROQ_API_KEY=your_groq_api_key_here
```

### Init Alembic (if not already)
```bash
alembic init alembic
```

### Generate migration
```bash
alembic revision --autogenerate -m "init"
```

### Apply migration
```bash
alembic upgrade head
```

### Start app
```bash
uvicorn app.main:app --reload
```
