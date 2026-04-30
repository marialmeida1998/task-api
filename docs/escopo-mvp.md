# Escopo do MVP - Micro-API de Tarefas

## Objetivo

Construir uma micro-API para gestao de tarefas de uma equipe interna, entregue em 3 releases: core, qualidade e entrega final.

O MVP deve permitir criar, consultar, atualizar e remover tarefas por meio de endpoints HTTP, mantendo uma base simples para evolucao futura.

## Release 1 - Core

### RF01 - Health check

- [ ] Disponibilizar endpoint `GET /health`
- [ ] Retornar `status` com valor `ok`
- [ ] Retornar `timestamp` em formato ISO 8601
- [ ] Responder com HTTP `200 OK`

### RF02 - Criar tarefa

- [ ] Disponibilizar endpoint `POST /tasks`
- [ ] Receber `titulo`, `descricao`, `prioridade` e `responsavel`
- [ ] Gerar identificador unico para a tarefa
- [ ] Definir status inicial como `pendente`
- [ ] Retornar a tarefa criada
- [ ] Responder com HTTP `201 Created`

### RF03 - Listar tarefas

- [ ] Disponibilizar endpoint `GET /tasks`
- [ ] Retornar lista de tarefas cadastradas
- [ ] Retornar lista vazia quando nao houver tarefas
- [ ] Responder com HTTP `200 OK`

### RF04 - Consultar tarefa por ID

- [ ] Disponibilizar endpoint `GET /tasks/{task_id}`
- [ ] Retornar a tarefa quando o ID existir
- [ ] Retornar erro quando o ID nao existir
- [ ] Responder com HTTP `200 OK` para tarefa encontrada
- [ ] Responder com HTTP `404 Not Found` para tarefa inexistente

### RT01 - Estrutura base da aplicacao

- [ ] Manter aplicacao FastAPI em `app/main.py`
- [ ] Declarar dependencias em `requirements.txt`
- [ ] Permitir execucao local com `uvicorn app.main:app --reload`
- [ ] Manter ambiente virtual fora do versionamento

## Release 2 - Qualidade

### RF05 - Atualizar tarefa

- [ ] Disponibilizar endpoint `PUT /tasks/{task_id}`
- [ ] Permitir atualizacao de `titulo`, `descricao`, `status`, `prioridade` e `responsavel`
- [ ] Atualizar campo `atualizado_em`
- [ ] Retornar a tarefa atualizada
- [ ] Responder com HTTP `200 OK` para tarefa atualizada
- [ ] Responder com HTTP `404 Not Found` para tarefa inexistente

### RF06 - Remover tarefa

- [ ] Disponibilizar endpoint `DELETE /tasks/{task_id}`
- [ ] Remover tarefa existente
- [ ] Responder com HTTP `204 No Content` para remocao concluida
- [ ] Responder com HTTP `404 Not Found` para tarefa inexistente

### RF07 - Validar status de tarefa

- [ ] Aceitar apenas status previstos pelo MVP
- [ ] Suportar `pendente`, `em_andamento`, `concluida` e `cancelada`
- [ ] Retornar HTTP `422 Unprocessable Entity` para status invalido

### RF08 - Validar prioridade de tarefa

- [ ] Aceitar apenas prioridades previstas pelo MVP
- [ ] Suportar `baixa`, `media`, `alta` e `critica`
- [ ] Retornar HTTP `422 Unprocessable Entity` para prioridade invalida

### RT02 - Testes automatizados

- [ ] Adicionar testes com Pytest
- [ ] Cobrir endpoint `GET /health`
- [ ] Cobrir fluxo de criacao e listagem de tarefas
- [ ] Cobrir consulta de tarefa existente e inexistente
- [ ] Cobrir atualizacao de tarefa
- [ ] Cobrir remocao de tarefa

### RT03 - Contrato e validacao

- [ ] Usar schemas Pydantic para entrada e saida
- [ ] Retornar JSON como formato padrao
- [ ] Usar codigos HTTP adequados por operacao
- [ ] Padronizar mensagens de erro basicas

## Release 3 - Entrega final

### RF09 - Filtrar tarefas

- [ ] Permitir filtro por `status`
- [ ] Permitir filtro por `prioridade`
- [ ] Permitir filtro por `responsavel`
- [ ] Retornar HTTP `200 OK` com a lista filtrada
- [ ] Retornar lista vazia quando nenhum item corresponder aos filtros

### RF10 - Preparar priorizacao assistida por IA

- [ ] Criar campo opcional para justificativa de prioridade
- [ ] Criar estrutura de servico para priorizacao futura
- [ ] Manter priorizacao automatica fora do fluxo obrigatorio do MVP
- [ ] Permitir revisao manual da prioridade

### RT04 - Documentacao da API

- [ ] Garantir acesso a documentacao Swagger em `/docs`
- [ ] Revisar nomes, descricoes e modelos exibidos na documentacao
- [ ] Documentar comandos de execucao local no `README.md`
- [ ] Documentar escopo e backlog em `docs/escopo-mvp.md`

### RT05 - Prontidao para entrega

- [ ] Garantir que o projeto inicia localmente sem erros
- [ ] Garantir que todos os testes passam
- [ ] Garantir que `.venv`, caches e arquivos locais nao sejam versionados
- [ ] Garantir que `requirements.txt` contenha as dependencias necessarias
- [ ] Registrar release final do MVP em commit versionado

## Fora de escopo

- [ ] Autenticacao e autorizacao
- [ ] Interface web ou mobile
- [ ] Persistencia em banco de dados
- [ ] Migrations
- [ ] Deploy em producao
- [ ] Integracao real com modelos de IA
- [ ] Notificacoes externas
- [ ] Comentarios em tarefas
- [ ] Historico de alteracoes por tarefa
- [ ] Anexos em tarefas
- [ ] Multi-tenant
