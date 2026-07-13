from fastapi import FastAPI 

from database import engine
 
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
    return tarefas

@app.put('/tarefas/{task_id}')
def atualizar_tarefa(task_id: int):
    for task in tarefas:
        if task['id'] == task_id:
            task['concluida'] = True
            return {'mensagem': f'Tarefa {task_id} Atualizada!'}

@app.post("/tarefas")
def adicionar (descricao: str):
    id_maior = 0
    for task in tarefas:
       if task['id'] > id_maior:
            id_maior = task["id"]

    novo_id = id_maior + 1

    tarefa_nova = {
        "id": novo_id,
        "descricao": 'Estudar Python',
        "conluida": False
    }

    tarefas.append(tarefa_nova)
    return {"mensagem": "Tarefa adicionada"}

@app.delete("/tarefas/{task_id}")
def apagar (task_id: int):
    tarefa_encontrada = None
    for task in tarefas:
        if task["id"] == task_id:
            tarefa_encontrada = task

    if tarefa_encontrada:
        tarefas.remove(tarefa_encontrada)
        return{'mensagem': "Tarefa removida"}
    
    else:
        return{"mensagem": "Tarefa nao encontrada, verifique o id"}