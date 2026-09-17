import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="glex AI", page_icon="✨")
st.title("✨ glex AI")


@st.cache_resource
def get_model():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation",
        max_tokens=512
    )
    return ChatHuggingFace(llm=llm)


model = get_model()

# --- Mode selection ---
if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False
    st.session_state.messages = []

if not st.session_state.mode_selected:
    st.subheader("Choose your AI model")
    choice = st.radio(
        "Select a mode:",
        options=[1, 2, 3],
        format_func=lambda x: {1: "Angrymode", 2: "Happymode", 3: "Neutralmode"}[x]
    )

    if st.button("Confirm"):
        mode_map = {
            1: "You have selected Angrymode",
            2: "You have selected Happymode",
            3: "You have selected Neutralmode"
        }
        mode = mode_map[choice]
        st.session_state.messages = [SystemMessage(content=mode)]
        st.session_state.mode_selected = True
        st.rerun()

else:
    # --- Chat interface ---
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    prompt = st.chat_input("Type your message...")

    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)

        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("assistant"):
            st.write(response.content)