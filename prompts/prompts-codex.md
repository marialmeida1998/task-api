## Prompt 1 - .gitignore

> **Contexto:** Estou iniciando uma API Python com FastAPI em um repositório de produto  
> **Objetivo:** Gerar um arquivo `.gitignore` para Python, ambiente virtual, cache de testes e configurações locais do editor  
> **Estilo:** Organizado por seções com comentários  
> **Resposta:** Forneça apenas o conteúdo do arquivo `.gitignore`

## Prompt 2 - README inicial

> **Contexto:** MVP de micro-API para gestão de tarefas com priorização assistida por IA  
> **Objetivo:** Escrever um README inicial com objetivo, stack, como rodar localmente e roadmap de releases  
> **Estilo:** Markdown simples, direto e profissional  
> **Resposta:** Forneça o README completo

## Prompt 3 - Endpoint de healthcheck

> **Contexto:** Projeto em Python 3.11 com FastAPI  
> **Objetivo:** Criar `app/main.py` com uma instância FastAPI e endpoint GET `/health` retornando status "ok" e timestamp  
> **Estilo:** Código limpo e tipado  
> **Resposta:** Forneça apenas o código de `app/main.py`

## Prompt 4 - Revisão crítica

> **Contexto:** Código gerado para o endpoint `/health` em FastAPI  
> **Objetivo:** Avaliar riscos técnicos, possíveis falhas em produção e sugerir testes mínimos  
> **Estilo:** Resposta curta em checklist  
> **Resposta:** Apenas checklist

## Prompt 5 - Mensagem de commit

> **Contexto:** Estrutura inicial criada, README, `.gitignore` e endpoint `/health` adicionados  
> **Objetivo:** Gerar mensagem de commit no padrão Conventional Commits  
> **Estilo:** Direto  
> **Resposta:** Apenas uma linha

## Prompt 6 - Escopo MVP

> **Contexto:** MVP de micro-API de tarefas para uso de equipe interna  
> **Objetivo:** Gerar documento de escopo com objetivo, requisitos funcionais, não funcionais e fora de escopo  
> **Estilo:** Linguagem técnica, direta, em Markdown  
> **Resposta:** Forneça o conteúdo completo de `docs/escopo-mvp.md`

## Prompt 7 - Backlog com releases

> **Contexto:** O produto será entregue em 3 releases: core, qualidade e entrega final  
> **Objetivo:** Criar backlog mínimo com IDs (RF/RT) e critérios de aceite  
> **Estilo:** Checklist em Markdown  
> **Resposta:** Conteúdo de `docs/escopo-mvp.md`

## Prompt 8 - Diagrama de componentes

> **Contexto:** FastAPI com camadas API, Service, Repository e componente PriorityAdvisor  
> **Objetivo:** Gerar diagrama Mermaid de componentes e fluxo de dados  
> **Estilo:** Simples, legível e versionável  
> **Resposta:** Apenas bloco Mermaid com o arquivo no repositório  
 
## Prompt 9 - Mensagens de commit (Conventional Commits)

> **Contexto:** Adicionei `docs/escopo-mvp.md`, `docs/arquitetura.md` e `docs/backlog.md`  
> **Objetivo:** Sugerir 3 mensagens de commit no padrão Conventional Commits  
> **Estilo:** Direto e conciso  
> **Resposta:** Apenas 3 linhas de commit e faça os commits para mim

## Prompt 10 - Revisão de planejamento

> **Contexto:** Escopo MVP e backlog definidos para uma micro-API de tarefas  
> **Objetivo:** Avaliar tamanho da release inicial, lacunas de testabilidade e riscos técnicos  
> **Estilo:** Bullets curtos e diretos  
> **Resposta:** Apenas lista em bullets  

## Prompt 11 - Modelo Pydantic

> **Contexto:** API de tarefas em FastAPI para uso interno de equipe  
> **Objetivo:** Gerar modelos `TaskCreate`, `TaskUpdate` e `TaskOut` com tipagem e validações  
> **Estilo:** Código limpo, tipado e organizado  
> **Resposta:** Apenas código de `app/models/task.py`  

## Prompt 12 - Repositório inicial

> **Contexto:** Preciso de persistência inicial enxuta para viabilizar a primeira release  
> **Objetivo:** Criar `TaskRepository` em memória com métodos `create`, `list`, `get_by_id`, `update` e `delete`  
> **Estilo:** Python tipado, sem dependências externas  
> **Resposta:** Código completo de `app/repositories/task_repository.py`  

## Prompt 13 - Service com regra de prioridade

