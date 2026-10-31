# Cenários de integração

## Registro do primeiro prompt

O texto abaixo é o prompt originalmente utilizado, preservado como histórico do processo de elaboração dos cenários. A menção contextual ao uso acadêmico faz parte do prompt, não do posicionamento deste repositório.

> Analise o projeto task-api aberto neste workspace do VS Code, considerando que estou realizando uma atividade acadêmica sobre o uso de Engenharia de Prompt e IA Generativa para apoiar testes de integração.
>
> O projeto é uma API REST em Python com FastAPI, organizada em camadas.
>
> Quero uma análise focada em testes de integração.
>
> 1. Leia as rotas, serviços, repositórios, modelos e testes existentes.
> 2. Identifique como ocorre a comunicação entre as camadas.
> 3. Identifique os principais fluxos de integração.
> 4. Verifique quais cenários ainda não estão cobertos pelos testes existentes.
> 5. Considere criação, consulta, atualização e exclusão de tarefas.
> 6. Considere validações, comunicação entre Service e Repository e integração com PriorityAdvisor.
> 7. Considere os cenários de sucesso e de erro.
> Não altere nenhum arquivo e não implemente funcionalidades.
>
> Não invente endpoints ou regras de negócio. Utilize apenas o comportamento encontrado no código.
>
> Ao final, apresente pelo menos 10 sugestões de casos de teste de integração. Para cada caso, informe identificador, objetivo, pré-condições, passos e resultado esperado.

## Objetivo e fluxo observado

O prompt solicitou cenários fundamentados no código para os fluxos CRUD, validações, comunicação entre camadas e `PriorityAdvisor`. As rotas validam dados e delegam ao `TaskService`; o serviço usa o `TaskRepository` em memória e chama o advisor quando aplicável. O repositório gera UUID e timestamps, define `pendente` na criação e preserva campos omitidos na atualização. Para registros ausentes, as rotas retornam `404`; erros de validação retornam `422`. O advisor aplica heurísticas locais e, se `OPENAI_API_KEY` estiver configurada, tenta a integração externa.

Os casos abaixo são propostas, não resultados de execução. Para testes HTTP, usar `pytest` e `TestClient` com serviço e repositório isolados. Simular chamadas ao LLM para não depender de rede real.

### IT-01: Criar tarefa com prioridade crítica
- **Objetivo:** Verificar se a classificação crítica local aparece na resposta e na tarefa armazenada.
- **Pré-condições:** Repositório isolado vazio; chamada externa desabilitada ou simulada.
- **Dados de entrada:** `POST /tasks`, título `Incidente urgente`, descrição `Bloqueio critico em producao`, prioridade enviada `media`.
- **Passos:** Criar a tarefa e consultar o ID retornado.
- **Resultado esperado:** `201`; prioridade `critica` na resposta e consulta, status inicial `pendente`.
- **Componentes envolvidos:** TestClient, rota, modelos, TaskService, PriorityAdvisor e TaskRepository.
- **Justificativa de integração:** Liga validação HTTP, advisor, persistência e consulta posterior.

### IT-02: Criar tarefa com prioridade alta
- **Objetivo:** Verificar a classificação local alta no fluxo de criação.
- **Pré-condições:** Repositório vazio; chamada externa desabilitada ou simulada.
- **Dados de entrada:** Título `Ajuste importante`; descrição `Existe risco de perder o prazo`.
- **Passos:** Criar a tarefa e consultá-la pelo ID.
- **Resultado esperado:** `201`; prioridade `alta` na resposta e na consulta.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor e TaskRepository.
- **Justificativa de integração:** Confirma que o resultado do advisor passa pelo serviço e é persistido.

### IT-03: Criar tarefa com prioridade baixa
- **Objetivo:** Verificar classificação local baixa e persistência.
- **Pré-condições:** Repositório vazio; chamada externa desabilitada ou simulada.
- **Dados de entrada:** Título `Melhoria sem urgencia`; descrição `Pode ser feita quando der`; prioridade enviada `media`.
- **Passos:** Criar a tarefa e consultá-la.
- **Resultado esperado:** `201`; prioridade `baixa` na resposta e na tarefa armazenada.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor e TaskRepository.
- **Justificativa de integração:** Observa a saída da heurística atravessando serviço e persistência.

