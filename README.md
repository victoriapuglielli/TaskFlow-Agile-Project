# TaskFlow

Sistema Web desenvolvido em Python utilizando Flask para gerenciamento de tarefas.

---

## Objetivo

O TaskFlow foi desenvolvido como projeto da disciplina de Engenharia de Software.

O sistema permite:

- cadastrar tarefas
- listar tarefas
- concluir tarefas
- excluir tarefas

---

## Tecnologias utilizadas

- Python 3.13
- Flask
- SQLite
- HTML
- Bootstrap 5
- Pytest
- Git
- GitHub Actions

---

## Estrutura do projeto

```
TaskFlow-Agile-Project/

│

├── .github/

│ └── workflows/

│ └── tests.yml

│

├── docs/

│

├── src/

│ ├── app.py

│ ├── database.py

│ └── models.py

│

├── tests/

│ └── test_tasks.py

│

├── requirements.txt

├── README.md

└── .gitignore
```

---

## Como executar

Clone o projeto

```
git clone URL_DO_REPOSITORIO
```

Entre na pasta

```
cd TaskFlow-Agile-Project
```

Crie o ambiente virtual

```
python -m venv .venv
```

Ative

Windows

```
.venv\Scripts\activate
```

Instale as dependências

```
pip install -r requirements.txt
```

Execute

```
python src/app.py
```

Abra

```
http://127.0.0.1:5000
```

---

## Funcionalidades

✔ Cadastro de tarefas

✔ Conclusão de tarefas

✔ Exclusão de tarefas

✔ Persistência em SQLite

✔ Interface responsiva utilizando Bootstrap

---

## Autor

Victoria Beatriz Puglielli

UNIFECAF

Análise e Desenvolvimento de Sistemas