from ..models.article import Article

class ArticleRepository:
    def get_all_articles(self):
        try:
            return Article.objects.all()
        except Article.DoesNotExist:
            return None

    def get_article_by_id(self, id: int):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return None
        
    
    def create_article(self, article: Article):
        try:
            return article.save()
        except Exception as e:
            return e

    def update_article(self, article: Article, title: str = None, content: str = None, status: str = None):
        try:
            if title is not None:
                article.title = title
            
            if content is not None:
                article.content = content
            
            if status is not None:
                article.status = status

            article.save()
            return True
        except Exception as e:
            return False
            
    def delete_article(self, id: int):
        try:
            article = self.get_article_by_id(id)
            article.delete()
            return True
        except Article.DoesNotExist:
            return False