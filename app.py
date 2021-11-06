import streamlit as st

m = st.markdown(""" <style> div.stButton > button:first-child { background-color: rgb(204, 49, 49); width: 100%; font-size: 32px} </style>""", unsafe_allow_html=True) 
m2 = st.markdown(f'''
    <style>
    section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
    </style>
''',unsafe_allow_html=True)

st.sidebar.title("TEAMS")
st.sidebar.button("Herren")
st.sidebar.button("Damen")
st.sidebar.button("U18")


