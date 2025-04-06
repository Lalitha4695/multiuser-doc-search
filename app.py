import streamlit as st
from scripts.query_handler import get_response, get_history
import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "watchdog"


st.set_page_config(page_title="Multi-User Document Search")
st.title("🔍 Multi-User Document Search (Local RAG with Flan-T5)")

email = st.text_input("Enter your email to begin:")

if email:
    st.write(f"Welcome, **{email}**! Start your queries below.")
    query = st.text_input("Enter your query:")
    if st.button("Submit") and query:
        results = get_response(email, query)
        if results:
            st.subheader("🧠 Local AI Answer:")
            st.markdown(results[0][1])
        else:
            st.warning("No authorized results found.")
    st.divider()
    st.subheader("📜 Chat History")
    history = get_history(email)
    for item in history:
        st.markdown(f"**Q:** {item['query']}  \n**A:** {item['response'][0][1]}")
