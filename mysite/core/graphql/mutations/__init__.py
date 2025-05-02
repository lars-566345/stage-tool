import graphene
from .article_mutation import CreateArticle, UpdateArticle, DeleteArticle

class Mutation(
    CreateArticle,
    UpdateArticle,
    DeleteArticle,
    graphene.ObjectType
):
    pass
