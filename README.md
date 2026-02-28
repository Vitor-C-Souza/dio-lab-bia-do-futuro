# 🤖 Financeiro Amigo Markin - Agente IA para Consultoria Financeira

Um agente financeiro inteligente baseado em IA Generativa que oferece **consultoria personalizada**, análise de investimentos e planejamento financeiro de forma proativa e acessível.

## 🎯 O que é o Markin?

**Markin** é um assistente virtual amigável e educativo que ajuda clientes a compreenderem suas finanças pessoais, otimizarem seus investimentos e tomarem decisões financeiras bem informadas. Diferente de chatbots tradicionais, Markin:

- 🎯 **Antecipa necessidades** com base no perfil e histórico do cliente
- 💰 **Personaliza recomendações** de investimentos e produtos financeiros
- 📊 **Analisa dados em tempo real** (transações, portfolio, objetivos)
- 🛡️ **Garante confiabilidade** com base de conhecimento estruturada (anti-alucinação)
- 🤝 **Adota tom consultivo** - educacional sem ser técnico demais

---

## 🏗️ Projeto Completo - Entregas

### 1. 📋 Documentação do Agente
Especificação completa de como Markin funciona:
- **Caso de Uso:** Consultoria de investimentos e planejamento financeiro para clientes PF
- **Persona:** Tom amigável, consultivo e educativo
- **Arquitetura:** Integração com base de conhecimento estruturada
- **Segurança:** Sistema de prompts controlado para evitar alucinações

👉 Veja [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. 📊 Base de Conhecimento Estruturada
Dados mockados realistas para criar contexto rico:

| Arquivo | Descrição |
|---------|-----------|
| `perfil_investidor.json` | Perfil, objetivos e tolerância ao risco |
| `transacoes.csv` | Histórico completo de transações |
| `historico_atendimento.csv` | Registro de interações anteriores |
| `produtos_financeiros.json` | Catálogo de produtos e serviços |

👉 Veja [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. 💬 Engenharia de Prompts
Prompts otimizados para precisão e segurança:
- **System Prompt:** Comportamento, restrições e diretrizes éticas
- **Exemplos Reais:** Cenários práticos de consultoria
- **Tratamento de Edge Cases:** Como lidar com perguntas fora do escopo

👉 Veja [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. 💻 Aplicação Funcional
Implementação em Python com montagem completa do contexto:

```python
# src/app.py - Montagem do contexto para o agente
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
```

👉 Veja [`src/app.py`](./src/app.py)

---

### 5. 📈 Avaliação e Métricas
Framework de avaliação da qualidade:
- **Precisão** das recomendações vs. perfil do cliente
- **Segurança** - taxa de respostas sem alucinações
- **Coerência** - alinhamento com histórico e objetivos

👉 Veja [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. 🎤 Pitch - Elevador
Apresentação estratégica de 3 minutos do projeto

👉 Veja [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## 🛠️ Stack Tecnológico

| Camada | Tecnologias |
|--------|-------------|
| **Backend/Runtime** | Python 3.8+ |
| **LLMs** | ChatGPT, Claude, Gemini, Ollama (via API) |
| **Framework Web** | Streamlit, Gradio ou FastAPI |
| **Orquestração** | LangChain, LangFlow, CrewAI |
| **Dados** | Pandas, JSON |
| **Documentação** | Mermaid, Draw.io |

---

## 📁 Estrutura do Projeto

```
📁 dio-lab-bia-do-futuro/
│
├── 📄 README.md                      # Este arquivo
│
├── 📁 src/                           # Código da aplicação
│   ├── app.py                        # Montagem do contexto e integração
│   └── README.md                     # Instruções técnicas
│
├── 📁 data/                          # Base de conhecimento mockada
│   ├── perfil_investidor.json        # Perfil e preferências do cliente
│   ├── produtos_financeiros.json     # Catálogo de produtos
│   ├── transacoes.csv                # Histórico de transações
│   ├── historico_atendimento.csv     # Histórico de interações
│   └── README.md                     # Descrição dos dados
│
├── 📁 docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md     # Caso de uso, persona, arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados e contexto
│   ├── 03-prompts.md                 # System prompt e exemplos
│   ├── 04-metricas.md                # Avaliação de qualidade
│   └── 05-pitch.md                   # Apresentação executiva
│
├── 📁 assets/                        # Imagens e diagramas
│   ├── README.md                     # Guia do laboratório
│   └── RoteiroLab.md                 # Roadmap de desenvolvimento
│
└── 📁 examples/                      # Exemplos de implementação
    └── README.md                     # Referências práticas
```

---

## ✨ Funcionalidades Principais

### 🎯 Análise Personalizada
- Avalia o perfil de risco do cliente (conservador, moderado, agressivo)
- Analisa histórico de transações e gastos
- Identifica padrões de comportamento financeiro

### 💡 Recomendações Inteligentes
- Sugestões de produtos alinhadas ao perfil
- Alertas sobre gastos excessivos
- Oportunidades de investimento personalizadas

### 📚 Educação Financeira
- Explica conceitos de forma acessível
- Responde dúvidas sobre produtos financeiros
- Ajuda no planejamento de metas

### 🛡️ Confiabilidade
- Respostas baseadas apenas em dados disponíveis
- Sistema de prompts controlado (zero alucinações)
- Histórico de interações rastreável

---

## 🚀 Como Usar

### 1. Preparar o Ambiente
```bash
pip install pandas
```

### 2. Estruturar o Contexto
```python
from src.app import contexto
# contexto contém todos os dados necessários para o agente
```

### 3. Integrar com LLM
Utilize qualquer LLM via API:
- **OpenAI GPT-4:** Melhor custo-benefício para produção
- **Claude:** Excelente para análise de documentos
- **Gemini:** Bom custo-benefício
- **Ollama:** Para modelos locais (privacidade)

---

## 📖 Dicas de Implementação

1. **Comece pelo system prompt:** Um bom prompt é a base de tudo
2. **Use dados mockados:** Garante consistência e funciona offline
3. **Teste cenários de edge case:** Perguntas fora do escopo ou ambíguas
4. **Valide respostas:** Compare com o perfil esperado do cliente
5. **Itere rápido:** Use exemplos reais de clientes para melhorar

---

## 📝 Licença

Este projeto foi desenvolvido como laboratório de inovação em IA para o setor financeiro.

---

## 📞 Mais Informações

Para detalhes técnicos completos, consulte a documentação em [`docs/`](./docs/).
