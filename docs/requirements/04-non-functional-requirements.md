# Especificação de Requisitos Não Funcionais - Task API

## 1. Objetivo

Este documento especifica os requisitos não funcionais identificados para a Task API com base nas histórias de usuário, nas regras de negócio e nas limitações observadas no projeto atual. As definições abaixo consideram as funcionalidades existentes de CRUD de tarefas, priorização assistida e operação via API REST.

## 2. Escopo

Os requisitos não funcionais a seguir se aplicam ao contexto atual do sistema, em que a aplicação:
- expõe endpoints para criar, listar, consultar, atualizar e remover tarefas;
- utiliza priorização local e, de forma opcional, integração com OpenAI;
- mantém os dados em memória;
- não implementa autenticação nem autorização no estado atual do projeto.

## 3. Requisitos não funcionais

### 3.1 Autenticação
- O projeto atual não implementa autenticação.
- Como requisito de evolução futura, a API deve prever mecanismos de autenticação para proteger o acesso aos endpoints, caso a aplicação passe a ser utilizada em ambiente compartilhado ou com mais de um perfil de usuário.

### 3.2 Disponibilidade
- A API deve estar disponível para operações básicas de gerenciamento de tarefas sempre que o serviço estiver em execução.
- A indisponibilidade temporária da integração com OpenAI não deve impedir o funcionamento da aplicação, pois o sistema deve continuar a operar com fallback local.

### 3.3 Integridade dos dados
- As tarefas devem manter valores válidos para título, descrição, status, prioridade e responsável, conforme as regras definidas pela aplicação.
- A API deve rejeitar entradas inválidas, como título vazio ou prioridade fora dos valores permitidos, retornando erro de validação.
- Os dados devem ser mantidos em um formato consistente durante as operações de criação, leitura, atualização e remoção.

### 3.4 Controle de acesso
- No estado atual do projeto, não há controle de acesso implementado.
- Em uma evolução futura, o sistema deve controlar o acesso às operações de tarefa por perfil ou papel, de modo a evitar uso indevido da API.

### 3.5 Desempenho
- A API deve responder de forma adequada para operações simples de CRUD e para a lógica de priorização local.
- O uso da priorização por integração externa deve ser tratado de forma que não comprometa o funcionamento principal da API em caso de falha ou latência.
- O tempo de resposta deve ser compatível com o uso local e com cenários de validação simples da aplicação.

### 3.6 Tratamento de falhas
- A aplicação deve responder de forma previsível a erros de validação, recursos inexistentes e falhas de integração externa.
- Em caso de falha na integração com OpenAI, a aplicação deve manter o funcionamento com fallback local.
- Erros de recurso inexistente devem resultar em resposta 404, e erros de entrada inválida devem resultar em resposta 422.

### 3.7 Auditoria
- O projeto atual não implementa mecanismos formais de auditoria.
- Como evolução futura, a API deve registrar eventos relevantes de criação, atualização e remoção de tarefas, além de operações de priorização, para apoiar rastreabilidade e acompanhamento.

## 4. Requisitos não funcionais resumidos

| Categoria | Requisito |
|---|---|
| Autenticação | Deve existir mecanismo de autenticação em evolução futura para proteger o acesso à API. |
| Disponibilidade | A API deve continuar operando mesmo quando a integração com IA estiver indisponível. |
| Integridade dos dados | As operações devem preservar a consistência dos campos e rejeitar entradas inválidas. |
| Controle de acesso | Deve existir controle de acesso em evolução futura para proteger operações sensíveis. |
| Desempenho | A API deve responder adequadamente para operações básicas e para priorização local. |
| Tratamento de falhas | A API deve tratar falhas de integração e entradas inválidas com respostas previsíveis. |
| Auditoria | Deve existir rastreabilidade de operações em evolução futura. |

## 5. Observações finais

Esses requisitos não funcionais foram definidos com base no que existe hoje na Task API e nas limitações observadas no projeto. Eles não pressupõem funcionalidades que ainda não foram implementadas, mas apontam para necessidades de evolução técnica e operacional do sistema.
