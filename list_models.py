"""Liste les modèles disponibles sur l'API Groq."""

from dotenv import load_dotenv
from groq import Groq


def main() -> None:
    load_dotenv()
    client = Groq()  # lit GROQ_API_KEY dans l'environnement

    models = sorted(client.models.list().data, key=lambda m: m.id)
    for model in models:
        print(f"{model.id:<50} {model.owned_by}")
    print(f"\n{len(models)} modèles disponibles")


if __name__ == "__main__":
    main()
