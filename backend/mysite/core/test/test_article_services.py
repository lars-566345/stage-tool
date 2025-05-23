from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Article, Profile
from core.services.article_service import ArticleService

class ArticleServiceTest(TestCase):
    def setUp(self):
        self.article_service = ArticleService()
        self.user = User.objects.create_user(username="jane", password="secret")
        self.profile = Profile.objects.get(user=self.user)
        self.article = Article.objects.create(title="Test", content="Sample", status=1)
        self.article_2 = Article.objects.create(title="Test2", content="Sample2", status=2)

    def test_get_by_id_returns_article(self):
        result = self.article_service.get_article_by_id(self.article.id)
        self.assertEqual(result, self.article)
    
    def test_get_all_articles_returns_articles(self):
        result = self.article_service.get_all_articles()
        self.assertEqual(len(result), 2)
    
    def test_create_article_successfully(self):
        self.article_service.create_article(
            title="Real Article",
            content="Some content",
            status=1,
            author=self.profile.id
        )

        article = Article.objects.get(title="Real Article")
        self.assertEqual(article.content, "Some content")
        self.assertEqual(article.status, 1)
        self.assertEqual(article.author, self.profile)


    def test_update_article_successfully(self):
        self.article_service.update_article(
            id=self.article.id,
            title="New Title",
            content="Updated content",
            status=1
        )

        updated_article = Article.objects.get(id=self.article.id)
        self.assertEqual(updated_article.title, "New Title")
        self.assertEqual(updated_article.content, "Updated content")
        self.assertEqual(updated_article.status, 1)



    def test_delete_article_successfully(self):
        self.assertTrue(Article.objects.filter(id=self.article.id).exists())
        self.article_service.delete_article(id=self.article.id)
        self.assertFalse(Article.objects.filter(id=self.article.id).exists())