from fastapi import FastAPI 
from database import factory  
from models import Tarefa

 
app = FastAPI()

tarefas = [
    {"id": 1, "descricao": "Estudar FastAPI", "concluida": False},
    {"id": 2, "descricao": "Fazer exercícios", "concluida": False}
]

@app.get("/")
def root():
    return {"mensagem": "API de Tarefas funcionando!"}

@app.get("/tarefas")
def listar_tarefas():
    session = factory()
    tarefas_banco = session.query(Tarefa).all()
    return tarefas_banco

@app.put('/tarefas/{task_id}')
def atualizar_tarefa(task_id: int):
    session = factory()
    tarefa = session.query(Tarefa).filter(Tarefa.id == task_id).first()
    if tarefa:
        tarefa.concluida = True
        session.commit()
        return {'mensagem': 'Tarefa concluida'}

@app.post("/tarefas")
def adicionar (descricao: str):
    tarefa_nova = Tarefa(descricao = descricao, concluida = False)
    session = factory()
    session.add(tarefa_nova)
    session.commit()
    return {"mensagem": "Tarefa adicionada"}

@app.delete("/tarefas/{task_id}")
def apagar (task_id: int):
    session = factory()
    tarefa = session.query(Tarefa).filter(Tarefa.id == task_id).first()
    if tarefa:
        session.delete(tarefa)
        session.commit()
        return {"mensagem": "Deletado"}
    else:
        return {"mensagem": "Não encontrado"}