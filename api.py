import googleapiclient.discovery
import os
from dotenv import load_dotenv
from googleapiclient.errors import HttpError

load_dotenv()


def get_comments_from_video(videoId: str) -> dict:
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('API_KEY')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.commentThreads().list(
        part='snippet',
        videoId=videoId,
        maxResults=100
    )
    try:
        response = request.execute()
    except HttpError as error:
        return {
            'error_message': error._get_reason(),
            'status_code': error.resp.status
        }
    else:
        return response
