# Respostas aos Riscos

## 1. Estratégia geral

As respostas foram definidas com foco em mitigação, monitoramento e contingência, considerando o estágio atual do MVP e as limitações técnicas observadas no projeto.

## 2. Plano de respostas aos riscos

| ID | Estratégia | Ação proposta | Observação |
|---|---|---|---|
| R1 | Mitigar | Manter o fallback local como mecanismo principal de contingência e documentar o comportamento esperado da integração com OpenAI. | O projeto já implementa esse comportamento de forma explícita. |
| R2 | Mitigar | Aprimorar a heurística local e preservar a prioridade informada pelo usuário quando não houver sinais claros de urgência. | Isso reduz o risco de priorização equivocada. |
| R3 | Mitigar | Planejar a evolução para armazenamento persistente, como arquivo ou banco de dados, em uma fase posterior do sistema. | O risco é relevante porque a aplicação atual é volátil por natureza. |
| R4 | Mitigar | Padronizar o uso de variáveis de ambiente e registrar os passos de execução em documentação de apoio. | Isso melhora a reprodutibilidade em diferentes ambientes. |
| R5 | Mitigar | Expandir os testes para cenários de falha, validação e comportamento de fallback. | O aumento da cobertura reduz a probabilidade de defeitos inesperados. |
| R6 | Mitigar | Validar a resposta recebida antes de aplicar a prioridade sugerida e tratar entradas inesperadas com segurança. | Isso reduz a fragilidade da dependência externa. |
| R7 | Mitigar / Monitorar | Manter o timeout da integração em um limite adequado e acompanhar o comportamento em chamadas reais. | A ação pode reduzir impactos de latência e falha de resposta. |
| R8 | Mitigar | Definir, em fase futura, mecanismos de autenticação e autorização para controle de acesso. | O risco é mais relevante caso a API seja exposta além do uso interno inicial. |

## 3. Ações imediatas recomendadas

- manter a lógica de fallback para priorização como parte do desenho da API;
- registrar as limitações de persistência e acesso no documento de contexto do projeto;
- incluir validações adicionais para cenários de falha de IA, ausência de configuração e respostas inesperadas;
- revisar a configuração do ambiente antes de demonstrações e validações;
- manter uma postura de monitoramento contínuo para os riscos de dependência externa e comportamento operacional.

## 4. Monitoramento contínuo

Os riscos devem ser revisados periodicamente durante o ciclo de desenvolvimento, principalmente após mudanças em dependências, configuração de ambiente, estrutura da API ou definição de escopo.
