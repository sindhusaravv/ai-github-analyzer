import streamlit as st

st.title("AI GitHub Profile Analyzer")

github_link = st.text_input("Enter your GitHub profile link")

if st.button("Analyze"):
    if github_link:
        st.subheader("Analysis Result")

        st.write("GitHub Score: 7/10")

        st.write("Suggestions:")
        st.write("- Add more projects")
        st.write("- Improve README files")
        st.write("- Include project demos")

        st.write("Top Recommendation:")
        st.write("Build one strong AI/ML project to stand out")
    else:
        st.write("Please enter a valid GitHub link")
