import streamlit as st

st.header (":mailbox: Get in touch with Me!")

st.title(f"Mail Message", anchor=False)


contact_form = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=true)
