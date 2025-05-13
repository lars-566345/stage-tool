from ..repositories.article_repository import *
from ..repositories.user_repository import *

class ArticleService:
    def __init__(self):
        self.article_repository = ArticleRepository()
        self.user_repository = UserRepository()

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
    
    def create_article(self, title, content, status, author):
        author_instance = self.user_repository.get_user_by_id(author)

        if not author_instance:
            raise ValueError("User not found")
        
        new_article_instance = Article(title=title, content=content, status=status, author=author_instance)

        self.article_repository.create_article(new_article_instance)