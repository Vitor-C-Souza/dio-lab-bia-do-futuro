import json
import pandas as pd
from dotenv import load_dotenv
import os
from google import genai
import streamlit as st

# Carregar chaves e configurar Gemini
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# --- CARREGAMENTO DA BASE DE CONHECIMENTO ---
# Usando os arquivos que você forneceu para garantir que o Markin saiba de quem fala
perfil = json.loads(open('./data/perfil_investidor.json', encoding='utf-8').read())
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.loads(open('./data/produtos_financeiros.json', encoding='utf-8').read())

# --- CONTEXTO E ANTI-ALUCINAÇÃO (SYSTEM PROMPT) ---
# Adicionamos regras rígidas para o Markin não inventar dados ou recomendar ações específicas.
SYSTEM_PROMPT = f"""
Você é o "Financeiro Amigo Markin". Sua base de conhecimento é restrita aos dados abaixo.

REGRAS RÍGIDAS:
1. Some TODOS os valores de uma categoria antes de responder sobre gastos.
2. Não ignore transações antigas; use o histórico completo fornecido.
3. Se houver mais de um gasto na mesma categoria (ex: alimentação), mencione todos ou o total somado.

CONTEXTO ATUAL:
- CLIENTE: {perfil['nome']}
- PATRIMÔNIO: R$ {perfil['patrimonio_total']}
- RESERVA: R$ {perfil['reserva_emergencia_atual']}
- HISTÓRICO COMPLETO DE TRANSAÇÕES:
{transacoes.to_dict(orient='records')} 
"""

def perguntar(msg):
    prompt_completo = f"{SYSTEM_PROMPT}\n\nPergunta do Usuário: {msg}"

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt_completo
    )
    return response.text

# --- INTERFACE STREAMLIT ---
st.set_page_config(page_title="Amigo Markin", page_icon="💰")

# Sidebar com Dashboard em tempo real baseado nos seus CSVs
with st.sidebar:
    st.header(f"📊 Resumo de {perfil['nome']}")
    st.metric("Patrimônio", f"R$ {perfil['patrimonio_total']}")
    
    # Gráfico rápido de Gastos por Categoria (Anti-Alucinação Visual)
    st.subheader("Gastos por Categoria")
    gastos = transacoes[transacoes['valor'] < 0].groupby('categoria')['valor'].sum().abs()
    st.bar_chart(gastos)

st.title("💰 O Financeiro Amigo Markin")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"Olá! Sou o Markin. Vi aqui que seu objetivo é {perfil['objetivo_principal']}. Como posso te ajudar hoje?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pergunta := st.chat_input("Ex: 'Vale a pena investir em Renda Fixa?'"):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Consultando sua carteira..."):
            resposta = perguntar(pergunta)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})