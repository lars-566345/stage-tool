import graphene
from .article_mutation import CreateArticle, UpdateArticle, DeleteArticle
from .evaluation_mutation import CreateEvaluation

class Mutation(
    CreateArticle,
    UpdateArticle,
    DeleteArticle,

    CreateEvaluation,
    graphene.ObjectType
):
    pass
