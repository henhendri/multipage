import streamlit as st

st.image("assets/profile.png", width=200)
st.title(f"Hendri Setiadi, S.Tr.Kom., Gr.", anchor=False)
st.write( 
    """
    Teacher SMAN 20 BANDUNG
    """
)
st.html("<p><span><a href="https://git.io/typing-svg">
        <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=435&lines=I+am+Teacher;I+am+Photographer;I+am+UI%2FUX+Designer;I+am+Freelancer" alt="Typing SVG" /></a>"
</span></p>)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)
