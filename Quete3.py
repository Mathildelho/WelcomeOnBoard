import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth

##A revoir car un peu flou ###
url = "Quete3.csv"
users = pd.read_csv(url)
users = users.to_dict(orient="records")  # POur que les colonnes soient bien en face
dico_users = dict()
for user in users:
    dico_users.update({user["name"]: user})  # revoir
dico_users = dict({"usernames": dico_users})  # a revoir


authenticator = Authenticate(
    dico_users,  # Les données des comptes du csv !!
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30,  # Le nombre de jours avant que le cookie expire
)

authenticator.login()


def accueil():

    if selection == "Accueil 🎈":
        st.header(""":rainbow: :rainbow[Welcome On Board - By Mathilde]""")
        st.image("mathilde.png")
    elif selection == "Photos ❄️":
        st.header(""":rainbow[Here you can see my Amazing Dog !!]:rainbow:""")
        st.text("Team chien")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header(""" :rainbow[I can see you, You can't see me..]""")
            st.image(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-ZRfXIvI2uMX-wJd4IEGnLpDimAiKziHRqQ&s"
            )
        with col2:
            st.header(""" :rainbow[Prepare to Landing guys!]""")
            st.image(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJHQFbiNeWEOGY0u_lW28GNlBU5giTLoYYkA&s"
            )
        with col3:
            st.header(""" :rainbow[Too badass for you!]""")
            st.image(
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa2Qi3-P5P8UqFYe73Oe2YPT_pfcip39GmuQ&s"
            )


if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion")
        selection = option_menu(menu_title=None, options=["Accueil 🎈", "Photos ❄️"])
        st.write(f"Bienvenue chèr(e): {st.session_state['name']}")
    accueil()


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplie")
