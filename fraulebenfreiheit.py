import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

path= Path.cwd() / "deputies.csv"
path

df = pd.read_csv(path, sep=";")

st.header(":mailbox: Schreibe deinen Abgeordneten")

st.write("Seit Wochen weht im Iran ein Wind der Veränderungen. Und seit Wochen lehnen sich immer mehr gesellschaftliche Schichten gegen das Unrechtsregime im Iran.")

with st.form("mail"):
    name = st.text_input("Vollständiger Name")
    email = st.text_input("E-Mail Adresse")
    plz = st.text_input("Deine Postleitzahl")
    
    submit = st.form_submit_button("Weiter")
