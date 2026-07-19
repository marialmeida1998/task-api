# Identificação de Riscos

## 1. Contexto do projeto

Esta micro-API em FastAPI tem como objetivo gerenciar tarefas com priorização assistida por heurística local e, opcionalmente, por integração com a OpenAI. O fluxo principal inclui rotas CRUD, serviço de negócio, repositório em memória e um componente de priorização que usa fallback local quando a integração externa não está disponível.

## 2. Premissas para identificação de riscos

A identificação foi realizada com base no que existe no projeto atual, incluindo:

- endpoints de criação, consulta, atualização e remoção de tarefas;
- persistência em memória, sem banco de dados;
- uso opcional de variável de ambiente para integração com IA;
- fallback local para priorização quando a chamada externa falha;
- testes automatizados para fluxo principal e cenários de erro.

## 3. Registro inicial de riscos

| ID | Risco | Causa provável | Efeito potencial | Categoria | Responsável sugerido |
|---|---|---|---|---|---|
| R1 | Falha ou indisponibilidade da integração com OpenAI | ausência de chave, timeout, erro na API externa ou resposta inválida | a priorização pode depender apenas da heurística local, reduzindo a qualidade da decisão | Técnico / Externo | Equipe de desenvolvimento |
| R2 | Priorização inadequada das tarefas | heurística local baseada em palavras-chave simples | tarefas podem receber prioridade incorreta, afetando a percepção de urgência | Técnico / Negócio | Equipe de desenvolvimento |
| R3 | Perda de dados ao reiniciar a aplicação | repositório implementado em memória | as tarefas criadas não persistem após reinicialização | Técnico / Operacional | Equipe de desenvolvimento |
| R4 | Inconsistência em ambientes de execução | dependência de variáveis de ambiente e configuração manual | a aplicação pode funcionar de forma diferente entre ambientes | Técnico / Operacional | Equipe de desenvolvimento |
| R5 | Falhas não cobertas em cenários reais | testes automatizados cobrem o fluxo principal, mas não todas as condições operacionais | problemas podem aparecer apenas em uso real | Técnico | Equipe de desenvolvimento |
| R6 | Alteração no formato de resposta da API da OpenAI | o código atual depende de um formato específico de payload/response | a lógica de extração de prioridade pode falhar mesmo com a chave configurada | Técnico / Externo | Equipe de desenvolvimento |
| R7 | Atraso ou latência na chamada externa | timeout configurado de forma curta e dependência de rede | a resposta da API pode demorar mais do que o esperado, impactando a experiência do usuário | Técnico / Externo | Equipe de desenvolvimento |

## 4. Observações importantes

Os riscos mais relevantes para este estágio são aqueles ligados à dependência externa de IA, à limitação de persistência e à necessidade de manter o comportamento previsível mesmo com falhas operacionais.
