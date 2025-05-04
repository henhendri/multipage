import streamlit as st

st.header (":mailbox: Get in touch with Me!")

st.title(f"Mail Message", anchor=False)


st.page == "contact":
st.write("Feel free to contact us with any questions or inquiries.")

contact_form_html = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
"""

st.markdown(contact_form_html, unsafe_allow_html=True)

# You can add other contact information below the form
st.write("Email: contact@example.com")
st.write("Phone: 123-456-7890")
contact_form_html.run
