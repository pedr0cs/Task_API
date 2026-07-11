from fastapi import FastAPI 

app = FastAPI()
@app.get("/")
def funcao():
    return{"mensagem": "API funcionando"}

