# 🎓 Schul AI Monorepo

This monorepo powers a full-stack AI-enabled educational platform using:

- 🧑‍🎨 **Frontend**: Angular (with Server-Side Rendering)
- 🧠 **Backend**: NestJS (REST APIs)
- 🤖 **AI Service**: FastAPI (Python) for ML/AI integrations

---

## 📁 Project Structure

```
schul-ai-workspace/
├── apps/
│   ├── frontend/       # Angular SSR app
│   ├── backend/        # NestJS API
│   └── ai-service/     # FastAPI-based AI service
├── libs/               # Shared libraries (optional)
├── nx.json             # Nx workspace config
├── package.json        # Root scripts
└── README.md
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Set up Python Virtual Environment (once)

```bash
cd apps/ai-service
python3 -m venv .schul_ai_env
source .schul_ai_env/bin/activate
pip install -r requirements.txt
```

> 💡 Run `pip freeze > requirements.txt` after adding new packages.

---

## 🧪 Run All Services

From the root of the monorepo:

```bash
npm run start:all
```

This will:
- Serve Angular at `http://localhost:4200`
- Serve NestJS at `http://localhost:3000/api`
- Serve AI API at `http://localhost:8000`

---

## 🔍 Individual Scripts

| Task             | Command                |
|------------------|------------------------|
| Frontend         | `npm run start:frontend` |
| Backend (NestJS) | `npm run start:backend`  |
| AI Service       | `npm run start:ai`       |

---

## 📡 API Endpoints

### ✅ FastAPI (AI Service)

| Method | Endpoint        | Description         |
|--------|------------------|---------------------|
| GET    | `/`             | Health check        |
| GET    | `/predict`      | Dummy AI prediction |

---

## ⚙️ Built With

- [Nx](https://nx.dev/)
- [Angular](https://angular.io/)
- [NestJS](https://nestjs.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

---

## 🧠 Contributors

- 

---

## 📌 Notes

- Remember to activate your virtualenv before starting the AI service manually.
- SSR is enabled for Angular by default.
- All services are run concurrently using `concurrently`.

---

## 📫 Contact

