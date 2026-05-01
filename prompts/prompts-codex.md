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
