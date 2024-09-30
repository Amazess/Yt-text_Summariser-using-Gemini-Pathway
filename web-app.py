import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Loading the environment variables
load_dotenv()
genai.configure(api_key="")

# Prompt Summarizing
prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing summary in points. Please provide the summary of the text given here:  """

# Function to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript: {str(e)}")
        return None

# Function to generate summary using Google Gemini
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit interface

# Add custom CSS for circular logo
st.markdown("""
    <style>
    .circular-logo {
        border-radius: 50%;
        width: 100px; /* Set width */
        height: 100px; /* Set height */
        object-fit: cover; /* Maintain aspect ratio */
    }
    </style>
""", unsafe_allow_html=True)

# Add the logo to the top of the app
logo_path = r"C:\Users\visha\project\assets\logo1.png"  # Use raw string to avoid issues with backslashes
st.image(logo_path, width=85, use_column_width=False, output_format="auto")  # Display the logo

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    with st.spinner("Extracting transcript..."):
        transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        with st.spinner("Generating summary..."):
            summary = generate_gemini_content(transcript_text, prompt)
        
        # Display the summary in the app
        st.markdown("## Detailed Notes:")
        st.write(summary)

        # Provide options to download the summary and transcript
        save_folder = "demo1/data"  # Specify the folder to save summaries
        os.makedirs(save_folder, exist_ok=True)  # Create the folder if it doesn't exist
        
        # Unique file names
        summary_file_name = f"{video_id}_summary.txt"
        transcript_file_name = f"{video_id}_transcript.txt"

        # Save the summary to a file
        # summary_file_path = os.path.join(save_folder, summary_file_name)
        # with open(summary_file_path, "w") as file:
        #     file.write(summary)  # Write the summary to the file

        # Save the transcript to a file
        transcript_file_path = os.path.join(save_folder, transcript_file_name)
        with open(transcript_file_path, "w") as file:
            file.write(transcript_text)  # Write the transcript to the file

        # Provide download buttons
        st.download_button(
            label="Download Summary",
            data=summary,
            file_name=summary_file_name,
            mime="text/plain",
        )
        st.download_button(
            label="Download Transcript",
            data=transcript_text,
            file_name=transcript_file_name,
            mime="text/plain",
        )

# Add instructions at the bottom for better user experience
with st.expander("Instructions", expanded=False):
    st.write("""
        - Paste the YouTube video URL into the input box.
        - The video thumbnail will appear for confirmation.
        - Click 'Get Detailed Notes' to generate a summarized transcript.
        - You can download both the summary and the transcript as text files.
    """)

# Footer section
st.markdown("---")
st.markdown("Built with ❤ by Swapnil and Vishal  ")