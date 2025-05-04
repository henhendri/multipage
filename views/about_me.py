import streamlit as st

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
    """Simulasi efek ketikan typewriter di Streamlit.

    Args:
        text (str): Teks yang akan ditampilkan.
        speed (int, optional): Kecepatan ketikan dalam milidetik per karakter. Default adalah 50.
    """
    placeholder = st.empty()  # Membuat placeholder untuk teks yang akan diupdate
    for char in text:
        placeholder.markdown(f"<span style='font-family: monospace; font-size: 20px;'>{char}</span>")  # Menggunakan monospace untuk tampilan typewriter
        time.sleep(speed / 1000)  # Mengubah kecepatan ke detik

def main():
    """Fungsi utama untuk menjalankan aplikasi Streamlit."
    st.title("Efek Typewriter dengan Streamlit")

    # Teks pembuka
    typewriter("I am ", speed=25) #Perlambat sedikit agar "I am" tidak terlalu cepat

    # Daftar pekerjaan
    professions = ["Teacher", "Photographer"]
    profession_index = 0

    # Loop untuk mengganti pekerjaan setiap beberapa detik
    while True:
        profession = professions[profession_index]
        placeholder_profesion = st.empty() # Membuat placeholder untuk kata Teacher/Photographer
        typewriter(profession, speed=50)
        time.sleep(2)  # Menunggu 2 detik sebelum menghapus
        placeholder_profesion.markdown("") # Menghapus tulisan sebelumnya
        profession_index = (profession_index + 1) % len(professions) #memastikan index tidak melebihi panjang list

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
