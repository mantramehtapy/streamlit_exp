import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('hello', 'mantra'))

st.write('You selected:', option)
