---
name: streamlit
description: "Builds interactive data apps and ML demos with Streamlit, using pure Python widgets and charts."
category: ai
tags: [streamlit, python, data-app, dashboard, ml]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Streamlit
> Turn Python scripts into interactive web apps in seconds.
## Quick Start
```python
import streamlit as st
st.title('My Data App')
name = st.text_input('Enter your name')
if st.button('Say Hello'): st.write(f'Hello, {name}!')
```
## Widgets & Caching
```python
uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
if uploaded_file:
    import pandas as pd; import plotly.express as px
    df = pd.read_csv(uploaded_file); st.dataframe(df)
    fig = px.histogram(df, x=st.selectbox("Column", df.columns)); st.plotly_chart(fig)
@st.cache_data
def load_data(): return pd.read_csv('large.csv')
```
## When to Use
- ML model demos; Data analysis dashboards; Internal tools; Rapid prototyping
## Validation
1. App runs with streamlit run; 2. Widgets update interactively; 3. Charts render correctly
