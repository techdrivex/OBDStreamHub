import asyncio
from fastapi import FastAPI, WebSocket
from obd_handler import OBDHandler
import json

app = FastAPI(title="OBDStreamHub")

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)

# Initialize OBD handler
obd_handler = OBDHandler(config)

@app.get("/")
async def root():
    return {"message": "OBDStreamHub - Live OBD Streaming"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Fetch live OBD data
            data = obd_handler.get_live_data()
            # Send data to connected WebSocket clients
            await websocket.send_json(data)
            await asyncio.sleep(1)  # Stream every 1 second (adjust as needed)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)