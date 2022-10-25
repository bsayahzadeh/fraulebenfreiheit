import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel("/Users/betisa/Desktop/fraulebenfreiheit/deputies.xlsx")

st.header(":mailbox: Schreibe deinen Abgeordneten")

st.write("Seit Wochen weht im Iran ein Wind der Veränderungen. Und seit Wochen lehnen sich immer mehr gesellschaftliche Schichten gegen das Unrechtsregime im Iran.")

st.table(df.head())
