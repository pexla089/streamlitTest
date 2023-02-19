import openai
import streamlit as st

# Set up OpenAI API key
st.sidebar.header("OpenAI API Key")
openai.api_key = st.sidebar.text_input("Enter your OpenAI API Key")

# Set up language selection
st.sidebar.header("Language Selection")
language = st.sidebar.selectbox("Choose a language:", ["English", "French", "German"])

# Set up keyword input
st.sidebar.header("Keyword Input")
keyword = st.sidebar.text_input("Enter a keyword:")

# Generate blog post titles based on keyword
st.header("Blog Post Titles")
if keyword:
    titles = generate_titles(keyword)
    selected_titles = st.multiselect("Select titles:", titles)
    if selected_titles:
        for title in selected_titles:
            st.subheader(title)
            generate_blog_post(title, language)

# Function to generate blog post titles based on keyword
def generate_titles(keyword):
    prompt = f"Generate blog post titles for the keyword '{keyword}'"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=5,
        stop=None,
        temperature=0.5,
    )
    titles = [choice.text.strip() for choice in response.choices]
    return titles

# Function to generate a blog post based on a title
def generate_blog_post(title, language):
    st.write(f"Generating a blog post for the title: '{title}'")
    prompt = f"Generate a blog post for the title '{title}' in {language}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    content = response.choices[0].text
    st.write(content)
