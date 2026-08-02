---
name: recomendar-artefatos-requisitos
description: Analisa histórias de usuário e recomenda artefatos de Engenharia de Requisitos adequados ao contexto do projeto, com prioridade e justificativa.
---

# Skill: Recomendar Artefatos de Requisitos

## Objetivo
Analisar histórias de usuário e demais informações de contexto do projeto para recomendar os artefatos de Engenharia de Requisitos mais adequados, considerando a maturidade atual da aplicação e os elementos efetivamente presentes no repositório.

## Contexto de aplicação
Esta skill deve ser usada quando for necessário apoiar a elicitação, organização e documentação de requisitos para projetos acadêmicos ou sistemas com escopo simples, como a Task API.

## Critérios de recomendação
A recomendação deve considerar:
- complexidade funcional do sistema;
- presença de regras de negócio claras;
- necessidade de comunicação visual entre atores e processos;
- relevância de rastreabilidade e validação;
- maturidade do projeto e grau de evolução esperado.

## Artefatos e recomendações

### 1. Critérios de Aceitação
- Prioridade: Alta
- Justificativa: São fundamentais para transformar as histórias de usuário em critérios objetivos de validação, especialmente para o fluxo CRUD de tarefas e a lógica de priorização.

### 2. Casos de Uso
- Prioridade: Alta
- Justificativa: O projeto possui funcionalidades bem delimitadas de criação, consulta, atualização, remoção e priorização, o que torna os casos de uso adequados para representar cenários principais.

### 3. Matriz de Perfis e Permissões (RBAC)
- Prioridade: Baixa
- Justificativa: O projeto atual não implementa autenticação, autorização ou perfis de usuário; portanto, esse artefato é pouco relevante no estado atual do MVP.

### 4. Especificação de Requisitos Não Funcionais
- Prioridade: Alta
- Justificativa: O projeto apresenta limitações explícitas em persistência, documentação, testes, segurança e operação, o que justifica a necessidade de registrar requisitos não funcionais.

### 5. Protótipos
- Prioridade: Média
- Justificativa: Podem ser úteis para ilustrar a experiência de uso da API e o fluxo de interação, mas não são essenciais para uma API backend enxuta sem interface gráfica.

### 6. Diagrama de Casos de Uso
- Prioridade: Alta
- Justificativa: Ajuda a visualizar atores, funcionalidades principais e o escopo do sistema de forma clara e didática.

### 7. Diagrama de Sequência UML
- Prioridade: Média
- Justificativa: Pode apoiar a compreensão do fluxo entre rotas, serviço, repositório e componente de priorização, especialmente para a lógica de criação e atualização de tarefas.

### 8. Matriz de Rastreabilidade
- Prioridade: Alta
- Justificativa: É recomendada para conectar histórias de usuário, regras de negócio, requisitos e testes, facilitando a rastreabilidade do projeto acadêmico.

### 9. DER
- Prioridade: Baixa
- Justificativa: O projeto não possui banco de dados nem modelo persistente formal implementado; portanto, um DER não é prioritário para o MVP atual.

### 10. BPMN
- Prioridade: Média
- Justificativa: Pode ser útil para representar visualmente o fluxo de gestão de tarefas e o processo de priorização, embora o projeto seja simples e não tenha processos de negócio complexos.

### 11. Diagrama de Estados
- Prioridade: Alta
- Justificativa: O sistema trabalha com estados explícitos de tarefa, como pendente, em_andamento, concluida e cancelada, o que torna esse artefato muito relevante.

## Saída esperada
Ao utilizar esta skill, a resposta deve:
- indicar os artefatos recomendados;
- informar a prioridade de cada artefato;
- justificar a recomendação com base no contexto do projeto.
- priorizar os artefatos mais úteis para um projeto acadêmico com CRUD, regras de negócio e priorização assistida.
