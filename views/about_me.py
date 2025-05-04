import streamlit as st
import time
import base64

def main():
    """
    Menampilkan animasi Typing SVG dari readme-typing-svg di Streamlit.
    """
    st.title("Menampilkan Typing SVG di Streamlit")

    # SVG code dari readme-typing-svg.com
    svg_code = """
<svg xmlns="http://www.w3.org/2000/svg" width="435" height="75" viewBox="0 0 435 75">
  <style>
    .typing-text {
      font-family: Fira Code, monospace;
      font-size: 20px;
      color: black;
      overflow: hidden;
      border-right: .15em solid orange;
      white-space: nowrap;
      margin: 0 auto;
      letter-spacing: .15em;
      animation:
        typing 6s steps(40, end) infinite,
        blink-caret .75s step-end infinite;
    }
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: orange; }
    }
  </style>
  <text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" class="typing-text">
    I am Teacher
  </text>
  <script>
    const textElement = document.querySelector('.typing-text');
    const phrases = ['I am Teacher', 'I am Photographer', 'I am UI/UX Designer', 'I am Freelancer'];
    let phraseIndex = 0;
    let charIndex = 0;
    let pause = 1000;

    function type() {
      const currentPhrase = phrases[phraseIndex];
      if (charIndex < currentPhrase.length) {
        textElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        setTimeout(type, 150); // Kecepatan mengetik
      } else {
        setTimeout(erase, pause);
      }
    }

    function erase() {
      if (charIndex > 0) {
        textElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, 50); // Kecepatan menghapus
      } else {
        phraseIndex = (phraseIndex + 1) % phrases.length;
        charIndex = 0;
        setTimeout(type, 500); // Pause sebelum mengetik kalimat berikutnya
      }
    }

    setTimeout(type, 500); // Memulai animasi setelah jeda
  </script>
</svg>
"""

    # Convert SVG code to base64
    b64 = base64.b64encode(svg_code.encode()).decode()
    # Display the SVG using st.markdown
    st.markdown(
        f'<img src="data:image/svg+xml;base64,{b64}" alt="Typing SVG">',
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()

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
