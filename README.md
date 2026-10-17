# SmartRecruit-AI-Resume-Analyzer-Matcher-
My Personal HR
# 📄 SmartRecruit: AI Resume Analyzer & Prep Coach

SmartRecruit is a web-based document intelligence system built for Semester 1 evaluations. The application allows hiring metrics teams or students to upload resume PDF attachments alongside raw text job guidelines to automatically generate profile matching percentages, detect skill gaps, and script mock technical questions.

## 🛠️ Tech Stack and Libraries
- **Language Layer:** Python 3.x
- **Web UI Engine:** Streamlit Framework Matrix
- **Document Parser:** PyPDF Vector Extractors
- **AI Inferencing:** Google Gemini Client SDK (`gemini-2.5-flash`)

## ⚙️ How to Deploy Locally

1. **Clone the project repository workspace:**
   ```bash
   git clone https://github.com
   cd SmartRecruit
   ```

2. **Assemble the package environment requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Access Credentials:**
   Open `config.py` and assign your Google AI Studio configuration token to the variable placeholder fields.

4. **Launch the Web App Framework server:**
   ```bash
   streamlit run app.py
   ```
