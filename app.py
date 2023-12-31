import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import matplotlib
from matplotlib import font_manager


st.title(":flag-tw: 慢性病連續處方箋釋出率")
st.markdown('[*資料來源：衛生福利部中央健康保險署*](https://data.gov.tw/dataset/79580)')

rx = pd.read_csv('./data_rxrelease_revise.csv', encoding='utf-8')

st.sidebar.subheader('調整參數：')
selected_year = st.sidebar.slider('選擇想要顯示的**年份**...', min_value=rx['year'].min(), max_value=rx['year'].max(), value=rx['year'].min())
selected_quarter = st.sidebar.slider('選擇想要顯示的**季度**...', min_value=1, max_value=4, value=1)
selected_hospital = st.sidebar.selectbox('選擇想要顯示的**醫院**...', rx['醫事機構名稱'].unique())
filtered_data = rx[(rx['year'] == selected_year) & (rx['quantile'] == selected_quarter) & (rx['醫事機構名稱'] == selected_hospital)]

st.dataframe(filtered_data)


fig, ax = plt.subplots()
ax.plot(filtered_data['year'], filtered_data['慢性病連續處方箋釋出率'], marker='o', label='慢性病連續處方箋釋出率')
ax.set_title('慢性病連續處方箋釋出率趨勢')
ax.set_xlabel('年度')
ax.set_ylabel('慢性病連續處方箋釋出率')
ax.legend()
st.pyplot(fig)

st.divider()
