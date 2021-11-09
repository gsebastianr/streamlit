import streamlit as st
import pandas as pnd

if __name__ == '__main__':
    st.bar_chart(pnd.Series(range(5)))