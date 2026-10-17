import streamlit as st
import pypdf
from google import genai
import config
import sys

# Configure basic web layout parameters
st.set_page_config(page_title=config.APP_TITLE, layout="wide")

def extract_text_from_pdf(uploaded_file):
    """Reads an uploaded binary PDF document stream and extracts raw text."""
    try:
        pdf_reader = pypdf.PdfReader(uploaded_file)
        extracted_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
        return extracted_text.strip()
    except Exception as e:
        st.error(f"Error parsing PDF structural data: {str(e)}")
        return None

def analyze_resume_package(resume_text, job_description):
    """Dispatches the paired data packages to Gemini API for analytical processing."""
    try:
        # Initialize Google GenAI client ecosystem securely using config keys
        client = genai.Client(api_key=config.GEMINI_API_KEY)
        
        analysis_prompt = f"""
        You are an expert technical recruiter and interview coach. Analyze the provided resume text against the target job description.
        
        RESUME TEXT:
        {resume_text}
        
        JOB DESCRIPTION:
        {job_description}
        
        Provide your comprehensive evaluation structured exactly under these markdown headings:
        ### 📊 Job Alignment Match Score
        Give a clear profile matching percentage score (e.g., 75%) along with a short 2-sentence summary justification.
        
        ### 🔑 Core Keyword and Skill Gaps
        List out specific industry keywords, certifications, framework stacks, or tools missing from the resume that were emphasized in the job description.
        
        ### 🎯 Tailored Technical Interview Questions
        Generate 3 custom technical interview questions designed specifically to test this candidate based on their background and this role.
        """
        
        response = client.models.generate_content(
            model=config.MODEL_ENGINE,
            contents=analysis_prompt
        )
        return response.text
    except Exception as e:
        return f"Operational Error linking to AI cloud processors: {str(e)}"

# Define Streamlit Web User Interface View Elements
st.title("📄 SmartRecruit")
st.subheader("AI-Powered Resume Matcher & Interview Prep Companion")
st.write("Upload a target candidate profile PDF and input the corresponding corporate job criteria to evaluate architectural alignment.")

st.divider()

# Create dynamic side-by-side display columns
col1, col2 = st.columns(2)

with col1:
    st.write("### 📤 Step 1: Upload Candidate Profile")
    uploaded_resume = st.file_uploader("Choose a Resume file (PDF format only)", type=["pdf"])

with col2:
    st.write("### 📝 Step 2: Input Job Specifications")
    job_desc_input = st.text_area("Paste the target job description requirements here...", height=200)

st.divider()

st.write("### ⚡ Step 3: Run Match Evaluation")
if st.button("Analyze Application Package", type="primary"):
    # Input validation checks
    if not config.GEMINI_API_KEY or config.GEMINI_API_KEY == "YOUR_SECURE_API_KEY_HERE":
        st.error("Configuration Error: Active Gemini API Key binding missing inside config.py profile context.")
    elif not uploaded_resume:
        st.warning("Please upload a valid candidate resume document before processing.")
    elif not job_desc_input.strip():
        st.warning("Please provide a corporate job criteria description to match against.")
    else:
        with st.spinner("Analyzing text fields and generating recruitment metrics..."):
            # Execute text parsing logic
            parsed_resume_text = extract_text_from_pdf(uploaded_resume)
            
            if parsed_resume_text:
                # Dispatch data structures to Gemini engine
                evaluation_results = analyze_resume_package(parsed_resume_text, job_desc_input)
                
                # Render results out visually
                st.success("Analysis Complete!")
                st.markdown(evaluation_results)
