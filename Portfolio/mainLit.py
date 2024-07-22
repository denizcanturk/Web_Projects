import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Arial', sans-serif;
}
.header {
    background-color: #4CAF50;
    padding: 20px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}
.section {
    background-color: white;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
h1, h2, h3 {
    color: #333;
}
h2 {
    margin-top: 0;
}
.sidebar .sidebar-content {
    background-color: #f8f9fa;
}
a {
    color: #4CAF50;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<div class='header'><h1>Welcome to My Portfolio! 🎉</h1></div>", unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.radio("Select a page:", ["Home", "Projects", "Skills", "Contact"])

# Function to load HTML content
def load_html(file_path):
    with open(file_path, "r") as f:
        html_content = f.read()
    return html_content

# Home Page
if page == "Home":
    st.markdown("<div class='section'><h2>About Me</h2>", unsafe_allow_html=True)
    st.write("""
    Hello! I'm [Your Name], a [Your Profession/Role]. 
    I have a passion for [Your Passion] and a knack for [Your Skill]. 
    Welcome to my portfolio where you can learn more about my work and skills.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Projects Page
elif page == "Projects":
    st.markdown("<div class='section'><h2>Projects</h2>", unsafe_allow_html=True)
    st.write(load_html("projects.html"), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Skills Page
elif page == "Skills":
    st.markdown("<div class='section'><h2>Skills</h2>", unsafe_allow_html=True)
    st.write(load_html("skills.html"), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.markdown("<div class='section'><h2>Contact</h2>", unsafe_allow_html=True)
    
    with st.form(key='contact_form'):
        st.write("Fill out the form below to get in touch!")
        name = st.text_input("Name")
        surname = st.text_input("Surname")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if name and surname and email and message:
                # Save to a CSV file
                data = {
                    "Timestamp": [datetime.now()],
                    "Name": [name],
                    "Surname": [surname],
                    "Email": [email],
                    "Message": [message]
                }
                df = pd.DataFrame(data)
                df.to_csv('contact_form_submissions.csv', mode='a', header=False, index=False)
                
                st.success("Your message has been sent successfully!")
            else:
                st.error("Please fill out all fields.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align: center; margin-top: 50px;'>© 2024 Your Name</div>", unsafe_allow_html=True)
