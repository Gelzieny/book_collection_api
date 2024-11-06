from ninja import Query, Router

from .models import Categorias, Livros
from .schemas import AvaliacaoSchema, FiltrosSortear, LivroSchema


livros_router = Router()

@livros_router.post('/', response={200: LivroSchema})
def create_livros(request,  livro_schema: LivroSchema):
  nome = livro_schema.dict()['nome']
  streaming = livro_schema.dict()['streaming']
  categorias = livro_schema.dict()['categorias']

  if streaming not in ['N', 'F', 'A']:
    return 400, {'status': 'Erro: Streaming deve ser N, F ou A'}
  
  livro = Livros(nome=nome, streaming=streaming)
  
  livro.save()

  for categoria in categorias:
    categoria_temp = Categorias.objects.get(id=categoria)
    livro.categorias.add(categoria_temp)

  livro.save()

  return livro

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id: int, avaliacao_schema: AvaliacaoSchema):
  
  comentarios = avaliacao_schema.dict()['comentarios']
  nota = avaliacao_schema.dict()['nota']
  livro = Livros.objects.get(id=livro_id)
  livro.comentarios = comentarios
  livro.nota = nota
  
  livro.save()
  return {'status': 'Avaliação realizada com sucesso'}

@livros_router.delete('/{livro_id}')
def deletar_livro(request, livro_id: int):
  livro = Livros.objects.get(id=livro_id)
  livro.delete()
  return {'status': f'Livro com (ID: {livro_id}) deletado com sucesso'}

@livros_router.get('/sortear/', response={200: LivroSchema, 404: dict})
def sortear_livro(request, filtros: Query[FiltrosSortear]):
  nota_minima = filtros.dict()['nota_minima']

  categoria = filtros.dict()['categorias']
  reassistir = filtros.dict()['reassistir']
  livros = Livros.objects.all()
  
  if not reassistir:
    livros = livros.filter(nota=None)
  if nota_minima:
    livros = livros.filter(nota__gte=nota_minima)
  if categoria:
    livros = livros.filter(categorias__id=categoria)
  livro = livros.order_by('?').first()
  
  if livros.count() > 0:
    return 200, livro
  else:
    return 404, {'status': 'Livro não encontrado'}