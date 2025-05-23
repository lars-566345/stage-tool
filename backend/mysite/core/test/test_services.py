from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Article
from core.services.article_service import ArticleService

class ArticleServiceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="jane", password="secret")
        self.article = Article.objects.create(title="Test", content="Sample", status=1)
        self.article_service = ArticleService()

    def test_get_by_id_returns_article(self):
        result = self.article_service.get_article_by_id(self.article.id)
        self.assertEqual(result, self.article)
