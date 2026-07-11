from fastapi import FastAPI 

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