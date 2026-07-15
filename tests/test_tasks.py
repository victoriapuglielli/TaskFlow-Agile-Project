import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")),
)

from app import app


def test_pagina_inicial():
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert b"TaskFlow" in resposta.data


def test_criacao_sem_titulo():
    cliente = app.test_client()

    resposta = cliente.post(
        "/criar",
        data={"titulo": "", "descricao": "Teste"},
    )

    assert resposta.status_code == 400
    assert b"obrigat" in resposta.data