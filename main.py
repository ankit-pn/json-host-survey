import json
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# Load data from x.json
with open('x.json', 'r') as file:
    appointment_data = json.load(file)

@app.get("/{time}")
async def get_appointments(time: str) -> List[Dict[str, str]]:
    if time in appointment_data:
        return appointment_data[time]
    else:
        return []

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)