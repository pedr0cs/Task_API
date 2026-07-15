# Task API 🚀

## Descrição
API REST para gerenciamento de tarefas, construída com FastAPI e Python. Um projeto de estudos para aprender desenvolvimento backend com banco de dados.

**Status:** Em desenvolvimento ⚙️

## Funcionalidades
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Persistência de dados com SQLite
- ✅ API REST com documentação automática
- ✅ Tarefas com status de conclusão

## Tecnologias
- Python 3.14
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Git

## Como Rodar:

### 1. Clone o repositório
```bash
git clone https://github.com/pedr0cs/Task_API.git
cd task_api
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
# No Windows:
.\\venv\\Scripts\\Activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Rode o servidor
```bash
uvicorn main:app --reload
```

## Documentação
Acesse http://localhost:8000/docs para ver a documentação interativa (Swagger)

## Endpoints
- `GET /tarefas` - Lista todas as tarefas
- `POST /tarefas?descricao=...` - Cria uma nova tarefa
- `PUT /tarefas/{id}` - Marca tarefa como concluída
- `DELETE /tarefas/{id}` - Deleta uma tarefa

## Roadmap (Em breve)
- [ ] Testes com Pytest
- [ ] Deploy
- [ ] Validação de dados com Pydantic
- [ ] Autenticação

## Autor
Pedro