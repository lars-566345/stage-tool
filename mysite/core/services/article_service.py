from ..repositories.article_repository import *

class ArticleService:
    def __init__(self):
        self.article_repository = ArticleRepository()

    def get_all_articles(self):
        articles = self.article_repository.get_all_articles()
        if not articles:
            raise ValueError("No articles found")
        return articles

    def get_article_by_id(self, id: int):
        article = self.article_repository.get_article_by_id(id)
        if not article:
            raise ValueError("Article not found")
        return article