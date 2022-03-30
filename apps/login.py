import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth

def app():

    def page_config():
         st.set_page_config(
             page_title="Login",
             page_icon=":bar_chart"
    )

    names = ['Julio Rafael', 'Utilizador 1']
    usernames = ['jr', 'user1']
    passwords = ['a', '123']

    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login('Login - Dashboard de vendas', 'main')

    if authentication_status:
        authenticator.logout('Sair', 'main')
        st.write('Bem-vindo(a) *%s*' % (name))
        st.title('Some content')
        #sys.stdout = open('home.py', 'r')
    elif authentication_status == False:
        st.error('Credenciais incorrectas')
    elif authentication_status == None:
        st.warning('Por favor, preencha as credenciais de acesso.')

    # Hide Streamlite style
    hide_st_styles = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_styles, unsafe_allow_html=True)


