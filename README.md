# Aula 06
## Revisão
- Ambiente: `pyenv local 3.12.5` `poetry init` `poetry env use 3.12.5` `poetry shell` `poetry add ...` `touch .gitignore && echo '.venv' >> .gitignore` `poetry run ...`
Boas práticas: [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
Classe usa a primeira letra maiúscula (DataFrame do pandas) enquanto função ou metodo usaria data_frame
- black isort flake8
* flake8 verifica o arquivo, mas tem que arrumar na mão `poetry run flake8 main.py`
* black arruma tudo sozinho `poetry run black main.py`
Entre os dois há diferenças. Número de caracteres na linha, o black permite 88 enquanto o flake 79. Para configurar a compatibilidade cria-se um arquivo `.flake8` na primeira linha `[flake8]` e em baixo outra linha `max-line-lenght = 89`
* blue utiliza o black e o flake8 também e permite 89 caracteres
* outras linhas para adicionar (claro depende do que a equipe devidir)
    - `extend-ignore = E203,E701`
Quando rodar vários juntos, eles acabam se bagunçando e para ajeitar vai no 'pyproject.toml' e insere
    - [tool.isort]
    - profile = "black"
aí pode rodar os reformatadores de boa. No pyproject.toml adicione:
    - [tool.taskipy.tasks]
    - format = """
    - isort main.py
    - black main.py
    - flake8 main.py
    - """
manda um `poetry run task format` (precisa adicionar o taskipy)
## Pré-Commit
Também é uma biblioteca (poetry add pre-commit) que serve, também, para verificar as paradas da PEP8 antes de qualquer add e commit.
Ele segue uma estrutura de dicionário `chave: valor` e assim você pode falar para ele todos os pre-commits que deseja, no arquivo `.pre-commit-config-yaml`, como segurança (bandit), arquivos grandes, padrão de commit (commitizen), formatação... um monte de coisas.
* depois de configurado manda um `poetry run pre-commit install` que vai adicionar ao .git
