import env

from .core import Texts

LOCALE = env.get("LOCALE")
LOCALES_PATH = env.get("LOCALES_PATH", "locales")

texts = Texts(f"{LOCALES_PATH}/{LOCALE}.yml")
