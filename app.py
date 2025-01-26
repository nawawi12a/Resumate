import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

# Function to generate a resume
def generate_resume(job_title, skills, experience):
    prompt = f"""
    Create a professional resume for a {job_title} with the following skills: {skills}. 
    The candidate has {experience} years of experience. Include sections for:
    - Contact Information
    - Summary
    - Skills
    - Experience
    - Education
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to generate a cover letter
def generate_cover_letter(job_title, company, skills, experience):
    prompt = f"""
    Write a professional cover letter for a {job_title} position at {company}. 
    The candidate has {experience} years of experience and the following skills: {skills}.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# App title and description
st.set_page_config(page_title="Resumate", page_icon="📄", layout="wide")
st.title("📄 Resumate - AI-Powered Resume Builder")
st.write("Create, upload, or write your resume in minutes!")

# Sidebar for user input
with st.sidebar:
    st.header("Choose Your Option")
    option = st.radio("How would you like to submit your resume?", ("Write Resume", "Upload Resume", "Generate Resume with AI"))

# Option 1: Write Resume
if option == "Write Resume":
    st.header("Write Your Resume")
    resume_text = st.text_area("Write your resume here:", height=300, placeholder="Paste or type your resume here...")
    if st.button("Submit Written Resume"):
        if resume_text.strip():
            st.success("Resume submitted successfully!")
            st.subheader("Your Resume")
            st.write(resume_text)
            st.download_button("Download Resume", resume_text, file_name="resume.txt")
        else:
            st.error("Please write or paste your resume.")

# Option 2: Upload Resume
elif option == "Upload Resume":
    st.header("Upload Your Resume")
    uploaded_file = st.file_uploader("Choose a file (PDF or TXT)", type=["pdf", "txt"])
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            st.warning("PDF files are not editable. Please upload a TXT file or write your resume.")
        else:
            resume_text = uploaded_file.read().decode("utf-8")
            st.success("Resume uploaded successfully!")
            st.subheader("Your Resume")
            st.write(resume_text)
            st.download_button("Download Resume", resume_text, file_name="resume.txt")

# Option 3: Generate Resume with AI
elif option == "Generate Resume with AI":
    st.header("Generate Resume with AI")
    job_title = st.text_input("Job Title", placeholder="e.g., Software Engineer")
    skills = st.text_area("Skills", placeholder="e.g., Python, JavaScript, React")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=1)
    company = st.text_input("Company Name (for cover letter)", placeholder="e.g., Google")

    if st.button("Generate Resume"):
        if job_title and skills and experience:
            with st.spinner("Generating your resume..."):
                resume = generate_resume(job_title, skills, experience)
                st.subheader("Your AI-Generated Resume")
                st.write(resume)
                st.download_button("Download Resume", resume, file_name="resume.txt")
        else:
            st.error("Please fill in all fields.")

    if st.button("Generate Cover Letter"):
        if job_title and skills and experience and company:
            with st.spinner("Generating your cover letter..."):
                cover_letter = generate_cover_letter(job_title, company, skills, experience)
                st.subheader("Your AI-Generated Cover Letter")
                st.write(cover_letter)
                st.download_button("Download Cover Letter", cover_letter, file_name="cover_letter.txt")
        else:
            st.error("Please fill in all fields.")
