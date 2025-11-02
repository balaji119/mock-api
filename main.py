from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Service is running"}

@app.post("/api/orders")
async def create_order(request: Request):
    data = await request.json()
    print("📦 New order received:", data)
    return {
        "status": "success",
        "message": "Order received successfully",
        "data": data
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
