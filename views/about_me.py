import streamlit as st
from streamlit_extras.stylable_container as stylable_container

c1, c2 = st.coloumns(2)

with c1 :
    with stylable_container(
        key="profile",
        css_styles="""
        img{
            border-radius: 100px;
        }
        """,
  ):
        st.image("assets/profile.png", width=200)
st.divider()
    
with c2 :
    st.title(f"Hendri Setiadi, S.Tr.Kom., Gr.", anchor=False)
    st.write( 
    """
    Teacher SMAN 20 BANDUNG
    """
    )

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"

)


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
    - Programming: Codeigniter, Python (Scikit-learn, Pandas, Streamlit), SQL, VBA, Apps Script
    - Data Visualization: PowerBi, MS Excel, Plotly, AppSheet
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    - Design and Editor: Adobe Photoshop, Adobe Lightroom, CorelDraw
    - Photographer
    """
)
