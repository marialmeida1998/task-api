# Cenários alternativos e erros

## Registro do segundo prompt

O texto abaixo é o segundo prompt utilizado, preservado como histórico de elaboração dos cenários. A referência à resiliência descreve o foco desses casos, não um requisito independente do projeto.

> Com base na análise anterior do projeto task-api, quero aprofundar a geração de casos de teste de integração com foco em falhas, exceções e resiliência.
>
> A análise identificou que a aplicação utiliza FastAPI, TaskService, TaskRepository e PriorityAdvisor, com integração opcional com OpenAI e fallback local.
>
> Já foram identificados os seguintes cenários de integração: IT-01 até IT-16. Portanto, não quero apenas repetir os casos anteriores.
>
> Gere novos cenários complementares, priorizando:
>
> 1. Falhas durante a comunicação com a OpenAI.
> 2. Retorno inesperado ou inválido da integração externa.
> 3. Acionamento do fallback local.
> 4. Garantia de que uma falha externa não impeça a criação de tarefas quando o fallback previsto pelo código puder atuar.
> 5. Tratamento de exceções nas operações entre serviço e repositório, quando houver comportamento implementado que possa ser verificado.
> 6. Integridade dos dados após operações que envolvam falhas.
> 7. Verificação de que tarefas não sejam criadas ou alteradas indevidamente quando uma operação falhar.
>
> REGRAS:
>
> - Leia novamente o código necessário para confirmar cada comportamento.
> - Não invente tratamento de exceções que não exista na aplicação.
> - Não invente endpoints ou regras de negócio.
> - Não repita os cenários IT-01 a IT-16.
> - Utilize pytest e TestClient, respeitando a estrutura de testes existente.
> - Simule chamadas externas para evitar dependência de uma API real da OpenAI.
> - Diferencie os cenários que podem ser automatizados daqueles que precisam apenas ser documentados.
> Para cada novo cenário, informe:
>
> - Identificador sequencial a partir de IT-17.
> - Nome.
> - Objetivo.
> - Pré-condições.
> - Dados de entrada.
> - Passos.
> - Resultado esperado.
> - Componentes envolvidos.
> - Justificativa de por que é um teste de integração.
>
> Ao final, apresente uma análise de como esses novos cenários complementam os 16 anteriores e quais ajustes no prompt ajudaram a obter resultados mais específicos e úteis.
>
> Não altere nenhum arquivo. Apenas apresente a análise e os novos casos de teste.

## Comportamento confirmado no código

`PriorityAdvisor` calcula primeiro a prioridade local. Com chave configurada, tenta a integração externa. Captura `HTTPError`, `URLError`, `TimeoutError`, `OSError` e `ValueError` (incluindo `JSONDecodeError`) e devolve o fallback local. Também usa fallback quando o parsing não encontra prioridade reconhecida. Outras exceções não são capturadas. Por exemplo, uma lista JSON no nível superior causa `AttributeError` quando o parser tenta chamar `.get`. `TaskService` não captura exceções do repositório. O repositório atual é em memória e não injeta falhas naturalmente; os casos de falha no repositório exigem um substituto de teste que falhe antes de mutar os dados.

Nos casos automatizáveis, simular `app.services.priority_advisor.urlopen`; não chamar o provedor real. Para respostas simuladas, fornecer `read()` e suporte a gerenciador de contexto. Use `TestClient(raise_server_exceptions=False)` para verificar resposta HTTP 500 em exceções não capturadas; sem isso, a exceção pode ser propagada ao teste.

### IT-17: Usar fallback após erro HTTP da OpenAI
- **Objetivo:** Verificar que erro HTTP capturado aciona fallback local sem impedir a criação.
- **Pré-condições:** Chave fictícia; `urlopen` simulado para lançar `HTTPError`; repositório vazio.
- **Dados de entrada:** Criar tarefa com termos locais de prioridade alta, como `Risco importante` e `Pode afetar o prazo da entrega`; prioridade enviada `media`.
- **Passos:** Enviar `POST /tasks`; consultar o ID retornado. Opcionalmente parametrizar `401` e `429`.
- **Resultado esperado:** `201`; prioridade `alta` na resposta e consulta; erro HTTP não é exposto.
- **Componentes envolvidos:** TestClient, rota, TaskService, PriorityAdvisor, transporte simulado e TaskRepository.
- **Justificativa de integração:** Verifica o erro externo, o fallback e o efeito na persistência e resposta HTTP.
- **Classificação:** Automatizável com simulação determinística.

