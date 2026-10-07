# VeriData: Proof-Carrying Data Analyst Backend
> **Hackathon Track:** HNX26PSI08 (Agentic GenAI · Data Analytics · Code Generation · Verification)

An agentic data analytics backend that produces **mathematically verifiable proofs** for every claimed metric. If the code does not execute or produces a different answer, the system fails. If data is corrupt or queries are ambiguous, the agent delivers **principled refusals**.

---

## 🚀 Quickstart

### 1. Run the Server
```bash
python run.py
```
Or directly with uvicorn:
```bash
uvicorn app.main:app --reload --port 8000
```

### 2. Interactive API Documentation
Open your browser at:
* **SWAGGER UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **MODEL:**[ [http://localhost:8000/redoc](http://localhost:8000/redoc)](http://localhost:8000/)

---

## 🏛️ Core Architecture

```
[User Query + Dataset Name]
             │
             ▼
  ┌───────────────────────┐
  │  Stage 1: Gatekeeper  │ ──► Unanswerable / Corrupted?
  └───────────────────────┘     └─► Immediate REFUSAL with Rationale
             │ Clear & Feasible
             ▼
  ┌───────────────────────┐
  │ Stage 2: Code Gen     │ ──► Pure Vectorized Pandas Script
  └───────────────────────┘
             │
             ▼
  ┌───────────────────────┐
  │   Stage 3: Sandbox    │ ──► AST Import Inspection (Blocks os/sys)
  │      Execution        │ ──► 5-Second Subprocess Timeout
  └───────────────────────┘ ──► Reflection Loop (Traceback Auto-Fix)
             │
             ▼
     [Proof-Carrying Result: Answer + Verified Code Output]
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/analyze` | Main Agent endpoint: runs Gatekeeper $\to$ CodeGen $\to$ Sandbox $\to$ Verification |
| `POST` | `/api/verify` | Standalone judge verifier: executes arbitrary Python code and returns output & audit |
| `GET` | `/api/datasets` | Lists all datasets available in `data/` |
| `GET` | `/api/datasets/{name}/schema` | In-depth dataset profiling (dtypes, nulls, unique values, head 3) |
| `POST` | `/api/datasets/upload` | Upload a new `.csv` dataset |

---

## 🧪 Benchmark Datasets Included

1. **`sales_clean.csv`**: Baseline clean multi-category sales records.
2. **`sales_dirty_traps.csv`**: Contains duplicate IDs, currency strings (`$`, `€`), missing values.
3. **`sales_adversarial.csv`**: Date bounds capped at 2023, missing cost columns (triggers principled refusal).

---

## 🛡️ Sandbox Security
* **AST Parsing**: Disallows `os`, `sys`, `subprocess`, `socket`, `eval`, `exec`.
* **Execution Timeout**: 5.0 seconds maximum execution time.
* **Vectorization Constraint**: Enforces vectorized Pandas operations, preventing slow `for` loops.
