import datetime
import praw
import json
from typing import List, Dict



def load_config(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        raise Exception(f"Config file not found at {file_path}")
    except json.JSONDecodeError:
        raise Exception(f"Invalid JSON format in the config file at {file_path}")
    
config = load_config('config.json')


def search_subreddit(subreddit_name: str, keyword: str, sort: str, time_filter: str, limit: int) -> List[Dict]:
    # Load configuration from the config file
    
    reddit = praw.Reddit(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        user_agent=config['user_agent']
    )
    
    subreddit = reddit.subreddit(subreddit_name)
    search_results = []

    # Use sort parameter directly
    print(f"""
        Buscando:
          \t Busqueda: {keyword}, 
          \t Orden: {sort}, 
          \t Filtro de tiempo: {time_filter},
          \t Numero maximo de resultados: {limit}""")

    submissions = subreddit.search(keyword, sort="hot", time_filter=time_filter.lower(), limit=limit)

    for submission in submissions:
        # Extract additional information
        search_results.append({
            "title": submission.title,
            "url": submission.url,
            "score": submission.score,
            "created_utc": submission.created_utc,  # Timestamp of the submission
            "body": submission.selftext,  # Body text of the submission, empty for link posts
            "image_urls": [url for url in submission.preview['images'][0]['resolutions']] if hasattr(submission, 'preview') else [],  # List of image URLs if available
            "author": str(submission.author),  # Author of the submission
            "comments_count": submission.num_comments  # Number of comments on the submission
        })

    return search_results

# Example usage of the search_subreddit function
if __name__ == "__main__":
    subreddit_results = search_subreddit('subreddit_name', 'keyword', 'hot', 'day', 10)
    print(subreddit_results)