### IT-18: Usar fallback após falha de conexão
- **Objetivo:** Verificar fallback para `URLError` ou `OSError` capturados.
- **Pré-condições:** Chave fictícia; `urlopen` simulado para lançar uma dessas exceções; repositório vazio.
- **Dados de entrada:** Criar tarefa com título `Incidente urgente` e descrição `Bloqueio no fluxo interno`.
- **Passos:** Enviar criação; consultar a tarefa.
- **Resultado esperado:** `201`; prioridade `critica` retornada e persistida.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor, transporte simulado e TaskRepository.
- **Justificativa de integração:** Observa recuperação de falha de comunicação ao longo do fluxo de criação.
- **Classificação:** Automatizável; pode parametrizar os tipos de exceção.

### IT-19: Usar fallback após timeout
- **Objetivo:** Verificar que `TimeoutError` capturado não interrompe a criação.
- **Pré-condições:** Chave fictícia; `urlopen` simulado para lançar `TimeoutError`; repositório vazio.
- **Dados de entrada:** Título `Melhoria sem urgencia`, descrição `Pode ser feita quando der`.
- **Passos:** Enviar criação; consultar a tarefa.
- **Resultado esperado:** `201`; prioridade local `baixa` persistida.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor, transporte simulado e TaskRepository.
- **Justificativa de integração:** Verifica tratamento de timeout e efeito no estado através do fluxo HTTP.
- **Classificação:** Automatizável com simulação.

### IT-20: Usar fallback após corpo JSON inválido
- **Objetivo:** Verificar falha de decodificação tratada pelo advisor.
- **Pré-condições:** Chave fictícia; resposta simulada cujo `read()` retorna bytes que não representam JSON; repositório vazio.
- **Dados de entrada:** Criar tarefa com `risco` no título ou descrição, sem termos críticos.
- **Passos:** Enviar `POST /tasks`; consultar a tarefa.
- **Resultado esperado:** `201`; `ValueError` de decodificação é capturado e prioridade local `alta` é persistida.
- **Componentes envolvidos:** TestClient, API, TaskService, PriorityAdvisor, resposta simulada e TaskRepository.
- **Justificativa de integração:** Exercita decodificação e fallback do advisor através da rota e persistência.
- **Classificação:** Automatizável com corpo de resposta simulado.

### IT-21: Usar fallback quando a resposta não contém prioridade reconhecida
- **Objetivo:** Verificar resposta JSON válida com saída não interpretável como prioridade.
- **Pré-condições:** Chave fictícia; HTTP 200 simulado com `{"output_text": "classificacao indisponivel"}`; repositório vazio.
- **Dados de entrada:** Criar tarefa com termos locais de prioridade alta e sem termos críticos.
- **Passos:** Enviar criação; consultar a tarefa.
- **Resultado esperado:** `201`; parser retorna `None` e advisor utiliza fallback local `alta`.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor, parsing simulado e TaskRepository.
- **Justificativa de integração:** Confirma a interpretação do retorno externo e o estado persistido entre componentes.
- **Classificação:** Automatizável com JSON simulado.

### IT-22: Receber JSON com estrutura superior inesperada
- **Objetivo:** Caracterizar JSON válido com estrutura incompatível com o parser atual.
- **Pré-condições:** Chave fictícia; HTTP 200 simulado com corpo `[]`; `TestClient(raise_server_exceptions=False)`.
- **Dados de entrada:** Requisição válida de criação.
- **Passos:** Enviar `POST /tasks`; depois chamar `GET /tasks`.
- **Resultado esperado:** `AttributeError` ao chamar `.get`; não é capturado e a resposta é `500`. A listagem permanece vazia porque a criação no repositório não foi alcançada.
- **Componentes envolvidos:** TestClient, rota, TaskService, PriorityAdvisor, resposta simulada e TaskRepository.
- **Justificativa de integração:** Verifica propagação e ausência de mutação entre parsing, serviço e repositório.
- **Classificação:** Automatizável como caracterização; não pressupõe que o comportamento seja desejável.

### IT-23: Falha HTTP externa durante atualização com repriorização
- **Objetivo:** Verificar que falha externa capturada não impede atualização que solicita prioridade automática.
- **Pré-condições:** Criar tarefa neutra; chave fictícia; `urlopen` simulado lançando `HTTPError`.
- **Dados de entrada:** `PUT /tasks/{id}` com título `Incidente urgente`, sem `priority`.
- **Passos:** Enviar atualização; consultar a tarefa.
- **Resultado esperado:** `200`; título atualizado, prioridade `critica` pelo fallback local e campos omitidos preservados conforme o repositório.
- **Componentes envolvidos:** API, TaskService, TaskRepository, PriorityAdvisor e transporte simulado.
- **Justificativa de integração:** Exercita busca, sugestão, fallback e persistência numa atualização HTTP.
- **Classificação:** Automatizável com simulação.

