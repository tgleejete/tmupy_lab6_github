import streamlit as st
import pandas as pd

st.title(":flag-tw: 慢性病連續處方箋釋出率")
st.markdown('[*資料來源：衛生福利部中央健康保險署*](https://data.gov.tw/dataset/79580)')

rx = pd.read_csv('./data_rxrelease_revise.csv', encoding='utf-8')

st.sidebar.subheader('調整參數：')
selected_year = st.sidebar.slider('選擇想要顯示的**年份**...', min_value=rx['year'].min(), max_value=rx['year'].max(), value=rx['year'].min())
selected_quarter = st.sidebar.slider('選擇想要顯示的**季度**...', min_value=1, max_value=4, value=1)
selected_hospitals = st.multiselect("選擇醫院", rx['hopital'].unique())
filtered_data = rx[(rx['year'] == selected_year) & (rx['quarter'] == selected_quarter) & (rx['hopital'].isin(selected_hospitals))]

st.dataframe(filtered_data)
st.divider()
