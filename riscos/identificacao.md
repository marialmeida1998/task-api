# Identificação de Riscos

## 1. Contexto do projeto

Esta micro-API em FastAPI tem como objetivo gerenciar tarefas de uma equipe interna, com cadastro, consulta, atualização e remoção de registros. O MVP utiliza um componente de priorização baseado em heurística local e, de forma opcional, em uma integração com a OpenAI, sempre com fallback para a lógica local quando a chamada externa falha.

## 2. Premissas para identificação

A identificação dos riscos foi realizada com base nos elementos efetivamente presentes no projeto atual, incluindo:

- rotas CRUD para tarefas expostas via FastAPI;
- camada de serviço com regras de negócio e priorização;
- repositório em memória, sem persistência durável;
- uso opcional de variáveis de ambiente para integração com IA;
- fallback local para priorização em cenários de falha;
- testes automatizados para fluxos principais e cenários de erro.

## 3. Registro inicial de riscos

| ID | Risco | Causa provável | Efeito potencial | Categoria | Responsável sugerido |
|---|---|---|---|---|---|
| R1 | Falha ou indisponibilidade da integração com OpenAI | ausência de chave, timeout, erro na API externa ou resposta inválida | a priorização pode depender apenas da heurística local, reduzindo a qualidade da decisão | Técnico / Externo | Equipe de desenvolvimento |
| R2 | Priorização inadequada das tarefas | heurística local baseada em palavras-chave simples | tarefas podem receber prioridade incorreta, afetando a percepção de urgência e a gestão do fluxo de trabalho | Técnico / Negócio | Equipe de desenvolvimento |
| R3 | Perda de dados ao reiniciar a aplicação | repositório implementado em memória | as tarefas criadas podem deixar de existir após reinicialização da API | Técnico / Operacional | Equipe de desenvolvimento |
| R4 | Inconsistência entre ambientes de execução | dependência de variáveis de ambiente e configuração manual | a aplicação pode apresentar comportamento diferente entre ambientes locais e de validação | Técnico / Operacional | Equipe de desenvolvimento |
| R5 | Falhas não identificadas em cenários reais | cobertura de testes limitada a cenários principais | problemas operacionais podem surgir somente em uso real | Técnico | Equipe de desenvolvimento |
| R6 | Alteração no formato de resposta da API da OpenAI | a integração atual depende de um formato específico de payload e resposta | a extração da prioridade pode falhar mesmo com a chave configurada | Técnico / Externo | Equipe de desenvolvimento |
| R7 | Atraso ou latência na chamada externa | timeout curto e dependência de rede | a experiência do usuário pode ser afetada por demora ou indisponibilidade temporária | Técnico / Externo | Equipe de desenvolvimento |
| R8 | Uso indevido da API em ambiente compartilhado | ausência de autenticação e autorização | a aplicação pode expor operações sem controle de acesso em cenários mais amplos | Segurança / Operacional | Equipe de desenvolvimento |

## 4. Observações importantes

Os riscos mais relevantes para este estágio são aqueles ligados à dependência externa de IA, à limitação de persistência e à necessidade de manter um comportamento previsível mesmo em cenários de falha operacional.
