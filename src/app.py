from flask import Flask, redirect, render_template_string, request, url_for

from database import conectar
from models import criar_tabela

app = Flask(__name__)
criar_tabela()

PAGINA = PAGINA = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>TaskFlow</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body class="bg-light">

    <nav class="navbar navbar-dark bg-primary">
        <div class="container">
            <span class="navbar-brand mb-0 h1">
                TaskFlow
            </span>
        </div>
    </nav>

    <main class="container py-5">

        <div class="text-center mb-5">
            <h1 class="fw-bold">Gerenciamento de Tarefas</h1>

            <p class="text-secondary">
                Organize, acompanhe e conclua as atividades da equipe.
            </p>
        </div>

        <div class="row g-4">

            <div class="col-lg-5">

                <div class="card shadow-sm">
                    <div class="card-body">

                        <h2 class="h4 mb-4">
                            Nova tarefa
                        </h2>

                        <form method="POST" action="/criar">

                            <div class="mb-3">
                                <label
                                    for="titulo"
                                    class="form-label"
                                >
                                    Título
                                </label>

                                <input
                                    type="text"
                                    id="titulo"
                                    name="titulo"
                                    class="form-control"
                                    placeholder="Digite o título da tarefa"
                                    required
                                >
                            </div>

                            <div class="mb-3">
                                <label
                                    for="descricao"
                                    class="form-label"
                                >
                                    Descrição
                                </label>

                                <textarea
                                    id="descricao"
                                    name="descricao"
                                    class="form-control"
                                    rows="4"
                                    placeholder="Descreva a atividade"
                                ></textarea>
                            </div>

                            <button
                                type="submit"
                                class="btn btn-primary w-100"
                            >
                                Cadastrar tarefa
                            </button>

                        </form>

                    </div>
                </div>

            </div>

            <div class="col-lg-7">

                <div class="card shadow-sm">
                    <div class="card-body">

                        <h2 class="h4 mb-4">
                            Tarefas cadastradas
                        </h2>

                        {% if tarefas %}

                            <div class="list-group">

                                {% for tarefa in tarefas %}

                                    <div class="list-group-item">

                                        <div
                                            class="d-flex justify-content-between align-items-start gap-3"
                                        >

                                            <div>

                                                <h3 class="h5 mb-1">
                                                    {{ tarefa[1] }}
                                                </h3>

                                                <p class="text-secondary mb-2">
                                                    {{ tarefa[2] or "Sem descrição" }}
                                                </p>

                                                {% if tarefa[3] == 1 %}

                                                    <span class="badge bg-success">
                                                        Concluída
                                                    </span>

                                                {% else %}

                                                    <span class="badge bg-warning text-dark">
                                                        Pendente
                                                    </span>

                                                {% endif %}

                                            </div>

                                            <div class="d-flex gap-2">

                                                {% if tarefa[3] == 0 %}

                                                    <a
                                                        href="/concluir/{{ tarefa[0] }}"
                                                        class="btn btn-success btn-sm"
                                                    >
                                                        Concluir
                                                    </a>

                                                {% endif %}

                                                <a
                                                    href="/excluir/{{ tarefa[0] }}"
                                                    class="btn btn-outline-danger btn-sm"
                                                    onclick="return confirm('Deseja excluir esta tarefa?')"
                                                >
                                                    Excluir
                                                </a>

                                            </div>

                                        </div>

                                    </div>

                                {% endfor %}

                            </div>

                        {% else %}

                            <div class="alert alert-secondary mb-0">
                                Nenhuma tarefa cadastrada.
                            </div>

                        {% endif %}

                    </div>
                </div>

            </div>

        </div>

    </main>

</body>
</html>
"""


@app.route("/")
def inicio():
    conexao = conectar()
    tarefas = conexao.execute(
        "SELECT id, titulo, descricao, concluida FROM tarefas ORDER BY id DESC"
    ).fetchall()
    conexao.close()

    return render_template_string(PAGINA, tarefas=tarefas)


@app.route("/criar", methods=["POST"])
def criar_tarefa():
    titulo = request.form.get("titulo", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not titulo:
        return "O título é obrigatório.", 400

    conexao = conectar()
    conexao.execute(
        "INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)",
        (titulo, descricao),
    )
    conexao.commit()
    conexao.close()

    return redirect(url_for("inicio"))


@app.route("/concluir/<int:tarefa_id>")
def concluir_tarefa(tarefa_id):
    conexao = conectar()
    conexao.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (tarefa_id,),
    )
    conexao.commit()
    conexao.close()

    return redirect(url_for("inicio"))


@app.route("/excluir/<int:tarefa_id>")
def excluir_tarefa(tarefa_id):
    conexao = conectar()
    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (tarefa_id,),
    )
    conexao.commit()
    conexao.close()

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)