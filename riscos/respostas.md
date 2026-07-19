# Respostas aos Riscos

## 1. Estratégia geral

As respostas foram definidas com foco em mitigação, monitoramento e preparação para contingência, de acordo com o contexto do projeto acadêmico e com as capacidades atuais da aplicação.

## 2. Plano de respostas

| ID | Estratégia | Ação proposta | Observação |
|---|---|---|---|
| R1 | Mitigar | Manter o fallback local como mecanismo principal de contingência e documentar o comportamento esperado da integração com OpenAI. | O projeto já implementa esse comportamento. |
| R2 | Mitigar | Continuar aprimorando a heurística local e preservar a prioridade informada pelo usuário quando não houver sinais claros. | Isso reduz o risco de priorização equivocada. |
| R3 | Mitigar | Planejar a evolução para armazenamento persistente, como arquivo ou banco de dados, em uma próxima fase. | O risco é relevante porque a aplicação atual é volátil por natureza. |
| R4 | Mitigar | Padronizar a configuração de variáveis de ambiente e registrar os passos de execução em documentos de apoio. | Isso melhora a reprodutibilidade do ambiente. |
| R5 | Mitigar | Expandir os testes para novos cenários de falha, validação e comportamento de fallback. | O aumento da cobertura reduz a probabilidade de defeitos inesperados. |
| R6 | Mitigar | Adotar uma abordagem de integração mais robusta, com validação da resposta recebida antes de aplicar a prioridade sugerida. | Isso reduz a fragilidade da dependência externa. |
| R7 | Mitigar / Monitorar | Manter o timeout da integração em um limite adequado e monitorar o comportamento em chamadas reais. | A ação pode reduzir impactos de latência e falha de resposta. |

## 3. Ações imediatas recomendadas

- manter a lógica de fallback para priorização como parte do desenho da API;
- registrar em documentação as limitações da persistência atual;
- incluir validações adicionais para cenários de falha de IA, ausência de configuração e respostas inesperadas;
- revisar a configuração de ambiente antes de qualquer validação ou demonstração.

## 4. Monitoramento contínuo

Os riscos devem ser revisados periodicamente durante o ciclo de desenvolvimento, principalmente após mudanças em dependências, configuração de ambiente ou estrutura da API.
