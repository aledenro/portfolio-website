import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.header("Alejandro Denver")

with col2:
    content = """"Hello, I am Alejandro. I am a software developer at an US Based company. 
    I started my career as a freelancer, developing an order management software for a local restaurant at my city, 
    based on Java. I am currently developing a locally based app, with Python as the main language, for DINADECO, 
    a government institution, in order to help them optimize their processes. After my experience as a freelancer, 
    I landed at viaPeople Inc. where I am junior dev, working as a fullstack developer using Java, Vue, and SQL Server."""
    st.info(content)

content_apps = """Below you can find some of the apps I have built. Feel free to contact me!"""

st.write(content_apps)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")