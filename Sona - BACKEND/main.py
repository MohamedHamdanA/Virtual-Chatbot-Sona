from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama

app = FastAPI()

# Initialize Ollama client
client = ollama.Client()

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(prompt: Prompt):
    try:
        response = client.chat(
            model='llama3.1',
            messages=[{'role': 'user', 'content': "You will always reply with a JSON array curly brackets of messages without any special characters. With a maximum of 3 messages but not necessarily 3 messages everytime .Each message has a text, facialExpression, and animation property.The different facial expressions are: smile, sad, angry, surprised, funnyFace, and default.The different animations are: Talking_0, Talking_1, Talking_2, Crying, Laughing, Rumba, Idle, Terrified, and Angry."+prompt.prompt }]
        )
        return {"text": response['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
