# Análise dos prompts

## Escopo

Dois prompts foram utilizados em sequência para propor cenários de integração para a implementação atual do `task-api`. Os textos estão preservados literalmente em [Cenários de integração](integration-scenarios.md) e [Cenários alternativos e erros](alternative-scenarios-and-errors.md), como histórico de elaboração. A contextualização original dos prompts não define o propósito ou posicionamento deste repositório.

A comparação trata da especificidade e diversidade das propostas. IT-01 a IT-28 não foram implementados nem executados; portanto, não há afirmação empírica sobre eficácia de testes.

## Prompt 1: cobertura de integração de referência

O primeiro prompt definiu escopo amplo, mas ancorado no código: ler rotas, serviços, repositórios, modelos e testes; identificar a comunicação entre camadas; considerar criação, consulta, atualização, exclusão, validações e cenários de sucesso e erro. Também proibiu inventar endpoints e regras de negócio.

Esse direcionamento originou IT-01 a IT-16: prioridades na criação, simulação de prioridade do LLM, fallback, listagem vazia e populada, atualização parcial, repriorização automática e explícita, ausência de chamada ao advisor para ID inexistente, integridade após exclusão, UUID malformado, limites dos modelos e caracterização de `null` explícito. O conjunto oferece amplitude funcional e relaciona resultados das camadas com respostas HTTP e estado no repositório.

## Prompt 2: comportamentos alternativos e falhas

O segundo prompt informou explicitamente a sequência existente IT-01 a IT-16 e solicitou novos casos a partir de IT-17. Priorizou falhas na comunicação externa, respostas inesperadas, fallback local, exceções entre serviço e repositório e integridade dos dados. Exigiu releitura do código, proibiu pressupor tratamento de exceções inexistente, solicitou simulações externas e definiu os campos a registrar em cada caso, além da distinção entre automatizável e documental.

Esses ajustes produziram IT-17 a IT-28: erros HTTP, conexão, timeout e decodificação cobertos pelo fallback; resposta sem prioridade reconhecida; estrutura JSON superior incompatível; atualização com falha externa; exceção externa não capturada; falhas injetadas no repositório antes de mutar em criação/atualização/exclusão; e observação operacional com provedor real. A exigência de substitutos e configuração de `TestClient` torna os casos mais reproduzíveis e distingue recuperação implementada de erro que apenas propaga.

## Comparação de qualidade e diversidade

O primeiro prompt oferece maior amplitude funcional. Os casos acompanham operações CRUD, validação, decisões de prioridade e estado após operações. Seu principal valor está em mapear operações expostas pela API à estrutura real de camadas.

O segundo prompt aprofunda os caminhos de falha. Separa exceções capturadas pelo advisor com fallback, respostas válidas sem prioridade interpretável e exceções que escapam ao tratamento atual. Também torna explícita a verificação do estado após a falha. A diversidade abrange transporte externo, decodificação/parsing, fronteira serviço–repositório e uma observação operacional dependente de ambiente.

Os prompts são complementares: o primeiro estabelece cobertura funcional de referência e o segundo adiciona caracterização de erros. A proibição de repetir cenários e a exigência de sequência preservaram os identificadores IT-01 a IT-28.

## Automatização e limites

- IT-01 a IT-16 são propostas para `pytest` e `TestClient`, com repositório em memória isolado. Chamadas externas devem ser desabilitadas ou simuladas.
- IT-17 a IT-24 podem ser automatizados com `urlopen` simulado em `app.services.priority_advisor`; respostas falsas devem suportar gerenciador de contexto e `read()`. Para afirmar resposta HTTP 500 em exceções não capturadas, usar `raise_server_exceptions=False`.
- IT-25 a IT-27 exigem repositório de teste que lança antes da mutação. Caracterizam a propagação atual e o estado sob falha injetada; o repositório em memória atual não produz esses erros naturalmente.
- IT-28 depende de ambiente externo autorizado e configurado e deve ser registrado como observação operacional, não como teste automatizado determinístico.

## Restrições de interpretação

1. `TaskRepository` usa dicionário em memória; não se presume banco externo nem comportamento transacional.
2. `TaskService` não captura exceções do repositório e as rotas não definem handler próprio para exceções arbitrárias. A resposta HTTP 500 é observável com `TestClient(raise_server_exceptions=False)`; por padrão, a exceção pode ser lançada ao teste.
3. `PriorityAdvisor` captura somente os tipos de exceção indicados na implementação. O fallback não deve ser generalizado para qualquer falha.
4. Uma lista JSON no nível superior é JSON válido, mas incompatível com o uso de `.get` no advisor e pode causar `AttributeError` não capturado. `RuntimeError` também está fora da lista capturada.
5. Os testes de falha do repositório precisam injetar a exceção antes da mutação para justificar a expectativa de estado inalterado.
6. Não se inferem regras de transição de status, autenticação, autorização, filtros, persistência externa ou funcionalidades não implementadas.

## Conclusão

Os refinamentos entre os prompts aumentaram a utilidade ao delimitar escopo, preservar identificadores prévios, exigir afirmações sobre exceções apoiadas no código, especificar simulação determinística da dependência externa e solicitar verificação do estado após falhas. Em conjunto, os prompts produzem uma linha de base funcional e propostas complementares de caminhos de erro, sem apresentar comportamento não implementado como funcionalidade existente nem afirmar que os testes foram executados.