### IT-04: Aplicar prioridade do LLM durante a criação
- **Objetivo:** Verificar que o resultado do LLM é usado pelo serviço e repositório.
- **Pré-condições:** Chave fictícia; simular o método do advisor para retornar `TaskPriority.CRITICAL`; repositório vazio.
- **Dados de entrada:** Título `Tarefa simples`, descrição `Sem termos de prioridade local`, prioridade enviada `baixa`.
- **Passos:** Criar a tarefa e consultá-la pelo ID.
- **Resultado esperado:** `201`; prioridade `critica` na resposta e no registro.
- **Componentes envolvidos:** TestClient, rota, TaskService, PriorityAdvisor simulado e TaskRepository.
- **Justificativa de integração:** Verifica a integração da saída do advisor ao fluxo HTTP e à persistência, sem chamada real ao provedor.

### IT-05: Usar fallback local quando a chamada ao LLM falha
- **Objetivo:** Confirmar que uma falha externa capturada não impede a criação.
- **Pré-condições:** Chave fictícia; simular `_suggest_with_llm` lançando `TimeoutError`; repositório vazio.
- **Dados de entrada:** Título `Risco importante`, descrição `Pode afetar o prazo da entrega`, prioridade inicial `media`.
- **Passos:** Enviar criação pela API e consultar a tarefa.
- **Resultado esperado:** `201`; prioridade local `alta` na resposta e persistida; timeout não é propagado ao cliente.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor e TaskRepository.
- **Justificativa de integração:** Exercita o fallback dentro do fluxo de criação e verifica seu efeito no estado.

### IT-06: Listar tarefas com repositório vazio
- **Objetivo:** Verificar resposta de coleção vazia.
- **Pré-condições:** Repositório isolado vazio.
- **Dados de entrada:** `GET /tasks`.
- **Passos:** Enviar a requisição de listagem.
- **Resultado esperado:** `200` e lista vazia.
- **Componentes envolvidos:** TestClient, rota de listagem, TaskService e TaskRepository.
- **Justificativa de integração:** Verifica delegação e serialização do resultado vazio do repositório.

### IT-07: Listar tarefas criadas
- **Objetivo:** Verificar que tarefas criadas pela API aparecem na listagem.
- **Pré-condições:** Repositório isolado.
- **Dados de entrada:** Duas criações com títulos diferentes.
- **Passos:** Criar as duas tarefas; chamar `GET /tasks`.
- **Resultado esperado:** `200`; lista contém as duas tarefas e seus IDs.
- **Componentes envolvidos:** TestClient, rotas de criação e listagem, TaskService e TaskRepository.
- **Justificativa de integração:** Combina endpoints e verifica estado compartilhado no repositório.

### IT-08: Atualizar parcialmente e preservar campos omitidos
- **Objetivo:** Verificar que campos omitidos permanecem inalterados.
- **Pré-condições:** Criar tarefa com descrição, prioridade e responsável conhecidos.
- **Dados de entrada:** `PUT /tasks/{id}` contendo somente um novo título.
- **Passos:** Guardar resposta original; atualizar; consultar a tarefa.
- **Resultado esperado:** `200`; título atualizado, campos omitidos e `created_at` preservados; `updated_at` não anterior ao original.
- **Componentes envolvidos:** API, `TaskUpdate`, TaskService e TaskRepository.
- **Justificativa de integração:** Confirma o contrato de atualização e o comportamento `exclude_unset` do repositório.

### IT-09: Recalcular prioridade automaticamente na atualização
- **Objetivo:** Verificar que atualização sem prioridade explícita aciona o advisor e persiste sua sugestão.
- **Pré-condições:** Criar tarefa neutra; chamada externa desabilitada ou simulada.
- **Dados de entrada:** `PUT /tasks/{id}` alterando o título para conter `urgente`, sem `priority`.
- **Passos:** Atualizar e consultar a tarefa.
- **Resultado esperado:** `200`; novo título e prioridade `critica` persistidos.
- **Componentes envolvidos:** API, TaskService, PriorityAdvisor e TaskRepository.
- **Justificativa de integração:** Exercita busca do estado atual, sugestão e atualização do registro numa requisição.

### IT-10: Respeitar prioridade explícita na atualização
- **Objetivo:** Verificar que prioridade informada é aplicada sem repriorização automática.
- **Pré-condições:** Criar tarefa; instrumentar `suggest_update` para detectar chamadas.
- **Dados de entrada:** `PUT /tasks/{id}` com `priority: "alta"`.
- **Passos:** Atualizar e consultar a tarefa; verificar se `suggest_update` foi invocado.
- **Resultado esperado:** `200`; prioridade `alta` persistida; `suggest_update` não é chamado pelo serviço.
- **Componentes envolvidos:** TestClient, rota, TaskService, PriorityAdvisor instrumentado e TaskRepository.
- **Justificativa de integração:** Verifica a decisão do serviço e o resultado persistido via API.

