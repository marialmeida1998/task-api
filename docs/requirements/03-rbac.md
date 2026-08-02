# Matriz RBAC - Task API

## 1. Objetivo

Este documento apresenta uma matriz de perfis e permissões com base no estado atual do projeto e nas histórias de usuário identificadas. Como a Task API, no seu MVP atual, não implementa autenticação nem autorização, a matriz abaixo reflete apenas os perfis que podem ser considerados para evolução futura do sistema, sem transformar essa evolução em funcionalidade já existente.

## 2. Premissas

- A aplicação atual expõe endpoints de CRUD para tarefas.
- Não há autenticação nem autorização implementadas no estado atual do projeto.
- O sistema é uma API backend simples, com persistência em memória e priorização assistida.
- A matriz abaixo é sugerida como referência para evolução futura, não como funcionalidade já implementada.

## 3. Perfis sugeridos para evolução futura

| Perfil | Descrição | Permissões sugeridas |
|---|---|---|
| Usuário da API | Perfil básico para consumo da API | Criar, listar, consultar, atualizar e remover tarefas próprias ou disponíveis no contexto do sistema |
| Equipe interna | Perfil de operação para uso interno da equipe | Visualizar tarefas, atualizar status e prioridade, acompanhar execução das atividades |
| Administrador | Perfil de gestão operacional | Gerenciar tarefas, revisar regras de priorização, ajustar configurações operacionais da aplicação |

## 4. Matriz de permissões sugerida

| Recurso / ação | Usuário da API | Equipe interna | Administrador |
|---|---|---|---|
| Criar tarefa | Sim | Sim | Sim |
| Listar tarefas | Sim | Sim | Sim |
| Consultar tarefa | Sim | Sim | Sim |
| Atualizar tarefa | Parcial | Sim | Sim |
| Remover tarefa | Parcial | Sim | Sim |
| Alterar status | Não | Sim | Sim |
| Alterar prioridade | Não | Sim | Sim |
| Gerenciar configuração da API | Não | Não | Sim |

## 5. Observações

- A matriz acima deve ser entendida como uma proposta para evolução futura da API.
- No estado atual do projeto, a ausência de autenticação e autorização significa que qualquer controle de acesso real ainda não está implementado.
- A recomendação é manter essa matriz apenas como referência para um estágio posterior de evolução da aplicação.
