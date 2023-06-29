import time
import streamlit as st
from streamlit_chat import message


# streamlit
st.set_page_config(layout="wide")


def reset_history():
    st.session_state['messages'] = [
        {"role": "system", "content": "あなたは優秀なアシスタントです。"}
    ]


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state['messages'].append(
        {"role": "user", "content": user_input}
    )


def _logo(is_user):
    # avatar_style="croodles-neutral" if is_user else "bottts",
    if is_user:
        logo = "https://api.dicebear.com/6.x/croodles-neutral/svg?seed=Felix"
    else:
        logo = "https://api.dicebear.com/6.x/bottts/svg?seed=Felix"

    return logo


if 'messages' not in st.session_state:
    reset_history()

chat_placeholder = st.empty()
with chat_placeholder.container():
    is_user = False
    message(
        "なんでも質問してください。",
        is_user=is_user,
        logo=_logo(is_user),
        key="message_0",
    )
    for i, m in enumerate(st.session_state['messages'][1:]):
        is_user = m["role"] == "user"
        message(
            message=m["content"],
            is_user=is_user,
            logo=_logo(is_user),
            key=f"message_{i+1}",
        )


m_last = st.session_state["messages"][-1]
if m_last["role"] == "user":
    user_input = st.session_state.user_input
    with st.spinner('Wait for it...'):
        time.sleep(1)
        # output = generate_response(user_input)
        output = f"「{user_input}」という質問はすばらしい！でも私にはわかりません。"
    st.session_state['messages'].append(
        {"role": "assistant", "content": output}
    )
    st.experimental_rerun()

with st.container():
    st.button("Clear message", on_click=reset_history)
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
