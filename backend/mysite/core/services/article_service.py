from ..repositories.article_repository import *
from ..repositories.coach_profile_repository import *
import logging

logger = logging.getLogger(__name__)

class ArticleService:
    def __init__(self):
        self.article_repository = ArticleRepository()
        self.profile_repository = CoachProfileRepository()

    def get_all_articles(self):
        logger.info("Fetching all articles")
        articles = self.article_repository.get_all_articles()
        if not articles:
            logger.warning("No articles found")
            raise ValueError("No articles found")
        logger.info(f"Found {len(articles)} articles")
        return articles

    def get_article_by_id(self, id: int):
        logger.info(f"Fetching article with id {id}")
        article = self.article_repository.get_article_by_id(id)
        if not article:
            logger.warning(f"Article with id {id} not found")
            raise ValueError("Article not found")
        logger.info(f"Article with id {id} found")
        return article
    
    def create_article(self, title: str, content: str, author: int):
        logger.info(f"Creating article with title '{title}' by author {author}")
        author_instance = self.profile_repository.get_profile_by_user_id(author)

        if not author_instance:
            logger.error(f"Profile for author {author} not found")
            raise ValueError("Profile not found")
        
        new_article_instance = KnowledgeBaseArticle(title=title, content=content, author=author_instance)
        self.article_repository.create_article(new_article_instance)
        logger.info(f"Article '{title}' created successfully")

    def update_article(self, id: int, title: str = None, content: str = None, status: int = None):
        logger.info(f"Updating article with id {id}")
        article_instance = self.article_repository.get_article_by_id(id)

        if not article_instance:
            logger.warning(f"Article with id {id} not found")
            raise ValueError("Article not found")
        
        self.article_repository.update_article(article_instance, title, content, status)
        logger.info(f"Article with id {id} updated successfully")

    def delete_article(self, id: int):
        logger.info(f"Deleting article with id {id}")
        article_instance = self.article_repository.get_article_by_id(id)

        if not article_instance:
            logger.warning(f"Article with id {id} not found")
            raise ValueError("Article not found")
        
        self.article_repository.delete_article(id)
        logger.info(f"Article with id {id} deleted successfully")