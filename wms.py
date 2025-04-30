import streamlit as st
from datetime import datetime

# Simulação de banco de dados em memória
if 'estoque' not in st.session_state:
    st.session_state.estoque = {}
if 'movimentacoes' not in st.session_state:
    st.session_state.movimentacoes = []

# Funções de negócio
def cadastrar_produto(codigo, nome, localizacao):
    if codigo in st.session_state.estoque:
        st.warning("Produto já cadastrado.")
        return
    st.session_state.estoque[codigo] = {
        "nome": nome,
        "localizacao": localizacao,
        "quantidade": 0
    }
    st.success(f"Produto '{nome}' cadastrado com sucesso!")

def movimentar_estoque(codigo, tipo, quantidade):
    if codigo not in st.session_state.estoque:
        st.error("Produto não encontrado.")
        return
    if tipo == "Saída" and st.session_state.estoque[codigo]["quantidade"] < quantidade:
        st.error("Estoque insuficiente.")
        return

    if tipo == "Entrada":
        st.session_state.estoque[codigo]["quantidade"] += quantidade
    else:
        st.session_state.estoque[codigo]["quantidade"] -= quantidade

    st.session_state.movimentacoes.append({
        "data": datetime.now(),
        "codigo": codigo,
        "tipo": tipo,
        "quantidade": quantidade
    })
    st.success(f"{tipo} registrada com sucesso.")

# Interface Streamlit
st.title("📦 Sistema WMS (Warehouse Management System)")

aba = st.sidebar.radio("Navegar para:", ["Cadastrar Produto", "Movimentar Estoque", "Consultar Estoque", "Histórico"])

if aba == "Cadastrar Produto":
    st.header("📋 Cadastro de Produto")
    with st.form("form_cadastro"):
        codigo = st.text_input("Código do Produto")
        nome = st.text_input("Nome do Produto")
        localizacao = st.text_input("Localização no Armazém (ex: A1)")
        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            cadastrar_produto(codigo, nome, localizacao)

elif aba == "Movimentar Estoque":
    st.header("📤 Entrada/Saída de Estoque")
    if not st.session_state.estoque:
        st.warning("Nenhum produto cadastrado.")
    else:
        with st.form("form_movimentacao"):
            codigo = st.selectbox("Produto", options=list(st.session_state.estoque.keys()))
            tipo = st.radio("Tipo de Movimentação", ["Entrada", "Saída"])
            quantidade = st.number_input("Quantidade", min_value=1, step=1)
            submitted = st.form_submit_button("Registrar")
            if submitted:
                movimentar_estoque(codigo, tipo, quantidade)

elif aba == "Consultar Estoque":
    st.header("🔎 Consulta de Estoque Atual")
    if st.session_state.estoque:
        for cod, info in st.session_state.estoque.items():
            st.write(f"**{cod} - {info['nome']}** | Qtd: {info['quantidade']} | Local: {info['localizacao']}")
    else:
        st.info("Nenhum produto no estoque.")

elif aba == "Histórico":
    st.header("📜 Histórico de Movimentações")
    if st.session_state.movimentacoes:
        for m in st.session_state.movimentacoes[::-1]:
            info = st.session_state.estoque.get(m["codigo"], {})
            st.write(f"{m['data'].strftime('%d/%m %H:%M')} | {m['tipo'].upper()} | {m['codigo']} - {info.get('nome', 'Desconhecido')} | Qtd: {m['quantidade']}")
    else:
        st.info("Nenhuma movimentação registrada.")
