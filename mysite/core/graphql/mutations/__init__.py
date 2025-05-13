import graphene

from .article_mutation import CreateArticle, UpdateArticle, DeleteArticle

from .evaluation_mutation import CreateEvaluation
 
class Mutation(graphene.ObjectType):

    create_article = CreateArticle.Field()

    update_article = UpdateArticle.Field()

    delete_article = DeleteArticle.Field()

    create_evaluation = CreateEvaluation.Field() 