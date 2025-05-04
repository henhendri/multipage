import streamlit as st
import time

st.image("assets/profile.png", width=200)
st.title(f"Hendri Setiadi, S.Tr.Kom., Gr.", anchor=False)
st.write( 
    """
    Teacher SMAN 20 BANDUNG
    """
)
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"

)

def typewriter(text, speed=50):
    placeholder = st.empty()
    for char in text:
        placeholder.markdown(f"<span style='font-family: monospace; font-size: 20px;'>{char}</span>", unsafe_allow_html=True)
        time.sleep(speed / 1000)

def main():
    st.title("Efek Typewriter dengan Streamlit")

    # Teks yang bergerak
    text_to_animate = "Ini adalah teks yang bergerak!"
    
    while True:
        for i in range(len(text_to_animate) + 1):
            animated_text = text_to_animate[:i]
            typewriter(animated_text, speed=75)  # Mengatur kecepatan animasi
            time.sleep(0.1)  # Jeda sebentar
            st.empty()  # Membersihkan output sebelumnya

if __name__ == "__main__":
    main()


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
