from fastapi import FastAPI
from datetime import datetime
from fastapi import HTTPException


app = FastAPI(root_path="/api/v1")

data = [
    {
        "campaign_id": 1, 
        "name": "Summer Launch", 
        "due_date": datetime.now(), 
        "created_at": datetime.now()
    }, 
    {
        "campaign_id": 2, 
        "name": "Black Friday", 
        "due_date": datetime.now(), 
        "created_at": datetime.now()
    }, 
    {
        "campaign_id": 3, 
        "name": "Pao House", 
        "due_date": datetime.now(), 
        "created_at": datetime.now()
    }
]




@app.get("/")
async def root(): 
    return {"message": "Hello workd!"}

@app.get("/campaigns")
async def read_campaigns(): 
    return {"campaigns": data}

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data: 
        if campaign.get("campaign_id") == id: 
            return {"campaign": campaign}
        raise HTTPException(status_code=404)
