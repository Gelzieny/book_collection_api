from ninja import ModelSchema, Schema
from .models import Livros


class AvaliacaoSchema(ModelSchema):
  class Meta:
    model = Livros
    fields = ['nota', 'comentarios']