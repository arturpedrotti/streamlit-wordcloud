import streamlit as st
import pandas as pd

def main():
    st.title('CSV Viewer')
    data = pd.read_csv('dados.csv')
    st.dataframe(data)

if __name__ == '__main__':
    main()
