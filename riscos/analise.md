# Análise de Riscos

## 1. Critério de análise

Cada risco foi avaliado com base em probabilidade, impacto e relevância para o MVP atual. A análise adotou uma abordagem qualitativa, conforme prática comum em gestão de riscos de projetos.

- Probabilidade: alta, média ou baixa
- Impacto: alto, médio ou baixo
- Classificação: alta, média ou baixa

## 2. Matriz de análise qualitativa

| ID | Risco | Probabilidade | Impacto | Classificação | Justificativa |
|---|---|---|---|---|---|
| R1 | Falha ou indisponibilidade da integração com OpenAI | Média | Médio | Média | O projeto já prevê fallback local, mas a experiência do usuário pode variar quando a IA não responde adequadamente. |
| R2 | Priorização inadequada das tarefas | Média | Médio | Média | A heurística local é simples e pode não refletir plenamente o contexto da tarefa. |
| R3 | Perda de dados ao reiniciar a aplicação | Alta | Alto | Alta | A persistência em memória torna qualquer reinicialização um ponto crítico de interrupção do estado dos dados. |
| R4 | Inconsistência entre ambientes de execução | Média | Médio | Média | A execução depende de variáveis de ambiente e de um ambiente local preparado corretamente. |
| R5 | Falhas não identificadas em cenários reais | Média | Médio | Média | Os testes cobrem o fluxo principal, mas ainda não substituem a validação em uso operacional real. |
| R6 | Alteração no formato de resposta da API da OpenAI | Média | Médio | Média | O fluxo atual depende de um padrão específico para interpretar a resposta externa. |
| R7 | Atraso ou latência na chamada externa | Média | Médio | Média | O timeout curto e a dependência de rede tornam esse risco relevante para a usabilidade. |
| R8 | Uso indevido da API em ambiente compartilhado | Média | Alto | Alta | A ausência de autenticação e autorização expõe o sistema a um risco maior de acesso não controlado. |

## 3. Priorização dos riscos

### Riscos prioritários

1. R3 — perda de dados por persistência em memória
2. R8 — ausência de controle de acesso em cenários mais amplos
3. R1 — dependência e falhas na integração com IA
4. R2 — qualidade da priorização heurística

### Riscos monitorados

- R4, R5, R6 e R7 devem ser acompanhados ao longo do desenvolvimento, principalmente em validações parciais e em mudanças de configuração ou infraestrutura.

## 4. Considerações finais

A análise indica que o projeto se encontra em um estágio com risco técnico moderado, mas controlável. Os principais pontos de atenção são a evolução da persistência, a robustez da integração externa e a necessidade de melhorar a previsibilidade do comportamento da API em cenários reais.
