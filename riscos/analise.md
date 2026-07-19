# Análise de Riscos

## 1. Critério de análise

Para cada risco, foi atribuída uma avaliação qualitativa de probabilidade e impacto, considerando a maturidade do MVP e a arquitetura atual do projeto.

- Probabilidade: alta, média ou baixa
- Impacto: alto, médio ou baixo
- Classificação: prioridade alta, média ou baixa

## 2. Matriz de análise

| ID | Risco | Probabilidade | Impacto | Classificação | Justificativa |
|---|---|---|---|---|---|
| R1 | Falha ou indisponibilidade da integração com OpenAI | Média | Médio | Média | O projeto já prevê fallback, mas a experiência do usuário pode variar quando a IA não responde corretamente. |
| R2 | Priorização inadequada das tarefas | Média | Médio | Média | A heurística local é simples e pode não refletir plenamente o contexto da tarefa. |
| R3 | Perda de dados ao reiniciar a aplicação | Alta | Alto | Alta | Como a persistência é em memória, qualquer reinicialização interrompe a disponibilidade dos dados. |
| R4 | Inconsistência em ambientes de execução | Média | Médio | Média | A configuração depende de variáveis de ambiente e de um ambiente local bem preparado. |
| R5 | Falhas não cobertas em cenários reais | Média | Médio | Média | O projeto possui testes importantes, porém ainda não substitui validação em ambiente operacional real. |
| R6 | Alteração no formato de resposta da API da OpenAI | Média | Médio | Média | O código atual depende de um fluxo específico para extrair prioridade a partir da resposta externa. |
| R7 | Atraso ou latência na chamada externa | Média | Médio | Média | O timeout curto e a dependência de rede tornam esse risco relevante para a usabilidade da aplicação. |

## 3. Priorização dos riscos

### Riscos prioritários

1. R3 — perda de dados por persistência em memória
2. R1 — dependência e falhas na integração com IA
3. R2 — qualidade da priorização heurística

### Riscos monitorados

- R4, R5, R6 e R7 devem ser acompanhados ao longo do desenvolvimento, principalmente em validações e entregas parciais.

## 4. Considerações finais

A análise indica que o projeto encontra-se em um estágio com risco técnico moderado, mas controlável. O maior ponto de atenção é a evolução do MVP para um ambiente mais confiável, especialmente em termos de persistência, integração externa e consistência operacional.