> **Contexto:** A prioridade da tarefa pode ser sugerida automaticamente  
> **Objetivo:** Criar `TaskService` que utilize `TaskRepository` e `PriorityAdvisor`  
> **Estilo:** Código limpo, tipado e organizado  
> **Resposta:** Código completo de `app/services/task_service.py`  

## Prompt 14 - PriorityAdvisor com fallback

> **Contexto:** Quero rodar sem custo de API quando não houver chave  
> **Objetivo:** Implementar `PriorityAdvisor` com heurística local e chamada opcional a LLM quando `OPENAI_API_KEY` existir  
> **Estilo:** Falha segura, com timeout e fallback obrigatório  
> **Resposta:** Código completo de `app/services/priority_advisor.py`  

## Prompt 15 - Rotas CRUD

> **Contexto:** FastAPI com `TaskService` pronto  
> **Objetivo:** Criar rotas `POST`, `GET`, `PUT` e `DELETE` para tarefas com status HTTP corretos e tratamento de `404`  
> **Estilo:** Router separado em `app/api/task_routes.py`  
> **Resposta:** Apenas o código do arquivo  

## Prompt 16 - Revisão técnica

> **Contexto:** Arquivos do core da API (models, repository, service e rotas)  
> **Objetivo:** Avaliar acoplamento, validações faltantes e priorização de testes  
> **Estilo:** Checklist direto e objetivo  
> **Resposta:** Apenas checklist  

## Prompt 17 - Testes de service

> **Contexto:** Tenho `TaskService` com CRUD de tarefas  
> **Objetivo:** Gerar suíte Pytest cobrindo criação, listagem, atualização, exclusão e erro por ID inexistente  
> **Estilo:** Testes claros, nomes descritivos e fixtures simples  
> **Resposta:** Código completo de `tests/test_task_service.py`  

## Prompt 18 - Testes do PriorityAdvisor

> **Contexto:** `PriorityAdvisor` possui heurística local e fallback quando a chamada externa falha  
> **Objetivo:** Gerar testes para os três níveis de prioridade e para o fallback  
> **Estilo:** Usar `monkeypatch` quando necessário  
> **Resposta:** Código completo de `tests/test_priority_advisor.py`  

## Prompt 19 - Testes da API

> **Contexto:** API FastAPI com endpoints CRUD de `/tasks`  
> **Objetivo:** Criar testes de rota com `TestClient` para status `201`, `200`, `204` e `404`  
> **Estilo:** Isolar dependência de repositório para evitar estado global entre testes  
> **Resposta:** Código completo de `tests/test_task_routes.py`  

## Prompt 20 - Refatoração DRY/SRP

> **Contexto:** Arquivos `app/services/task_service.py` e `app/repositories/task_repository.py`  
> **Objetivo:** Sugerir refatoração com foco em DRY (Don't Repeat Yourself) e SRP (Single Responsibility Principle), sem adicionar dependências externas  
> **Estilo:** Técnico, direto e organizado  
> **Resposta:** 1) Lista de mudanças propostas  2) Patch sugerido por arquivo  

## Prompt 21 - README final técnico

> **Contexto:** MVP de micro-API de tarefas com prioridade assistida por IA  
> **Objetivo:** Gerar README completo com instalação, execução, testes, arquitetura, uso e limitações  
> **Estilo:** Markdown profissional, objetivo e bem estruturado  
> **Resposta:** README completo  

## Prompt 22 - Revisão final de qualidade

> **Contexto:** Código e testes atuais da aplicação  
> **Objetivo:** Avaliar riscos técnicos restantes, cobertura de testes e melhorias prioritárias  
> **Estilo:** Bullets curtos e diretos  
> **Resposta:** Checklist em bullets  

## Prompt 23 - Makefile

> **Contexto:** Projeto FastAPI com comandos de instalar dependências, executar API e rodar testes  
> **Objetivo:** Gerar Makefile com targets `install`, `run` e `test`  
> **Estilo:** Simples e portável  
> **Resposta:** Conteúdo completo do `Makefile`  

## Prompt 24 - .env.example

> **Contexto:** Projeto FastAPI com uso opcional de integração com LLM  
> **Objetivo:** Criar arquivo `.env.example` com variáveis essenciais (API key, ambiente, configurações básicas)  
> **Estilo:** Claro, comentado e seguro (sem dados sensíveis reais)  
> **Resposta:** Conteúdo completo do `.env.example`  

## Prompt 25 - Revisão de README

> **Contexto:** README atual do projeto  
> **Objetivo:** Avaliar reprodutibilidade, onboarding técnico e uso de IA  
> **Estilo:** Checklist objetivo e direto  
> **Resposta:** Apenas checklist  
