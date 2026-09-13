# Discovery tecnico da Task API

## Objetivo do discovery

A Task API e uma micro-API FastAPI para gerenciamento de tarefas de uma equipe interna. O sistema oferece operacoes CRUD, validacao por schemas Pydantic e priorizacao local com integracao opcional com a OpenAI.

Esta documentacao foi produzida exclusivamente a partir do codigo e dos documentos existentes no repositorio.

## Escopo confirmado

- `GET /health` para verificacao basica da API.
- Criacao, listagem, consulta, atualizacao e remocao de tarefas.
- Validacao de titulo, descricao, status e prioridade.
- Geracao de UUID, status inicial `pendente` e timestamps.
- Persistencia em memoria durante a execucao do processo.
- Priorizacao local por palavras-chave.
- Consulta opcional a OpenAI quando `OPENAI_API_KEY` esta configurada.
- Fallback local em falhas tratadas, timeouts ou respostas sem prioridade reconhecivel.
- Documentacao interativa FastAPI em `/docs`.

## Componentes e responsabilidades

- **API:** expoe as rotas HTTP, recebe schemas e traduz recursos inexistentes para `404`.
- **Models:** define schemas Pydantic e enums de status e prioridade.
- **TaskService:** coordena regras de negocio, CRUD e priorizacao.
- **TaskRepository:** cria e atualiza `TaskOut` e mantem o dicionario em memoria.
- **PriorityAdvisor:** executa a heuristica local, consulta a LLM quando habilitada e aplica o fallback.

A separacao entre armazenamento em memoria e `TaskRepository` e uma representacao logica para fins de documentacao. No codigo, o dicionario e um atributo interno do repositorio.

## Priorizacao

A heuristica local avalia titulo e descricao, nesta ordem:

1. termos criticos: `critico`, `critica`, `urgente`, `bloqueio` e `incidente`;
2. termos de alta prioridade: `alta`, `importante`, `risco` e `prazo`;
3. termos de baixa prioridade: `baixa`, `quando der`, `sem urgencia` e `baixa prioridade`;
4. prioridade de entrada ou prioridade atual quando nenhum termo corresponde.

Com `OPENAI_API_KEY`, o sistema tenta a API Responses da OpenAI depois da heuristica local. Uma prioridade reconhecivel da resposta e utilizada. Falhas tratadas, timeouts e respostas sem prioridade valida retornam ao resultado local.

## Limites e desconhecidos

- Os dados sao perdidos quando a aplicacao reinicia.
- Nao ha autenticacao, autorizacao, auditoria, filtros, paginacao ou deploy configurado.
- O codigo nao define regras de transicao entre status.
- Nao estao definidos volume, concorrencia, escalabilidade, observabilidade ou topologia de deploy.
- `OPENAI_TIMEOUT_SECONDS` aparece no `.env.example`, mas nao e lida pelo codigo.
- O arquivo `.env` nao e carregado automaticamente por uma dependencia ou rotina da aplicacao.

## Artefatos arquiteturais

- [Diagrama estrutural](architecture-container.mmd)
- [Diagrama comportamental de criacao de tarefa](sequence-create-task.mmd)
