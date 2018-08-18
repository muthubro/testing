import graphene
from ingredients.schema import Query as ingredientsQuery

class Query(ingredientsQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)