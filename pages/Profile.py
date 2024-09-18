import streamlit as st
import base64

st.title('My Profile')
st.subheader('Mikhaïl BENALI')

st.image("img/profile_picture.jpeg", width=200, caption='A picture of me')

st.markdown("""
    I'm **Mikhaïl BENALI**, a student in the Big Data & Machine Learning Master's program at EFREI Paris.
    I'm passionate about data science and machine learning, and I'm always looking for new projects to work on.
""")

col1, col2 = st.columns(2)

with col1:
    # Github button
    st.markdown(
        """<a href="https://github.com/mikhailBenali/">
        <img src="data:image/png;base64,{}" width="75">
        </a>""".format(
            base64.b64encode(open("/home/mikhail/Documents/Coding/DataAnalysis/DataVizProject/img/GitHub-Symbol.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
with col2:
    # Linkedin button
    st.markdown(
        """<a href="https://www.linkedin.com/in/mikha%C3%AFl-benali/">
        <img src="data:image/png;base64,{}" width="75">
        </a>""".format(
            base64.b64encode(open("/home/mikhail/Documents/Coding/DataAnalysis/DataVizProject/img/linkedin-logo-linkedin-icon-transparent-free-png.webp", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )

st.header('My Skills :hammer_and_wrench:')

st.markdown("""
**Programming languages** :computer: : Python, Java, C, C++, SQL

**Soft skills** 🗣️ : Teamwork, communication, problem-solving

**Mathematics** 🔣 : Linear algebra, calculus, statistics, probability
""")