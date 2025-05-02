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