### IT-24: Exceção externa não capturada antes da criação
- **Objetivo:** Caracterizar exceção de transporte fora da lista capturada pelo advisor.
- **Pré-condições:** Chave fictícia; `urlopen` simulado lançando `RuntimeError`; `TestClient(raise_server_exceptions=False)`; repositório vazio.
- **Dados de entrada:** Payload válido de `POST /tasks`.
- **Passos:** Enviar criação; chamar `GET /tasks`.
- **Resultado esperado:** `500`; `RuntimeError` propaga. A listagem permanece vazia porque o serviço não chega a chamar `repository.create`.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor, transporte simulado e TaskRepository.
- **Justificativa de integração:** Verifica ordem de chamadas e estado após exceção externa não tratada.
- **Classificação:** Automatizável como caracterização com exceção injetada.

### IT-25: Exceção do repositório durante criação
- **Objetivo:** Caracterizar propagação na fronteira serviço–repositório e ausência de mutação parcial.
- **Pré-condições:** Repositório de teste cuja operação `create` lança `RuntimeError` antes de alterar o armazenamento; advisor sem chamada externa; `TestClient(raise_server_exceptions=False)`.
- **Dados de entrada:** Requisição válida de criação.
- **Passos:** Enviar `POST /tasks`; chamar `GET /tasks` no mesmo serviço isolado.
- **Resultado esperado:** `500`, pois serviço e rota não capturam a exceção; lista vazia porque o repositório de teste falhou antes da mutação.
- **Componentes envolvidos:** TestClient, rota, TaskService, PriorityAdvisor e repositório de teste.
- **Justificativa de integração:** Verifica chamada entre serviço e repositório e estado observável após falha injetada.
- **Classificação:** Automatizável com substituto; não é falha natural do repositório atual.

### IT-26: Exceção do repositório durante atualização
- **Objetivo:** Verificar que falha anterior à mutação preserva a tarefa original.
- **Pré-condições:** Criar tarefa; repositório de teste lança antes de aplicar `update`; prioridade explícita para evitar repriorização; `TestClient(raise_server_exceptions=False)`.
- **Dados de entrada:** `PUT /tasks/{id}` com título alterado e `priority: "alta"`.
- **Passos:** Guardar estado original; enviar atualização; consultar novamente.
- **Resultado esperado:** `500`; título, prioridade e timestamps permanecem iguais, pois a falha foi injetada antes da mutação.
- **Componentes envolvidos:** TestClient, rota, TaskService e repositório de teste.
- **Justificativa de integração:** Verifica atualização entre camadas e integridade após falha do repositório.
- **Classificação:** Automatizável com substituto; caracteriza propagação, não recuperação.

### IT-27: Exceção do repositório durante exclusão
- **Objetivo:** Verificar que falha antes da remoção não seja reportada como sucesso nem apague a tarefa.
- **Pré-condições:** Criar tarefa; repositório de teste lança antes de excluir; `TestClient(raise_server_exceptions=False)`.
- **Dados de entrada:** `DELETE /tasks/{id}` para tarefa existente.
- **Passos:** Enviar exclusão; consultar novamente pelo ID.
- **Resultado esperado:** `500`, não `204`; tarefa permanece consultável porque o substituto falhou antes da remoção.
- **Componentes envolvidos:** TestClient, rota, TaskService e repositório de teste.
- **Justificativa de integração:** Verifica propagação do erro e estado depois da falha injetada.
- **Classificação:** Automatizável com substituto; a falha não ocorre naturalmente no repositório atual.

### IT-28: Observar falha real do provedor em ambiente controlado
- **Objetivo:** Documentar comportamento operacional de falhas reais de provedor/configuração/rede sem incluir dependência ativa na suíte comum.
- **Pré-condições:** Ambiente não produtivo autorizado, chave/modelo configurados e meios para observar a resposta. Não registrar credenciais em logs ou documentação.
- **Dados de entrada:** Requisição válida de criação com integração externa habilitada.
- **Passos:** Executar chamada controlada; registrar status/corpo do provedor, exceção observada e resposta da API; identificar o tipo exato da exceção.
- **Resultado esperado:** Registrar somente observações. Tipos na lista capturada usam fallback; outros podem propagar. Não existe resposta universal sem especificar provedor e ambiente.
- **Componentes envolvidos:** Cliente HTTP, FastAPI, TaskService, PriorityAdvisor, configuração de ambiente, TaskRepository e OpenAI.
- **Justificativa de integração:** Observa comunicação e configuração reais além do que uma simulação local comprova.
- **Classificação:** Apenas documental/operacional; depende de ambiente externo e não é determinístico para a suíte automatizada comum.

## Complementaridade e situação

IT-17 a IT-28 complementam IT-01 a IT-16 sem repetir CRUD básico e validações de entrada. Diferenciam falhas externas capturadas com fallback, saída não reconhecida, exceções não capturadas e falhas injetadas no repositório; também verificam o estado após erros. São propostas: não foram implementadas nem executadas aqui.
