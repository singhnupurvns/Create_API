from fastapi import FastAPI ,Depends ,HTTPException,Header 
import os  
import ollama 
from dotenv import load_dotenv 
load_dotenv() 
API_KEYS_CREDITS = {os.getenv("API_KEY"):5}  

app = FastAPI() 
def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEYS_CREDITS.get(x_api_key,0)  
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key or insufficient credits") 
    return x_api_key 

@app.get("/generate") 
def generate(prompt: str,x_api_key: str = Depends(verify_api_key)):
    API_KEYS_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="gemma4:e2b",messages=[{"role": "user", "content": prompt}]) 
    return {"response": response["message"]["content"]} 
