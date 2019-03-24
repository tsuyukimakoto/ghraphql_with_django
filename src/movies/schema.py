import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import Actor, Movie


class ActorType(DjangoObjectType):  
    class Meta:
        model = Actor


class MovieType(DjangoObjectType):  
    class Meta:
        model = Movie


class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)

    def resolve_actor(self, info, **kwargs):
        _id = kwargs.get('id')
        if _id is not None:
            return Actor.objects.get(pk=_id)
        return None

    def resolve_movie(self, info, **kwargs):
        _id = kwargs.get('id')
        if _id is not None:
            return Movie.objects.get(pk=id)
        return None

    def resolve_actors(self, info, **kwargs):
        return Actor.objects.all()

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()
