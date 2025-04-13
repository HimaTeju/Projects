import streamlit as st
from streamlit_chat import message
from backend import get_llama_response  

# --- UI Setup ---
st.set_page_config(page_title="LLaMA Chat", page_icon="🦙", layout="centered")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "system", "content": "You are a helpful assistant."}]

# Sidebar Reset
with st.sidebar:
    st.title("LLaMA Chat 🦙")
    if st.button("🔄 Reset Chat"):
        st.session_state['generated'] = []
        st.session_state['past'] = []
        st.session_state['messages'] = [{"role": "system", "content": "You are a helpful assistant."}]

# Backend response integration
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    
    response = get_llama_response(prompt)  # 🧠 Call your model
    st.session_state['messages'].append({"role": "assistant", "content": response})
    
    return response

# Chat UI
chat_container = st.container()
input_container = st.container()

with input_container:
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_area("Type your message", key='input', height=80)
        send = st.form_submit_button("Send")

    if send and user_input:
        output = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

with chat_container:
    for i in range(len(st.session_state['generated'])):
        message(st.session_state["past"][i], is_user=True, key=f"{i}_user")
        message(st.session_state["generated"][i], key=f"{i}")

# CSS for styling (same as before)
st.markdown("""...""", unsafe_allow_html=True)  # Add your earlier CSS here
