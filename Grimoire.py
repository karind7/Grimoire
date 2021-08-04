# streamlit run main.py
# streamlit run Grimoire.py
import pandas as pd
import streamlit as st
import datetime

today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day

Title_html = """
    <style>
        .title h1{
          user-select: none;
          font-size: 43px;
          color: white;
          background: repeating-linear-gradient(-45deg, red 0%, yellow 7.14%, rgb(0,255,0) 14.28%, rgb(0,255,255) 21.4%, cyan 28.56%, blue 35.7%, magenta 42.84%, red 50%);
          background-size: 600vw 600vw;
          -webkit-text-fill-color: transparent;
          -webkit-background-clip: text;
          animation: slide 10s linear infinite forwards;
        }
        @keyframes slide {
          0%{
            background-position-x: 0%;
          }
          100%{
            background-position-x: 600vw;
          }
        }
    </style> 

    <div class="title">
        <h1>Grimoire</h1>
    </div>
    """


def mf_table(year):
    mf_year = pd.read_html('https://www.timeanddate.com/moon/phases/?year={}'.format(year))
    mf_year = mf_year[1]
    for i in ['Lunation', 'New Moon.1', 'First Quarter.1', 'Full Moon.1', 'Third Quarter.1', 'Duration']:
        try:
            mf_year = mf_year.drop(i, axis=1)
        except:
            pass
    mf_year = mf_year[:13]
    for i in ['New Moon', 'First Quarter', 'Full Moon', 'Third Quarter']:
        try:
            mf_year[i] = pd.to_datetime(mf_year[i] + " " + str(year), format='%b %d %Y').dt.strftime('%d/%m/%Y')
        except:
            pass
    mf_year = mf_year.fillna('')
    return mf_year


def herbs_table():
    herbs = pd.read_excel('witchcraft.xlsx')
    return herbs


st.markdown(Title_html, unsafe_allow_html=True)

with st.beta_container():
    st.markdown('## **Moon Phases**')
    year = st.text_input(label='year:', value=year)
    st.dataframe(mf_table(year), width=800, height=900)
    st.image("https://c.tadst.com/gfx/1200x630/moon-phases-explained.png?1")


# with st.beta_container():
#     st.markdown('## **Herbs**')
#     st.dataframe(herbs_table(), width=800, height=900)