### IT-11: Atualizar com objeto vazio
- **Objetivo:** Caracterizar atualização sem campos informados.
- **Pré-condições:** Criar tarefa e guardar sua resposta.
- **Dados de entrada:** `PUT /tasks/{id}` com `{}`.
- **Passos:** Enviar atualização e consultar a tarefa.
- **Resultado esperado:** `200`; campos funcionais permanecem iguais. O repositório define novo `updated_at`, não anterior ao original.
- **Componentes envolvidos:** API, `TaskUpdate`, TaskService e TaskRepository.
- **Justificativa de integração:** Verifica a interação entre modelo, serviço e atualização parcial do repositório.

### IT-12: Não chamar o advisor ao atualizar ID inexistente
- **Objetivo:** Confirmar que o serviço retorna ausência antes de pedir sugestão.
- **Pré-condições:** UUID válido ausente do repositório; advisor instrumentado.
- **Dados de entrada:** `PUT /tasks/{id}` com novo título e sem prioridade.
- **Passos:** Enviar atualização e observar a chamada a `suggest_update`.
- **Resultado esperado:** `404` com detalhe `Task not found`; advisor não é chamado porque a busca no repositório retorna `None`.
- **Componentes envolvidos:** API, TaskService, TaskRepository e PriorityAdvisor instrumentado.
- **Justificativa de integração:** Verifica a ordem das chamadas entre serviço, repositório e advisor e a tradução HTTP da ausência.

### IT-13: Confirmar remoção em consultas posteriores
- **Objetivo:** Verificar o estado depois da exclusão bem-sucedida.
- **Pré-condições:** Criar tarefa.
- **Dados de entrada:** ID retornado pela criação.
- **Passos:** Enviar `DELETE /tasks/{id}`; consultar pelo ID; listar tarefas.
- **Resultado esperado:** Exclusão retorna `204` sem corpo; consulta retorna `404`; listagem não contém a tarefa removida.
- **Componentes envolvidos:** API, TaskService e TaskRepository.
- **Justificativa de integração:** Confirma exclusão e estado resultante por meio de endpoints distintos.

### IT-14: Rejeitar UUID malformado na rota
- **Objetivo:** Verificar que UUID inválido é rejeitado antes da consulta ao serviço.
- **Pré-condições:** Nenhuma.
- **Dados de entrada:** `GET /tasks/not-a-uuid`.
- **Passos:** Enviar requisição; opcionalmente instrumentar o serviço para verificar se foi chamado.
- **Resultado esperado:** `422`; consulta não chega ao serviço/repositório.
- **Componentes envolvidos:** TestClient, roteamento FastAPI e conversão de UUID.
- **Justificativa de integração:** Verifica o contrato HTTP e o limite entre validação do caminho e execução da aplicação.

### IT-15: Rejeitar campos de criação acima dos limites
- **Objetivo:** Verificar limites declarados em `TaskCreate`.
- **Pré-condições:** Repositório vazio.
- **Dados de entrada:** Casos separados/parametrizados com título acima de 120 caracteres, descrição acima de 1000 ou responsável acima de 120.
- **Passos:** Enviar cada payload por `POST /tasks`; verificar listagem.
- **Resultado esperado:** Cada payload retorna `422`; nenhuma tarefa inválida é persistida.
- **Componentes envolvidos:** TestClient, FastAPI, `TaskCreate` e TaskRepository.
- **Justificativa de integração:** Verifica que a validação na fronteira HTTP impede gravação no repositório.

### IT-16: Definir descrição como nula durante repriorização automática
- **Objetivo:** Caracterizar a interação entre `null` explícito, persistência e dados considerados pelo advisor.
- **Pré-condições:** Sem chave; criar tarefa com descrição contendo `risco`, resultando em prioridade local `alta`.
- **Dados de entrada:** `PUT /tasks/{id}` com `description: null`, sem `priority`.
- **Passos:** Enviar atualização e consultar a tarefa.
- **Resultado esperado conforme o código atual:** `200`; descrição é persistida como nula. `suggest_update` trata `None` como ausência e usa a descrição anterior para sugerir, mantendo a prioridade `alta`. É caracterização, não regra de negócio inferida.
- **Componentes envolvidos:** API, `TaskUpdate`, TaskService, PriorityAdvisor e TaskRepository.
- **Justificativa de integração:** Verifica a diferença entre o `null` enviado à persistência e o valor utilizado pelo advisor.

## Situação

Os 16 cenários foram propostos a partir da análise do código. Não foram implementados nem executados aqui.
