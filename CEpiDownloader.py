import streamlit as st
import requests

st.set_page_config(page_title='CEpiDownloader', page_icon=':sparkles:', layout='wide')

st.subheader("CEpi Downloader :sparkles:")

download_url = st.text_input("Enter URL: ")

req = requests.get(download_url)

filename = st.text_input("Enter preferred file name: ")

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
            st.write("Download complete!", "\nIf you wish to download another file, just paste the link. Thank you!")

