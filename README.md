## This repository features an application that utilizes Google Gemini Pro and Streamlit to transcribe and summarize YouTube videos.

## Installation

1. Clone the repository:

git clone ""

2. Install dependencies:

pip install -r requirements1.txt

3. Configure Google Gemini Pro API.

4. Run the app:

streamlit run web-app.py

## Now put the video link and you can get the summary of the video.

## If you get an error for 'Error extracting transcript' try running the below command

## Firstly try clicking the button "Get detailed notes" twice if that doesnt work try this:

pip install --upgrade youtube-transcript-api

## If you want to ask any further questions about the video you can have to run the docker locally for that

## to get the prerequisites visit these links:

## https://dsg-iit-roorkee.gitbook.io/dsg-iit-roorkee-bootcamp/module-5-hands-on-development/prerequisites-must

## https://dsg-iit-roorkee.gitbook.io/dsg-iit-roorkee-bootcamp/module-5-hands-on-development/docker-basics

## After the prerequisites are done run the following commands on powershell:
## inside the demo1 folder

docker build -t rag .

docker run -v "${PWD}/data:/app/data" -p 8000:8000 rag 

## ---- {PWD is your working directory}

## Now the server is up you can ask any question with the following prompt in another terminal

$body = @{
    prompt = "Your Question"
}

Invoke-RestMethod -Method Post -Uri "http://localhost:8000/v1/pw_ai_answer" -ContentType "application/json" -Body ($body | ConvertTo-Json)

## Thanks