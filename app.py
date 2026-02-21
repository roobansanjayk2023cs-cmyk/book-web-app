import streamlit as st
import requests

st.set_page_config(page_title="Book Finder", layout="wide")

st.title("📚 Book Search Application")
st.write("Search for any book and get details instantly!")

if "reading_list" not in st.session_state:
    st.session_state.reading_list = []

book = st.text_input("🔎 Enter Book Name")

if book != "":
    url = f"https://openlibrary.org/search.json?q={book}"
    response = requests.get(url)
    data = response.json()

    if data["docs"]:
        result = data["docs"][0]

        title = result.get("title","N/A")
        author = result.get("author_name",["Unknown"])[0]
        year = result.get("first_publish_year","N/A")

        st.subheader(title)
        st.write("✍ Author:", author)
        st.write("📅 First Published:", year)

        if st.button("➕ Add to Reading List"):
            st.session_state.reading_list.append(title)

        st.divider()
        st.subheader("📖 Recommended Books")

        for r in data["docs"][1:6]:
            st.write("•", r.get("title"))

    else:
        st.warning("No books found. Try another name.")

st.sidebar.title("📚 My Reading List")
for b in st.session_state.reading_list:
    st.sidebar.write("✔", b)
