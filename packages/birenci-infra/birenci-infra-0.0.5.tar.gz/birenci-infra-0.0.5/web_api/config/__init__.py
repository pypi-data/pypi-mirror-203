import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), verbose=True)
currentEnv = os.getenv("BR_CI_API_ENV")
if currentEnv == "prod":
    from .prod import Config

    print("环境： prod")
    Conf = Config

else:
    from .develop import Config

    print("环境： develop")
    Conf = Config
