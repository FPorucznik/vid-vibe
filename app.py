from api import get_comments_from_video
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd

import nltk
nltk.download(['vader_lexicon', 'stopwords', 'punkt', 'wordnet'])

sentiment_intensity_analyzer = SentimentIntensityAnalyzer()


def app():
    videoId = input('Input video ID: ')
    response = get_comments_from_video(videoId)

    if 'error_message' in response:
        print(f'API Error:\nStatus code: {response['status_code']}\nmessage: {response['error_message']}')
    elif response['items']:
        df = process_response(response['items'])
        df['comment'] = df['comment'].apply(preprocess_comment)
        df['sentiment'] = df['comment'].apply(get_comment_sentiment)

        most_frequent_sentiment = df['sentiment'].mode()[0]
        print(f'The overall sentiment is: {most_frequent_sentiment}')
    else:
        print('The given video has no comments')


def process_response(items: list) -> pd.DataFrame:
    comments = []
    for item in items:
        comments.append(
            item['snippet']['topLevelComment']['snippet']['textDisplay']
        )

    df = pd.DataFrame(comments, columns=['comment'])
    return df


def preprocess_comment(comment: str) -> str:
    tokens = word_tokenize(comment.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_result = ' '.join(lemmatized_tokens)
    return processed_result


def get_comment_sentiment(comment: str) -> str:
    scores = sentiment_intensity_analyzer.polarity_scores(comment)

    compound_score = scores['compound']
    positive_threshold = 0.2
    negative_threshold = -0.2

    if compound_score > positive_threshold:
        return 'positive'
    elif compound_score < negative_threshold:
        return 'negative'
    else:
        return 'neutral'


if __name__ == '__main__':
    app()
