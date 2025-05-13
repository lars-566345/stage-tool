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
            # return Article.objects.create(title=article.title, content=article.content, status=article.status, author=article.author)
        except Exception as e:
            return e

    def update_article(self, article: Article):
        try:
            for field in article._meta.fields:
                field_name = field.name

                if field_name == 'id':
                    continue

                setattr(article, field_name, getattr(article, field_name))

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