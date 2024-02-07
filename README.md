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

First i copy the id:

Then i enter it in the input and get the result:
