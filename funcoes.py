import random
import csv


def embaralhar_perguntas(perguntas):
    random.shuffle(perguntas)

def mostrar_perguntas(pergunta):
    print()
    print(pergunta["pergunta"])

    for i, alternativa in enumerate(pergunta["alternativas"]):
        print(f"{i}: {alternativa}")

def verificar_resposta(pergunta, resposta_usuario):
    return resposta_usuario == pergunta["resposta"]


def atualizar_pontos(acertou, pontos):

    if acertou:
        pontos += 1

    return pontos


def salvar_ranking(nome, pontos):

    with open(
        "ranking.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            nome,
            pontos
        ])


def carregar_ranking():

    ranking = []

    try:

        with open(
            "ranking.csv",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.reader(arquivo)

            for linha in leitor:

                ranking.append({
                    "nome": linha[0],
                    "pontos": int(linha[1])
                })

    except FileNotFoundError:

        pass

    return ranking


def ordenar_ranking(ranking):

    ranking.sort(
        key=lambda jogador: jogador["pontos"],
        reverse=True
    )

    return ranking
