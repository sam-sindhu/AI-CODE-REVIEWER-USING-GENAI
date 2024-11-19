import streamlit as st
import google.generativeai as genai

# Configure your API key
key="AIzaSyCpybaH_MC6gItkK5Sn2fZ4FpU_HDxoVbQ"
genai.configure(api_key=key)


# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Background styling */
        .stApp {
            background-image: linear-gradient(to right, #a9a9a9, #e0ffff);
            color: grey;
        }

        /* Title styling */
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #000000;
            text-shadow: 2px 2px 5px #000;
            margin-bottom: 10px;
        }

        /* Text area styling */
        textarea {
            background: rgba(255, 255, 255, 0.8) !important;
            border: 1px solid #ddd !important;
            color: #000 !important;
            border-radius: 5px !important;
            font-size: 16px !important;
        }

        /* Button styling */
        button[kind="primary"] {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            font-size: 18px !important;
            padding: 10px 20px !important;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }

        /* Subheader styling */
        .stMarkdown h2 {
            color: #000000;
            text-shadow: 1px 1px 2px #000;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("AI Code Reviewer Features")
st.sidebar.subheader("How to use?")
st.sidebar.write(" Enter Your Python code for review.")
st.sidebar.write(" Get a bug report .")

st.sidebar.markdown("---")
st.sidebar.write("Designed to provide a great experience!")

st.sidebar.markdown("---")
st.sidebar.write("📌 **Take the time to review your code for improvements**.")

# Title
st.markdown('<div class="title">AI Code Reviewer </div>', unsafe_allow_html=True)

# Description
st.write("Welcome to the **AI Code Reviewer**! Paste your Python code below, and let the AI help you identify bugs and provide useful feedback.")

# Input for the human prompt
human_code = st.text_area("📝 Enter your code here for review:")

# Button to trigger code review
if st.button("✨ Generate"):
    if human_code:
        # Initialize the generative model
        genai.configure(api_key=key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = model.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{human_code}")
        #response = chatbot.send_message(f"Review the following Java code and identify any bugs:\n{human_code}")
        # Display the AI-generated response
        st.subheader("🧐 Code Review")
        st.markdown("**Bug Report:**")
        st.write(response.text)  # Display AI response
    else:
        st.error("❌ Please enter some code before generating the review!")

# Footer
st.markdown("---")
#st.markdown("Made by Rakshitha")

