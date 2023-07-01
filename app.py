import time
import streamlit as st
from streamlit_chat import message


# streamlit
st.set_page_config(layout="wide")


def reset_history():
    st.session_state["messages"] = []


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state["messages"].append({"role": "user", "content": user_input})


def _logo(is_user):
    # avatar_style="croodles-neutral" if is_user else "bottts",
    if is_user:
        logo = "https://api.dicebear.com/6.x/croodles-neutral/svg?seed=Felix"
    else:
        logo = "https://api.dicebear.com/6.x/croodles-neutral/svg?eyes=variant09&mouth=variant08"

    return logo


if "messages" not in st.session_state:
    reset_history()

chat_placeholder = st.empty()
with chat_placeholder.container():
    pre_messages = [
        {"role": "assistant", "content": "なんでも質問してください。"},
    ]
    for i, m in enumerate(pre_messages + st.session_state["messages"]):
        is_user = m["role"] == "user"
        message(
            message=m["content"],
            is_user=is_user,
            logo=_logo(is_user),
            key=f"message_{i+1}",
        )


def generate_response(user_input):
    # sample response
    time.sleep(1)
    output = f"「{user_input}」という質問はすばらしい！でも私にはわかりません。"
    return output


# def generate_response(user_input):
#     template = "Q: {input}\nA: "

#     prompt = PromptTemplate(
#         input_variables=["input"],
#         template=template,
#     )

#     chain = LLMChain(llm=llm_chat, prompt=prompt)
#     res = chain.run(input=user_input)
#     return res


if len(st.session_state["messages"]) > 0:
    m_last = st.session_state["messages"][-1]
    if m_last["role"] == "user":
        user_input = st.session_state.user_input
        with st.spinner("Wait for it..."):
            output = generate_response(user_input)
        st.session_state["messages"].append({"role": "assistant", "content": output})
        st.experimental_rerun()

with st.container():
    st.button("Clear message", on_click=reset_history)
    # st.text_input("User Input:", key="user_input", on_change=on_input_change)
    st.chat_input("User Input:", key="user_input", on_submit=on_input_change)
