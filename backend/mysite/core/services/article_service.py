from ..repositories.article_repository import *
from ..repositories.profile_repository import *

class ArticleService:
    def __init__(self):
        self.article_repository = ArticleRepository()
        self.profile_repository = ProfileRepository()

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
    
    def create_article(self, title: str, content: str, status: int, author: int):
        author_instance = self.profile_repository.get_profile_by_user_id(author)

        if not author_instance:
            raise ValueError("Profile not found")
        
        new_article_instance = Article(title=title, content=content, status=status, author=author_instance)

        self.article_repository.create_article(new_article_instance)

    def update_article(self, id: int, title: str = None, content: str = None, status: int = None):
        article_instance = self.article_repository.get_article_by_id(id)

        if not article_instance:
            raise ValueError("Article not found")
        
        self.article_repository.update_article(article_instance, title, content, status)


    def delete_article(self, id: int):
        article_instance = self.article_repository.get_article_by_id(id)

        if not article_instance:
            raise ValueError("Article not found")
        
        self.article_repository.delete_article(id)