# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Qual a sua função no agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Determinar o perfil do cliente para recomendações |
| `produtos_financeiros.json` | JSON | Sugestões de produtos financeiros adequados ao perfil do cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não, os dados foram utilizados conforme fornecidos, sem alterações. Eles foram suficientes para criar um contexto rico para o agente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O agente carrega os dados no início de cada sessão, utilizando bibliotecas como `pandas` para CSV e `json` para arquivos JSON. Os dados são armazenados em variáveis de contexto que o agente pode acessar durante a interação.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são consultados dinamicamente durante a interação. O agente utiliza as informações para personalizar as respostas, oferecendo recomendações e insights baseados no perfil e histórico do cliente.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
