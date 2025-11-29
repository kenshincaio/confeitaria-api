from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify

def get_cardapio():
    cardapio = [
        {
            'id': 1,
            'titulo': 'Bolo de Chocolate',
            'descricao': 'Delicioso bolo de chocolate',
            'foto': ''
        },
        {
            'id': 2,
            'titulo': 'Bolo de Morango',
            'descricao': 'Delicioso bolo de morango',
            'foto': ''
        }
    ]
    return cardapio