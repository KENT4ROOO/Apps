import streamlit as st

st.set_page_config(page_title = 'CEpi', page_icon = ':orange_book:', layout = 'wide')


st.title('Welcome to CEpi! :sparkles:')
st.subheader('What subject you need help?')
st.write('Differential Calculus / Mathematics in the Modern World / General Chemistry / Integral Calculus / Physics / Computer Programming (Python)')

response = st.text_input('Enter Subject: ')
if response == 'General Chemistry':
    st.write('[Activities & PSets >](https://drive.google.com/drive/folders/1dFxx5fM0mK5eoNIIezyknchb1L3mempL?usp=sharing)')
    st.write('[Experiments >](https://drive.google.com/drive/folders/1ynplAOUnUfQnv2lSTGjysNxg2EqmaU_j?usp=sharing)')
if response == 'Physics':
    st.write('[Activities & PSets >](https://drive.google.com/drive/folders/1-aaGmSl6No9DUsbzc-fo-S0SuBQi1-qq?usp=sharing)')
    st.write('[Books & Modules >](https://drive.google.com/drive/folders/1zPtWCrsRwgChtilwzA5xAWKEiAZ8YI1d?usp=sharing)')
if response == 'Computer Programming (Python)':
    st.write('[Books & Modules >](https://drive.google.com/drive/folders/1Hj-SKd8M4P_iol46r5kaiGx9okHUExdK?usp=sharing)')


