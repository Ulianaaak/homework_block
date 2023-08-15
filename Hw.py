import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, ttest_rel

st.title('Анализ данных и проверка гипотез')

load_file = st.file_uploader('Загрузите CSV файл с данными', type='csv')

if load_file is not None:
    df = pd.read_csv(load_file)
else:
    st.warning('Пожалуйста, загрузите CSV файл.')
    st.stop()
st.set_option('deprecation.showPyplotGlobalUse', False)
variable_1 = st.selectbox('Выберите первую переменную', df.columns)
variable_2 = st.selectbox('Выберите вторую переменную', df.columns)


st.subheader('Распределение переменной 1')
if df[variable_1].dtype == 'object':
    plt.figure(figsize=(6, 6))
    df[variable_1].value_counts().plot.pie(autopct='%1.1f%%')
    st.pyplot()
else:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[variable_1], bins=20, kde=True)
    st.pyplot()

st.subheader('Распределение переменной 2')
if df[variable_2].dtype == 'object':
    plt.figure(figsize=(6, 6))
    df[variable_2].value_counts().plot.pie(autopct='%1.1f%%')
    st.pyplot()
else:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[variable_2], bins=20, kde=True)
    st.pyplot()

hypothesis_test = st.selectbox('Выберите алгоритм проверки гипотез', ['t-тест (независимые выборки)', 't-тест (зависимые выборки)'])

if hypothesis_test == 't-тест (независимые выборки)':
    result = ttest_ind(df[variable_1], df[variable_2])
    st.write('p-значение:', result.pvalue)
    if result.pvalue < 0.05:
        st.write('Гипотеза о равенстве средних отвергается.')
    else:
        st.write('Гипотеза о равенстве средних принимается.')
else:
    result = ttest_rel(df[variable_1], df[variable_2])
    st.write('p-значение:', result.pvalue)
    if result.pvalue < 0.05:
        st.write('Гипотеза о равенстве средних отвергается.')
    else:
        st.write('Гипотеза о равенстве средних принимается.')
    pass


def run():
    html_temp = """

    """

if __name__=='__main__':
    st.sidebar.write('https://github.com/Ulianaaak')

    run()
