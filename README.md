# 📦 Sistema WMS (Warehouse Management System)

Este é um sistema de gerenciamento de armazéns (WMS) desenvolvido com **Streamlit**. Ele permite o **cadastro de produtos**, **movimentação de estoque** (entradas e saídas), **consulta de estoque atual** e **visualização do histórico de movimentações**.

---

## 🚀 Funcionalidades

### 📋 Cadastro de Produto
Permite cadastrar novos produtos no sistema.  
Informações fornecidas:
- Código do produto
- Nome do produto
- Localização no armazém (ex: A1, B2)

### 📤 Movimentação de Estoque
Registra **entradas** e **saídas** de produtos no estoque.  
Validações:
- Verifica se o produto está cadastrado no estoque
- Garante que a quantidade de saída não exceda o estoque disponível

### 🔎 Consulta de Estoque
Exibe uma lista de produtos atualmente no estoque.  
Informações exibidas:
- Código do produto
- Nome do produto
- Quantidade disponível
- Localização no armazém

### 📜 Histórico de Movimentações
Exibe o histórico completo de movimentações.  
Informações exibidas:
- Data e hora da movimentação
- Tipo de movimentação (Entrada ou Saída)
- Código e nome do produto
- Quantidade movimentada

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Streamlit**: Para a interface do usuário
- **Datetime**: Para registro de data e hora das movimentações

---

## ✅ Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
