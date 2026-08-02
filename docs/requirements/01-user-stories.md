# Documento de Requisitos - Task API

## 1. Visão geral do sistema

A Task API é uma micro-API em FastAPI para gerenciamento de tarefas de uma equipe interna. O sistema permite criar, listar, consultar, atualizar e remover tarefas por meio de endpoints HTTP.

A aplicação possui uma camada de serviço para organizar as regras de negócio e um componente de priorização que pode usar uma heurística local e, de forma opcional, uma integração com a OpenAI. Quando a integração externa não está disponível, o sistema utiliza o resultado da heurística local como fallback.

## 2. Atores identificados

- Usuário da API: consome os endpoints para criar, consultar, listar, atualizar e remover tarefas.
- Equipe interna: recebe tarefas com informações de prioridade, status e responsável.
- Sistema de priorização: componente interno que avalia a prioridade das tarefas com base em heurística local e, quando disponível, em integração externa.

## 3. Histórias de usuário

### História 1
Como usuário da API
Quero criar uma tarefa
Para registrar uma nova atividade com título, descrição, prioridade, status inicial e responsável.

### História 2
Como usuário da API
Quero listar as tarefas cadastradas
Para visualizar o conjunto de tarefas disponíveis no sistema.

### História 3
Como usuário da API
Quero consultar uma tarefa específica pelo seu identificador
Para visualizar os detalhes de uma tarefa existente.

### História 4
Como usuário da API
Quero atualizar uma tarefa existente
Para alterar informações como título, descrição, status, prioridade e responsável.

### História 5
Como usuário da API
Quero remover uma tarefa
Para excluir uma tarefa que não deve mais permanecer cadastrada.

### História 6
Como usuário da API
Quero que a prioridade da tarefa seja sugerida automaticamente
Para reduzir o esforço manual na classificação inicial da tarefa.

### História 7
Como usuário da API
Quero que a aplicação continue funcionando mesmo quando a integração com IA falhar
Para garantir que a priorização ainda seja realizada com fallback local.

## 4. Regras de negócio identificadas

- Cada tarefa deve possuir um título obrigatório com tamanho entre 1 e 120 caracteres.
- A descrição da tarefa é opcional, com limite máximo de 1000 caracteres.
- A prioridade da tarefa deve ser uma das opções permitidas: baixa, media, alta ou critica.
- O status inicial de uma tarefa criada é "pendente".
- O status de uma tarefa pode assumir os valores: pendente, em_andamento, concluida ou cancelada.
- A atualização de uma tarefa pode alterar título, descrição, status, prioridade e responsável.
- Quando a prioridade não é informada explicitamente em uma atualização, o sistema pode recalcular a prioridade com base na tarefa atual e no conteúdo atualizado.
- A priorização local usa palavras-chave presentes no título e na descrição para inferir prioridade.
- A integração com a OpenAI é opcional e depende da variável de ambiente OPENAI_API_KEY.
- Se a integração com IA falhar, o sistema deve retornar para a priorização local.
- O endpoint de health-check deve responder com status de operação da API.

## 5. Requisitos não funcionais identificados

- A aplicação deve expor uma API REST com endpoints para gerenciamento de tarefas.
- A aplicação deve fornecer documentação interativa por meio do FastAPI Swagger/OpenAPI, acessível em /docs.
- O sistema deve responder com status HTTP adequado para operações bem-sucedidas e para cenários de erro, como 404 Not Found e 422 Unprocessable Entity.
- A aplicação deve possuir testes automatizados para validar o comportamento principal das rotas, serviços e lógica de priorização.
- A aplicação deve funcionar sem a configuração de IA, mantendo o comportamento básico de priorização local.
- A aplicação utiliza persistência em memória, o que implica que os dados não são duráveis após reinicialização.
- A aplicação não implementa autenticação nem autorização no estado atual do projeto.
- A aplicação não possui paginacao nem filtros avançados para listagem de tarefas.
