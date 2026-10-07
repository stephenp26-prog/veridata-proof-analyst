import uvicorn
from app.config import settings

def main():
    print("=" * 65)
    print("  VERIDATA: Proof-Carrying Data Analyst Backend")
    print(f"  Version: {settings.VERSION}")
    print(f"  LLM Provider Mode: {settings.LLM_PROVIDER}")
    print(f"  Data Directory: {settings.DATA_DIR}")
    print(f"  Interactive Docs (Swagger): http://localhost:8000/docs")
    print(f"  Alternative Docs (ReDoc):   http://localhost:8000/redoc")
    print("=" * 65)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
