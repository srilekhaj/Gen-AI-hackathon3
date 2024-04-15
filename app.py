import streamlit as st
from routingprompt import navigator
 
@st.cache_resource
def initialize():
    pass
 
st.session_state.chat=initialize()
 
st.title("Customer Support Chatbot 🤖🏦")
 
if "messages" not in st.session_state:
    # Welcome Message
    welcome_message = """**<h3>Welcome to our payment and banking support chat!**</h3>\n\nHow can we assist you?\n\nWe're delighted to help with any inquiries about your financial transactions.\nWhether it's making payments, checking balances, or resolving banking issues, 
    our team is here for you.\n\nJust type your query in the chatbox, and we'll swiftly provide the support you need.\nFor security purposes, please refrain from sharing sensitive information such as account numbers or passwords during this chat.\n\nLet's get started! 🚀    """

    st.session_state.messages = [{"role": "assistant", "content": welcome_message}]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"],unsafe_allow_html=True)
 
if prompt := st.chat_input("Enter Question"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
 
    response = navigator(prompt) # Backend
    with st.chat_message("assistant"):
        st.markdown(response,unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})
 
custom_css = """
<style>
body {
    color: #FF2D51; /* Change to your desired color */
    font-size:40;
}
</style>
"""

# Display the custom CSS

