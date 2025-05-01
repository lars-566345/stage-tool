import graphene
from .queries.article_query import Query as ArticleQuery
from .mutations.article_mutation import ( CreateArticle, UpdateArticle, DeleteArticle )

class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()
    delete_article = DeleteArticle.Field()

class Query(ArticleQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
