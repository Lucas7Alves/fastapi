from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
database = []

class Events(BaseModel):
    nome: str
    dono: str
    desc: str
    data: str
    
@app.post('/event', response_model=Events)
async def criar_events(event: Events):
        database.append(event)
        
        return event
    
@app.get('/event')
async def ler_events() -> List[Event]:
    return database