# Análise de Requisitos – Recomendação de Artefatos de Especificação

## Introdução

Esta análise foi elaborada exclusivamente com base nas histórias de usuário identificadas no projeto. As recomendações consideram as funcionalidades existentes da Task API: criação, listagem, consulta, atualização, remoção de tarefas e priorização assistida, incluindo o comportamento de fallback quando a integração com IA não estiver disponível.

## 1. Tabela de artefatos

| Artefato | Recomenda? | Prioridade | Justificativa |
|---|---|---|---|
| Critérios de Aceitação | Sim | Alta | São fundamentais para transformar as histórias de usuário em critérios objetivos de validação, principalmente para as operações CRUD e para o comportamento de priorização. |
| Casos de Uso | Sim | Alta | O projeto possui funcionalidades bem delimitadas e recorrentes, o que torna este artefato adequado para representar os cenários principais do sistema. |
| Matriz de Perfis e Permissões (RBAC) | Não | Baixa | O projeto atual não implementa autenticação, autorização ou perfis de usuário, portanto esse artefato não é prioritário no estado atual do MVP. |
| Especificação de Requisitos Não Funcionais | Sim | Alta | O projeto apresenta limitações explícitas relacionadas a persistência, documentação, testes e operação, o que justifica a documentação desses requisitos. |
| Protótipos | Não | Média | Podem ser úteis em uma fase futura, mas não são essenciais para uma API backend sem interface gráfica. |
| Diagrama de Casos de Uso | Sim | Alta | Ajuda a visualizar os atores, as funcionalidades principais e o escopo do sistema de forma clara. |
| Diagrama de Sequência UML | Sim | Média | Pode apoiar a compreensão do fluxo entre rotas, serviço, repositório e componente de priorização, principalmente nas operações de criação e atualização. |
| Matriz de Rastreabilidade | Sim | Alta | É especialmente útil para conectar histórias de usuário, regras de negócio, requisitos e testes em um projeto acadêmico. |
| DER | Não | Baixa | O sistema não possui banco de dados implementado nem um modelo persistente formal, o que torna este artefato pouco prioritário no momento. |
| BPMN | Não | Média | Pode ser relevante para ilustrar o fluxo de gestão de tarefas, mas o projeto não apresenta processos de negócio complexos o bastante para justificar prioridade alta. |
| Diagrama de Estados | Sim | Alta | O sistema trabalha com estados explícitos de tarefa, como pendente, em_andamento, concluida e cancelada, o que torna esse artefato altamente pertinente. |

## 2. Explicação detalhada dos artefatos recomendados

### Critérios de Aceitação
Os critérios de aceitação são recomendados porque as histórias de usuário do projeto descrevem claramente o que o sistema deve fazer, mas precisam de uma forma objetiva de validação. Eles ajudam a confirmar se uma tarefa criada, consultada, atualizada ou removida atende ao comportamento esperado, além de apoiar a validação do comportamento de priorização.

### Casos de Uso
Os casos de uso são importantes porque as funcionalidades do sistema são bem estruturadas em torno de ações específicas do usuário. Eles permitem descrever, de forma organizada, os cenários de criação, consulta, atualização, remoção e priorização das tarefas, facilitando a compreensão do escopo funcional.

### Especificação de Requisitos Não Funcionais
Este artefato merece prioridade alta porque o projeto já evidencia limitações não funcionais importantes, como persistência em memória, ausência de autenticação e autorização, ausência de paginação e dependência de configuração de ambiente. Essas características precisam ser registradas para evitar ambiguidades futuras.

### Diagrama de Casos de Uso
O diagrama de casos de uso é adequado porque oferece uma visão visual do escopo funcional do sistema. Ele é particularmente útil para mostrar os atores envolvidos e as funcionalidades principais da API, especialmente em contexto acadêmico.

### Diagrama de Sequência UML
Este artefato pode ser útil para demonstrar a interação entre os componentes da aplicação em cenários de criação e atualização de tarefas. Embora não seja o primeiro artefato a ser produzido, ele agrega valor para a compreensão da arquitetura interna do sistema.

### Matriz de Rastreabilidade
A matriz de rastreabilidade é altamente recomendada porque permite ligar histórias de usuário a requisitos, regras de negócio e testes. Isso é especialmente benéfico em projetos acadêmicos, pois ajuda a demonstrar como as funcionalidades foram derivadas e validadas.

### Diagrama de Estados
O diagrama de estados é relevante porque o projeto envolve estados explícitos de tarefa, e isso aparece diretamente nas histórias de usuário e nas regras de negócio. Ele é útil para documentar as transições entre pendente, em_andamento, concluida e cancelada.

## 3. Artefatos não priorizados e seus motivos

### Matriz de Perfis e Permissões (RBAC)
Não é prioritária porque o projeto atual não define autenticação, autorização ou papéis de usuário. As histórias analisadas não indicam necessidade de controle de acesso por perfil.

### Protótipos
Não são priorizados neste momento porque o projeto é uma API backend e as histórias de usuário se concentram em comportamento funcional, regras de negócio e integração, não em interface visual.

### DER
Não é prioritário porque o sistema não implementa persistência relacional nem um modelo de dados formal em banco de dados. O estado atual do projeto é orientado à lógica de serviço e repositório em memória.

### BPMN
Não é priorizado com alta relevância porque o projeto não apresenta fluxo de negócio complexo ou processual suficiente para justificar a produção imediata desse artefato.

## 4. Se eu pudesse escolher apenas dois artefatos

Os dois artefatos mais importantes para este projeto são:

1. Casos de Uso
2. Critérios de Aceitação

Esses dois artefatos formam a base mais sólida para especificar o comportamento esperado da API. Os casos de uso ajudam a estruturar as funcionalidades principais, enquanto os critérios de aceitação permitem transformar as histórias de usuário em validações objetivas e verificáveis.

## 5. Recomendação resumida — próximos passos

Os artefatos que devem ser produzidos primeiro são:

1. Casos de Uso
2. Critérios de Aceitação
3. Diagrama de Estados
4. Especificação de Requisitos Não Funcionais
5. Matriz de Rastreabilidade

Essa ordem prioriza os artefatos que melhor sustentam a compreensão funcional do sistema, a validação das histórias de usuário e a documentação das restrições operacionais do projeto.
