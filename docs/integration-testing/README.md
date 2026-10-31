# Testes de integração

## Objetivo

Esta documentação reúne cenários de integração propostos para o `task-api` e registra os prompts usados na elaboração. O conteúdo descreve o comportamento encontrado nas rotas FastAPI, `TaskService`, `TaskRepository`, `PriorityAdvisor`, modelos Pydantic e integração opcional com OpenAI.

IT-01 a IT-28 são propostas baseadas na análise do código. Não foram implementadas nem executadas como parte desta documentação. Nenhum código de produção foi alterado e nenhum endpoint ou regra de negócio adicional é presumido.

## Documentos

- [Cenários de integração](integration-scenarios.md): registro do primeiro prompt e casos IT-01 a IT-16, cobrindo CRUD, validações, integração entre camadas e priorização.
- [Cenários alternativos e erros](alternative-scenarios-and-errors.md): registro do segundo prompt e casos IT-17 a IT-28, cobrindo falhas externas, fallback, respostas inesperadas e falhas injetadas no repositório.
- [Análise dos prompts](prompt-analysis.md): compara escopo, qualidade e diversidade dos resultados, refinamentos e limitações.

## Notas de testabilidade

- Os casos automatizáveis são propostas para `pytest` e `TestClient`, usando repositório em memória isolado. Chamadas externas devem ser simuladas.
- Para verificar uma resposta HTTP 500 em exceções não capturadas, use `TestClient(raise_server_exceptions=False)`. Na configuração padrão, a exceção pode ser propagada ao teste.
- IT-25 a IT-27 exigem um repositório de teste que lance a exceção antes de alterar o estado. O repositório em memória atual não produz essas falhas naturalmente.
- IT-28 é documental/operacional, depende de ambiente externo autorizado e não é determinístico para a suíte automatizada comum.

## Limites da implementação observada

O repositório mantém tarefas em memória. `TaskService` não captura exceções do repositório. `PriorityAdvisor` captura apenas os tipos de erro específicos previstos no código e usa a prioridade local como fallback. Os cenários caracterizam esses limites; não presumem mecanismos de recuperação não implementados.
