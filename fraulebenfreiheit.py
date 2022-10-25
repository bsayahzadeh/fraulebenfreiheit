import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

path= Path.cwd() / "deputies.csv"

df = pd.read_csv(path, sep=";")

st.header(":mailbox: Schreibe deinen Abgeordneten")

st.write("Seit Wochen weht im Iran ein Wind der Veränderungen. Und seit Wochen lehnen sich immer mehr gesellschaftliche Schichten gegen das Unrechtsregime im Iran.")

@st.cache(suppress_st_warning= True, allow_output_mutation=True)
def get_info(plz):
    info = df[["Abgeordnete", "E-Mail", "Partei", "Wahlkreis"]].loc[df.PLZ.str.contains(plz)]
    info = info.set_index("Abgeordnete").sort_values(by=["Wahlkreis"])
    return info

with st.form("mail"):
    name = st.text_input("Vollständiger Name")
    email = st.text_input("E-Mail Adresse")
    plz = st.text_input("Deine Postleitzahl")
    
    submit = st.form_submit_button("Weiter")

if submit:
    df = get_info(plz)
    st.table(df)
    email_list = df["E-Mail"]
    contact = st.multiselect("Möchtest du gewissen Abgeordneten NICHT schreiben? Diese kannst du hier entfernen:", email_list, default=email_list)
    st.write("Wir empfehlen grundsätzlich ALLEN Abgeordneten (parteiübergreifend) zu schreiben.")

st.text_area("Deine E-Mail", value="""Sehr geehrte/r Abgeordnete/r, \nseit Wochen weht im Iran ein Wind der Veränderungen. Und seit Wochen lehnen sich immer mehr gesellschaftliche Schichten gegen das Unrechtsregime im Iran.
             """)
