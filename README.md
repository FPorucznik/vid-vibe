# vid-vibe

A sentiment analysis Python project that examines comments of a given youtube video to check the general reception of it. It uses the YouTube Data API v3 to fetch comments and the Natural Language Toolkit (NLTK) (an open-source library for natural language processing (NLP)) to determine the overall sentiment of the comments.

## Tech stack

- Python 3.12.1
- nltk 3.8.1
- YouTube Data API v3
- pandas 2.2.0

## Local setup guide

**Clone repo, head to project location and install necessary dependencies**

```
git clone https://github.com/FPorucznik/vid-vibe.git
cd vid-vibe
pip install -r requirements.txt
```

**Create .env file and add your own api key generated from YouTube Data API v3**

```
API_KEY=your-API-key-here
```

**Create directory for nltk necessary packages which will be downloaded automatically**

```
C:\Users\<your-user>\nltk_data
```

**Run app and provide a valid YouTube video ID for the input**

```
python app.y
```

**Example usage**

I selected a video with mostly positive feedback.

<img width="416" alt="comments1" src="https://github.com/FPorucznik/vid-vibe/assets/56200864/a0b6788e-f507-4087-b1b1-b231fdb12541">

First i copy the id from the URL:

<img width="222" alt="vidId" src="https://github.com/FPorucznik/vid-vibe/assets/56200864/ef8e0228-2787-43e4-b55b-5bc87886b991">

Then i enter it in the input and get the result:

<img width="191" alt="resultSentiment" src="https://github.com/FPorucznik/vid-vibe/assets/56200864/1aec4b5c-2b00-4d4d-aa10-8dd4028fe0d5">

