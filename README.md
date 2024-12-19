# YouTube Video Transcription and Summarization App

This repository contains an application that utilizes **Google Gemini Pro** and **Streamlit** to transcribe and summarize YouTube videos. Additionally, it supports asking further questions about the video content using a Docker-based local server.

---

## Features
- Transcribe YouTube videos.
- Summarize video content.
- Ask follow-up questions about video content (requires Docker).

---

## Installation

### Prerequisites
- Python 3.10 or above 
- Docker (for advanced features)

### Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements1.txt
   ```

3. **Configure Google Gemini Pro API**
   - Set up your Google Gemini Pro API credentials as per the official documentation.

4. **Run the app:**
   ```bash
   streamlit run web-app.py
   ```

   - Open the provided local URL in your browser.
   - Enter the YouTube video link to get the summary.

---

## Troubleshooting

### Error: `Error extracting transcript`
1. Try clicking the **"Get detailed notes"** button twice.
2. If the error persists, upgrade the YouTube Transcript API:
   ```bash
   pip install --upgrade youtube-transcript-api
   ```

---

## Advanced Features: Asking Questions

To enable the Q&A feature, you need to run the application using Docker.

### Prerequisites
- Complete the prerequisites from these links:
  - [Development Prerequisites](https://dsg-iit-roorkee.gitbook.io/dsg-iit-roorkee-bootcamp/module-5-hands-on-development/prerequisites-must)
  - [Docker Basics](https://dsg-iit-roorkee.gitbook.io/dsg-iit-roorkee-bootcamp/module-5-hands-on-development/docker-basics)

### Steps

1. **Navigate to the `demo1` folder:**
   ```bash
   cd demo1
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t rag .
   ```

3. **Run the Docker container:**
   ```bash
   docker run -v "${PWD}/data:/app/data" -p 8000:8000 rag
   ```

   - `{PWD}` refers to your current working directory.

4. **Ask questions about the video:**
   In a new terminal, run the following command:
   ```powershell
   $body = @{ prompt = "Your Question" }
   Invoke-RestMethod -Method Post -Uri "http://localhost:8000/v1/pw_ai_answer" -ContentType "application/json" -Body ($body | ConvertTo-Json)
   ```

---

## Notes
- Ensure all dependencies are correctly installed.
- Use Docker for enhanced functionality such as follow-up questions.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
