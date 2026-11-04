from fastapi import FastAPI
app = FastAPI(title="Learning Platform API")
@app.get("/health")
def health():
    return {"status": "ok", "service": "python-api"}
@app.get("/lessons")
def lessons():
    return [{"title": "Container builds"}, {"title": "Release promotion"}]
