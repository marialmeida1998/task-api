# Micro-API de Tarefas com Prioridade Assistida por IA

API em FastAPI para gestao de tarefas de uma equipe interna. A prioridade pode ser calculada por heuristica local e, opcionalmente, por LLM quando `OPENAI_API_KEY` estiver configurada.

## Objetivo

Fornecer um MVP enxuto para cadastro, consulta, atualizacao e remocao de tarefas, com uma arquitetura simples e evolutiva baseada em `API`, `Service`, `Repository` e `PriorityAdvisor`.

## Requisitos

- Python 3.11 ou superior
- `pip`
- Git

## Instalação

### 1. Verificar a versao do Python

```powershell
python --version
```

### 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

CMD:

```bat
.\.venv\Scripts\activate.bat
```

### 4. Instalar dependencias

```powershell
make install
```

Ou, sem `make`:

```powershell
pip install -r requirements.txt
```

### 5. Configurar variaveis opcionais

Copie o arquivo de exemplo e ajuste apenas o que for necessario:

```powershell
copy .env.example .env
```

Use `OPENAI_API_KEY` somente se quiser habilitar a integracao opcional com LLM.

## Execucao local

Inicie a API:

```powershell
make run
```

Ou diretamente:

```powershell
uvicorn app.main:app --reload
```

Endpoints principais:

- `GET /health`
- `POST /tasks`
- `GET /tasks`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

Documentacao interativa:

```text
http://127.0.0.1:8000/docs
```

## Testes

Execute a suite:

```powershell
make test
```

Ou diretamente:

```powershell
pytest
```

Cobertura atual:

- `PriorityAdvisor`
- `TaskService`
- Rotas CRUD de `/tasks`
- `GET /health`
- Cenarios de `404 Not Found`
- Cenarios de validacao `422`
- Fallback de priorizacao quando a chamada externa falha

## Arquitetura

O projeto segue uma separacao simples por camadas:

```text
app/
|-- api/
|   `-- task_routes.py
|-- models/
|   `-- task.py
|-- repositories/
|   `-- task_repository.py
|-- services/
|   |-- priority_advisor.py
|   `-- task_service.py
`-- main.py
```

### Fluxo

- `api`: expoe os endpoints HTTP e traduz erros em status code.
- `models`: define schemas Pydantic e enums de contrato.
- `repositories`: guarda a persistencia em memoria.
- `services`: concentra regras de negocio.
- `PriorityAdvisor`: decide a prioridade com heuristica local e fallback opcional a LLM.

## Uso de IA

O `PriorityAdvisor` segue esta ordem:

1. Aplica heuristica local.
2. Se `OPENAI_API_KEY` existir, tenta consultar a LLM com timeout.
3. Se a chamada falhar, expirar ou retornar algo invalido, usa o fallback local.

Comportamento por cenario:

- Sem `OPENAI_API_KEY`: nenhuma chamada externa e nenhum custo adicional.
- Com `OPENAI_API_KEY`: tenta uso opcional da LLM.
- Falha externa: a API continua funcionando com o resultado local.

Variaveis relacionadas:

```powershell
OPENAI_API_KEY=
OPENAI_MODEL=gpt-5.4-nano
OPENAI_TIMEOUT_SECONDS=3
```

Exemplo de resultado:

- Titulo com `incidente`, `urgente` ou `bloqueio` tende a virar `critica`.
- Titulo com `prazo`, `risco` ou `importante` tende a virar `alta`.
- Sem termos fortes, a prioridade informada pode ser mantida.

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

- [Escopo do MVP](docs/escopo-mvp.md)
- [Backlog do MVP](docs/backlog-mvp.md)
- [Diagrama de componentes](docs/diagrama-componentes.mmd)

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
