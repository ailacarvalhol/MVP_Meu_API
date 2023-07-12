from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    produto: str = "Body"
    tamanho: str = "P"
    quantidade: Optional[int] = 4
    

class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    produto: str = "Digite o nome do produto"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):

    """ Retorna uma representação do produto seguindo o schema definido em ProdutoViewSchema. 
    """

    result = []
    for produto in produtos:
        result.append({
            "produto": produto.produto,
            "tamanho": produto.tamanho,
            "quantidade": produto.quantidade,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):

    """ Define como um produto será retornado: produto + comentários.
    """

    id: int = 1
    produto: str = "Body"
    tamanho: str = "P"
    quantidade: Optional[int] = 12
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    produto: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "produto": produto.produto,
        "tamanho": produto.tamanho,
        "quantidade": produto.quantidade,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
