# Aula 06
## Revisão
Ambiente:

    gh repo create --public <meu-novo-repositorio>
    echo '.env' >> .gitignore && echo '.venv' >> .gitignore && echo '# Nome do projeto' >> README.md
    git init
    git remote add origin git@github.com:seu_usuario/meu-novo-repositorio.git
    pyenv local 3.12.5
    poetry init
    poetry env use 3.12.5
    poetry shell
    poetry add <...>
    git add .
    git commit -m "build(env): first commit"
    git push -u origin main
    poetry run <...>
Boas práticas: [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
Classe usa a primeira letra maiúscula (DataFrame do pandas) enquanto função ou metodo usaria data_frame
* criar o .env pras senhas tudo que for secret
- black isort flake8
* flake8 verifica o arquivo, mas tem que arrumar na mão `poetry run flake8 main.py`
* black arruma tudo sozinho `poetry run black main.py`
Entre os dois há diferenças. Número de caracteres na linha, o black permite 88 enquanto o flake 79. Para configurar a compatibilidade cria-se um arquivo `.flake8` na primeira linha `[flake8]` e em baixo outra linha `max-line-lenght = 89`
* blue utiliza o black e o flake8 também e permite 89 caracteres
* outras linhas para adicionar (claro depende do que a equipe devidir) `extend-ignore = E203,E701`
exemplo:

        [flake8]
        max-line-length = 89
        extend-ignore = E203,E701,W291
        exclude = .venv

Quando rodar vários juntos, eles acabam se bagunçando e para ajeitar vai no 'pyproject.toml' e insere:

    [tool.isort]
    profile = "black"

aí pode rodar os reformatadores de boa. No pyproject.toml adicione:

     [tool.taskipy.tasks]
     format = """
     isort main.py
     black main.py
     flake8 main.py
     """

manda um `poetry run task format` (precisa adicionar o taskipy)

O commitizen inicia com `cz init` ai vem as configurações vc pode adicionar uma tag ao git com `git tag 0.1.0` ai faz o commit com o formato `git commit -m "docs(readme): added new instructions"`
configurações do commitizen também podem ser inseridas no pyproject.toml, exemplo:

    [tool.commitizen]
    name = "cz_conventional_commits"
    version = "0.1.0"
    version_files = [
        "src/__version__.py",
        "pyproject.toml:version"
    ]
    update_changelog_on_bump = true
    style = [
        ["qmark", "fg:#ff9d00 bold"],
        ["question", "bold"],
        ["answer", "fg:#ff9d00 bold"],
        ["pointer", "fg:#ff9d00 bold"],
        ["highlighted", "fg:#ff9d00 bold"],
        ["selected", "fg:#cc5454"],
        ["separator", "fg:#cc5454"],
        ["instruction", ""],
        ["text", ""],
        ["disabled", "fg:#858585 italic"]
    ]

`isinstance(objeto, classinfo)` verifica o tipo e retorna booleano. bom para validar com if e else algumas coisas
## Pré-Commit
Também é uma biblioteca (poetry add pre-commit) que serve, também, para verificar as paradas da PEP8 antes de qualquer add e commit.
Ele segue uma estrutura de dicionário `chave: valor` e assim você pode falar para ele todos os pre-commits que deseja, no arquivo `.pre-commit-config-yaml`, como segurança (bandit), arquivos grandes, padrão de commit (commitizen), formatação... um monte de coisas.
* depois de configurado manda um `poetry run pre-commit install` que vai adicionar ao .git
* adicionar o bandit e o commitizen é uma boa, veja a documentation
* `pre-commit autoupdate`

# Aula 07: Funções em Python e Estrutura de dados (parte 1)
* Permite reutilizar um código (função) em vários scripts.
Digamos que vários scripts usam uma função, se necessário uma alteração na função (por exemplo um destino LOAD) basta alterar uma vez só e não 6000.
* Lista de exercícios
* Projeto: ler um csv, processar dados, calcular vendas e exibir resultados

# Aula 08: Funções em Python - ETL com Pandas, JSON e Parquet
Criar o múdlo de ETL que lê 3 arquivos JSON e concatena em um único Data Frame usando Pandas (+ os e glob), cria um novo DF com outra coluna e então exporta para CSV ou Parquet;
Criar o módulo Pipeline que chama as funções da ETL e usa pathlib para manejar as pastas.

# Aula 09: Funções em Python - Decoradores
* LOG: Como se fosse um debug, mas não precisa estar ali fazendo. Registra as informações e erros, da avisos...
    Usando a biblioteca loguru (open source)
    Há o sentry_sdk que é ótimo, só cobra dependendo da quantidade de serviços (sentry.io)

* Decoradores: Funciona tanto para função quanto classe. Como uma função que recebe outra função, que recebe todos os parâmetros que o usuário colocar. Por isso normalmente é chamada de wrapper pois você envolve a função com essas funções adicionais. Ai põe ali no log de erro os try e except fica tudo já embalado pra usar nas funções. E você chama usando @tal_decorator.

* tenacity decorator: biblioteca externa.
tem o decorator retry, da uma quantidade de tentativas antes de abortar
