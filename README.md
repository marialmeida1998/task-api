# Micro-API de Tarefas com Prioridade Assistida por IA

API em FastAPI para gestao de tarefas de uma equipe interna, com priorizacao assistida por heuristica local e suporte opcional a LLM quando `OPENAI_API_KEY` estiver configurada.

## Objetivo

Fornecer um MVP enxuto para cadastro, consulta, atualizacao e remocao de tarefas, mantendo uma arquitetura simples e evolutiva com separacao entre API, Service, Repository e componente de priorizacao.

## Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- HTTPX
- Git

## Instalacao

Clone ou acesse o diretorio do projeto:

```powershell
cd C:\LABORATÓRIO-PROJETO
```

Crie o ambiente virtual, se ainda nao existir:

```powershell
python -m venv .venv
```

Ative o ambiente virtual no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependencias:

```powershell
pip install -r requirements.txt
```

## Execucao local

Inicie a API com reload:

```powershell
uvicorn app.main:app --reload
```

Acesse a documentacao interativa:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
GET http://127.0.0.1:8000/health
```

## Testes

Execute a suite completa:

```powershell
pytest
```

Ou usando explicitamente o Python do ambiente virtual:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Cobertura atual da suite:

- `PriorityAdvisor`
- `TaskService`
- Rotas CRUD de `/tasks`
- Cenarios de sucesso
- Cenarios de `404 Not Found`
- Fallback de priorizacao quando chamada externa falha

## Arquitetura

O projeto segue uma separacao simples por camadas:

```text
app/
├── api/
│   └── task_routes.py
├── models/
│   └── task.py
├── repositories/
│   └── task_repository.py
├── services/
│   ├── priority_advisor.py
│   └── task_service.py
└── main.py
```

### Camadas

- `api`: define os endpoints HTTP, status codes e tratamento de erros.
- `models`: define schemas Pydantic, enums e contratos de entrada/saida.
- `repositories`: concentra a persistencia em memoria.
- `services`: concentra regras de negocio e integracao com priorizacao.
- `PriorityAdvisor`: sugere prioridade por heuristica local e usa LLM opcionalmente.

## Priorizacao assistida

A prioridade da tarefa pode ser sugerida automaticamente pelo `PriorityAdvisor`.

Comportamento padrao:

- Sem `OPENAI_API_KEY`: usa apenas heuristica local, sem custo externo.
- Com `OPENAI_API_KEY`: tenta chamada a LLM com timeout.
- Em caso de erro, timeout ou resposta invalida: usa fallback local obrigatorio.

Variaveis de ambiente opcionais:

```powershell
$env:OPENAI_API_KEY="sua-chave"
$env:OPENAI_MODEL="gpt-5.4-nano"
```

## Uso da API

### Criar tarefa

```http
POST /tasks
Content-Type: application/json
```

```json
{
  "title": "Corrigir incidente urgente",
  "description": "Bloqueio no fluxo interno",
  "priority": "media",
  "assignee": "Equipe API"
}
```

Resposta esperada:

```http
201 Created
```

```json
{
  "id": "uuid",
  "title": "Corrigir incidente urgente",
  "description": "Bloqueio no fluxo interno",
  "status": "pendente",
  "priority": "critica",
  "assignee": "Equipe API",
  "created_at": "2026-05-01T00:00:00Z",
  "updated_at": "2026-05-01T00:00:00Z"
}
```

### Listar tarefas

```http
GET /tasks
```

Resposta esperada:

```http
200 OK
```

### Consultar tarefa por ID

```http
GET /tasks/{task_id}
```

Resposta esperada para tarefa existente:

```http
200 OK
```

Resposta esperada para tarefa inexistente:

```http
404 Not Found
```

### Atualizar tarefa

```http
PUT /tasks/{task_id}
Content-Type: application/json
```

```json
{
  "title": "Corrigir incidente urgente",
  "status": "em_andamento",
  "priority": "alta",
  "assignee": "Equipe Plataforma"
}
```

Resposta esperada:

```http
200 OK
```

### Remover tarefa

```http
DELETE /tasks/{task_id}
```

Resposta esperada para tarefa existente:

```http
204 No Content
```

Resposta esperada para tarefa inexistente:

```http
404 Not Found
```

## Valores aceitos

### Status

- `pendente`
- `em_andamento`
- `concluida`
- `cancelada`

### Prioridade

- `baixa`
- `media`
- `alta`
- `critica`

## Documentacao do projeto

Arquivos complementares:

- `docs/escopo-mvp.md`
- `docs/backlog-mvp.md`
- `docs/diagrama-componentes.mmd`

## Limitacoes

- Persistencia em memoria: os dados sao perdidos ao reiniciar a aplicacao.
- Nao ha autenticacao ou autorizacao.
- Nao ha banco de dados.
- Nao ha paginacao ou filtros avancados.
- Nao ha deploy configurado.
- A integracao com LLM e opcional e possui fallback local obrigatorio.
- A heuristica local e simples e baseada em termos no titulo e descricao.
- O uso de LLM depende de chave valida em `OPENAI_API_KEY`.

## Roadmap

- Adicionar persistencia com banco de dados.
- Separar configuracao por ambiente.
- Adicionar autenticacao para uso interno.
- Adicionar filtros por status, prioridade e responsavel.
- Melhorar observabilidade com logs estruturados.
- Evoluir o `PriorityAdvisor` com criterios configuraveis.
- Preparar deploy da API.
