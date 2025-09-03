import requests

from config import POSTS_API_URL

def fetch_posts(limit=10, page=1):
    """
    Fetch posts from JSONPlaceholder with pagination.

    Args:
        limit (int): Number of posts per page.
        page (int): Page number to fetch.

    Returns:
        list: A list of post dictionaries.
    """
    try:
        url = f"{POSTS_API_URL}?_limit={limit}&_page={page}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[Error] Failed to fetch posts: {e}")
        return []
    except Exception as e:
        print(f"[Unexpected Error] Something went wrong: {e}")
        return []
