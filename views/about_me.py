import streamlit as st


c1, c2 = st.columns(2)

with c1 :
    st.image("assets/profile.png", width=200)
    
with c2 :
    st.markdown(
        """
            <div class="container" style="text-align: left; margin-top: -4px;">
                <h2 class='custom-title' style='color: #3dd56d;'>Hendri Setiadi, S.Tr.Kom</h2>
                <h4 class='custom-title'>Teacher SMAN 20 Bandung</h4>
            </div>
            <div class="main-description"> 
            <ul>
                <li><h6>Aspiring Software Developer & Microsoft Certified: Azure Developer Associate</h6></li>
                <li><h6>Systems Analysis and Development Student at Faculdade XP</h6></li>
                <li><h6>Passionate about data modeling and cloud technologies</h6></li> 
                <li><h6>Driven to innovate, collaborate, and make a positive impact</h6></li>
            </ul>
            </div>
        """, 
        unsafe_allow_html=True
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
