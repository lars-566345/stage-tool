from ..repositories.article_repository import *


def get_all_articles():
    articles = get_all_articles()
    if not articles:
        raise ValueError("No articles found")
    return articles

def get_article_by_id(id: int):
    article = get_article_by_id(id)
    if not article:
        raise ValueError("Article not found")
    return article