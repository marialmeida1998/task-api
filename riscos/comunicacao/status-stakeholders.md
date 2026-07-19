# Status de Riscos e Comunicação com Stakeholders

## 1. Objetivo

Este documento tem como finalidade manter os stakeholders alinhados sobre o estado atual dos riscos do projeto, as ações em andamento e os pontos que exigem atenção.

## 2. Stakeholders envolvidos

- Orientador ou professor responsável pelo projeto acadêmico
- Equipe de desenvolvimento
- Usuários ou interessados no MVP de gerenciamento de tarefas

## 3. Estratégia de comunicação

A comunicação deve ocorrer de forma periódica, com foco em:

- status geral do projeto;
- principais riscos identificados;
- ações corretivas ou preventivas em andamento;
- decisões relevantes para o MVP.

## 4. Cadência recomendada

- semanal, durante o desenvolvimento ativo;
- antes de entregas parciais ou demonstrações;
- sempre que houver mudança relevante na arquitetura, na configuração ou no escopo.

## 5. Status atual (modelo de relatório)

### Status geral: Amarelo

O projeto apresenta risco moderado, principalmente em relação à persistência em memória, à dependência de integração externa para priorização assistida e à necessidade de garantir consistência em ambientes diferentes.

### Pontos principais

- a integração com OpenAI é opcional e o sistema já conta com fallback local;
- a persistência em memória pode comprometer a continuidade dos dados após reinicialização;
- a aplicação possui cobertura de testes para fluxo principal, mas ainda precisa de validação contínua em cenários reais.

### Ações em andamento

- manter o fallback operacional como estratégia de contingência;
- monitorar limitações de execução e configuração de ambiente;
- revisar a evolução do MVP com atenção à robustez e à consistência da experiência do usuário.

### Pendências a acompanhar

- definição de persistência mais robusta em fase futura;
- melhoria da heurística de priorização e validação de resultados;
- alinhamento de expectativas quanto ao comportamento real da API em ambientes diversos.

## 6. Modelo de mensagem para stakeholders

> O projeto segue com desenvolvimento estável, com foco em manter a funcionalidade principal do MVP e reduzir riscos operacionais. O principal ponto de atenção atual é a limitação de persistência em memória e a necessidade de garantir comportamento previsível mesmo em cenários de falha de integração com IA.
