import streamlit as st
from view import views
class UI:
    def main():
        st.header("Informações dos Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar","Excluir"])

        with tab1:
            st.header("Listar")

        with tab2:
            st.header("Inserir")
            nome = st.text_input("informe o nome")
            email = st.text_input("informe o email")
            fone = st.text_input("informe o Telefone")
            if st.button("Inserir"):
                views.cliente_inserir(nome, email, fone)
        with tab3:
            st.header("Atualizar")
            option = st.selectbox(
                'Selecione o cliente que desejar atualizar',
                (views.cliente_listar()))
            nome = st.text_input("informe o novo nome")
            email = st.text_input("informe o novo email")
            fone = st.text_input("informe o novo Telefone")
            if st.button("Atualizar"):
                views.cliente_atualizar(nome, email, fone)
        with tab4:
            st.header("Excluir")
            option = st.selectbox(
                'Selecione o cliente que desejar excluir',
                (views.cliente_listar()))
            if st.button("Excluir"):
                views.cliente_excluir()
