# Micro-API de Gestao de Tarefas com Priorizacao por IA

MVP de uma API para cadastro, consulta e organizacao de tarefas, com suporte futuro a priorizacao assistida por inteligencia artificial.

## Objetivo

Criar uma micro-API simples, extensivel e bem estruturada para gerenciar tarefas de produto ou operacao, permitindo evoluir gradualmente para recursos inteligentes de priorizacao, recomendacao e automacao.

O MVP deve permitir:

- Criar tarefas
- Listar tarefas
- Consultar tarefas por ID
- Atualizar tarefas
- Remover tarefas
- Preparar a base para priorizacao assistida por IA

## Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Ambiente virtual com `.venv`
- Git para versionamento

Dependencias futuras previstas:

- SQLAlchemy ou SQLModel
- Alembic
- PostgreSQL ou SQLite
- Integracao com API de IA
- Pytest

## Como rodar localmente

### 1. Acessar o projeto

```powershell
cd C:\LABORATORIO-PROJETO
```

### 2. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Windows CMD:

```bat
.\.venv\Scripts\activate.bat
```

### 3. Instalar dependencias

Quando o arquivo `requirements.txt` estiver disponivel:

```powershell
pip install -r requirements.txt
```

Ou, durante o desenvolvimento inicial:

```powershell
pip install fastapi uvicorn
```

### 4. Rodar a API

```powershell
uvicorn app.main:app --reload
```

### 5. Acessar a documentacao interativa

Depois que o servidor estiver ativo, acesse:

```text
http://127.0.0.1:8000/docs
```

## Estrutura prevista

```text
.
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── routes/
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Roadmap de releases

### Release 0.1.0 - Base da API

- Criar estrutura inicial do projeto
- Configurar FastAPI
- Criar endpoints basicos de tarefas
- Usar armazenamento em memoria
- Disponibilizar documentacao automatica via Swagger

### Release 0.2.0 - Persistencia

- Adicionar banco de dados
- Criar camada de models
- Criar migrations
- Persistir tarefas entre execucoes
- Adicionar configuracoes por ambiente

### Release 0.3.0 - Testes e qualidade

- Adicionar testes automatizados
- Validar contratos dos endpoints
- Configurar lint e formatacao
- Adicionar tratamento padronizado de erros

### Release 0.4.0 - Priorizacao assistida por IA

- Criar servico de priorizacao
- Enviar contexto das tarefas para modelo de IA
- Retornar sugestao de prioridade
- Registrar justificativa da priorizacao
- Permitir revisao manual da prioridade sugerida

### Release 0.5.0 - Produto minimo utilizavel

- Adicionar filtros por status, prioridade e responsavel
- Adicionar paginacao
- Melhorar documentacao da API
- Preparar deploy inicial

## Licenca

A definir.
