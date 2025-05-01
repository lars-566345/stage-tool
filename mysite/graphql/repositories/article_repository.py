from ..models.article import Article


def get_all_articles():
    try:
        return Article.objects.all()
    except Article.DoesNotExist:
        return None

def get_article_by_id(id: int):
    try:
        return Article.objects.get(id=id)
    except Article.DoesNotExist:
        return None