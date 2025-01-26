import openai

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

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
