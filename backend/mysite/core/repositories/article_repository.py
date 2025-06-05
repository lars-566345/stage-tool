from ..models.fix import KnowledgeBaseArticle
import logging

logger = logging.getLogger(__name__)

class ArticleRepository:
    def get_all_articles(self):
        try:
            logger.info("Getting all articles")
            return KnowledgeBaseArticle.objects.all()
        except KnowledgeBaseArticle.DoesNotExist:
            logger.exception("An error occurred getting all Articles. No articles exist!")
            return None

    def get_article_by_id(self, id: int):
        try:
            logger.info("Getting article by id")
            return KnowledgeBaseArticle.objects.get(id=id)
        except KnowledgeBaseArticle.DoesNotExist:
            logger.exception("An error occurred getting the Article. The article with that id does not exist!")
            return None

    def create_article(self, article: KnowledgeBaseArticle):
        try:
            logger.info("Creating a new article")
            return article.save()
        except Exception as e:
            logger.exception("An error occurred while creating the Article.")
            return e

    def update_article(self, article: KnowledgeBaseArticle, title: str = None, content: str = None):
        try:
            logger.info(f"Updating article with id {article.id}")
            if title is not None:
                article.title = title

            if content is not None:
                article.content = content

            article.save()
            return True
        except Exception as e:
            logger.exception(f"An error occurred while updating the Article with id {getattr(article, 'id', None)}.")
            return False

    def delete_article(self, id: int):
        try:
            logger.info(f"Deleting article with id {id}")
            article = self.get_article_by_id(id)
            article.delete()
            return True
        except KnowledgeBaseArticle.DoesNotExist:
            logger.exception(f"An error occurred while deleting the Article. The article with id {id} does not exist!")
            return False