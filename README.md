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

## Discovery e documentação arquitetural

Como parte desta atividade, foi realizado um discovery técnico com apoio de GenAI e da abordagem **Diagrams as Code**. A análise foi baseada exclusivamente no código e na documentação existentes no repositório, e os artefatos foram mantidos em formato versionável.

- [Documento de discovery](docs/discovery.md)
- [Diagrama estrutural](docs/architecture-container.mmd)
- [Diagrama comportamental de criação de tarefa](docs/sequence-create-task.mmd)

Os diagramas são versionados junto ao código, permitindo acompanhar a evolução da arquitetura e comparar a documentação com o comportamento implementado.

### Decisões e ajustes realizados sobre a saída da IA

- **Identificações corretas:** a IA reconheceu a API FastAPI, as camadas de serviço e repositório, o armazenamento em memória, o `PriorityAdvisor`, o fluxo de criação de tarefas e a integração opcional com a OpenAI.
- **Inferências válidas:** a divisão entre API, serviço, repositório e priorizador foi tratada como uma visão lógica inspirada em C4. O cliente foi representado como cliente HTTP, e o armazenamento foi separado visualmente para facilitar a leitura, embora seja um dicionário interno do repositório.
- **Pontos corrigidos:** a geração do UUID, do status inicial e dos timestamps foi atribuída ao `TaskRepository`; o fallback foi atribuído ao `PriorityAdvisor`; a condição real de execução local foi descrita como ausência de `OPENAI_API_KEY`, e não como uma decisão de que a heurística seria suficiente; respostas inválidas foram diferenciadas de falhas e timeouts externos; a validação de `TaskCreate` foi incluída no fluxo.
- **Informações desconhecidas:** permanecem indefinidos a topologia de deploy, os limites de volume e concorrência, as regras de transição de status, os requisitos de observabilidade, a estratégia de persistência futura e a política de autenticação e autorização.
- **Decisões ainda necessárias:** um futuro agente deverá receber definições sobre o contrato de campos, as regras de repriorização, o comportamento para valores nulos em atualizações, a configuração efetiva de timeout e ambiente, o modelo OpenAI suportado, o tratamento de exceções não previstas, a necessidade de logs e auditoria, os requisitos de persistência, segurança, escala e os perfis de acesso.

### Validação da documentação com GenAI

Após a criação da documentação, foi realizado um teste utilizando somente os documentos produzidos e documentos existentes no repositório, sem consultar o código-fonte.

O teste consistiu em simular a implementação da funcionalidade de filtro de tarefas por status.

- **O que o agente conseguiu determinar com segurança:** a presença do requisito de filtro por status no escopo do MVP, o contexto de domínio das tarefas e a intenção de que a funcionalidade faz parte da API de consulta de tarefas.
- **O que ele precisaria inferir:** o contrato exato do endpoint, o nome e o tipo do parâmetro de consulta, os valores válidos de status, o comportamento do filtro quando nenhum valor é informado, a combinação com outros filtros e a forma de resposta esperada.
- **Decisões de implementação ausentes:** o contrato da API, as regras de validação do filtro, o comportamento exato de filtro por status, os cenários de erro e sucesso, e os critérios de teste para a funcionalidade.
- **Perguntas que precisariam ser feitas ao responsável pelo sistema:** qual é o nome do parâmetro de consulta, quais status existem no sistema, o filtro é case-sensitive, aceita múltiplos valores, combina com outros filtros e como deve se comportar quando o valor informado for inválido ou inexistente?
- **Principais riscos de um agente inventar decisões:** criar um contrato de API inconsistente com o sistema real, assumir regras de validação sem confirmação, definir filtros com semântica errada, e gerar testes que validam comportamento inexistente ou incompatível com a regra de negócio.

O teste demonstrou que a documentação reduziu a necessidade de inferências, mas ainda possui lacunas relacionadas principalmente ao contrato da API, regras de validação, comportamento de filtros e critérios de teste.

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
