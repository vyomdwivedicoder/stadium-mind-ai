# 🧠 StadiumMind AI

AI-powered Smart Stadium Operations Platform for FIFA World Cup 2026.

## Features

- Live Incident Dashboard
- AI Command Center
- Rule Engine
- Real-time WebSocket Updates
- Groq AI Integration
- Incident Decision Engine

## Tech Stack

Frontend
- React
- TypeScript
- Vite

Backend
- FastAPI
- WebSockets
- Groq API

## Run

Backend

```bash
pip install -r requirements.txt

uvicorn main:app --reload
```

Frontend

```bash
npm install

npm run dev
```

Create a `.env`

```
GROQ_API_KEY=your_key
```