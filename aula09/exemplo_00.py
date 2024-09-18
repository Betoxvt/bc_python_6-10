from functools import wraps
from sys import stderr

from loguru import logger


def hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Isso e um decorador")
        return result

    return wrapper


# Se quiser salvar o log em um arquivo
logger.add("meu_app.log")  # Salva todos

# Salva só criticos, personalizada e cria um novo sempre que atingir 5MB
logger.add(
    "critical_logs.log",
    format="{time} {level} {message} {file}",
    level="CRITICAL",
    rotation="5 MB",
)

# stderr para exibir os logs
logger.add(
    sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO"
)


@hello
def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Soma ocorreu bem, {x} + {y} = {soma}")
        return soma
    except Exception as e:
        logger.critical(f"Você tem que digitar valores corretos: {e}")


soma(2, 3)
soma(4, 2)
soma(2, "3")
