"""Interface graphique (chat dans le navigateur) pour l'agent.

Lancement : uv run python gui.py   (la page s'ouvre toute seule ; Ctrl+C pour arrêter)
"""

import os

# Gradio envoie par défaut des statistiques d'usage : on les coupe avant de l'importer.
os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")

import gradio as gr
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

from agent import build_graph

load_dotenv()
GRAPH = build_graph()

MAX_RESULTAT_AFFICHE = 2_000  # caractères d'un résultat d'outil montrés dans l'encadré

EXEMPLES = [
    "Quel jour sommes-nous et combien font 17 % de 2 340 ?",
    "Quel temps fera-t-il demain à Lyon ?",
    "Quels sont les 3 derniers épisodes de Choses à savoir sciences ?",
    "Résume-moi le dernier épisode de Choses à savoir sciences",
    "Fais jouer le dernier épisode de Choses à savoir sciences",
]


def _texte(contenu) -> str:
    """Gradio peut stocker un message sous forme de texte ou de liste de blocs."""
    if isinstance(contenu, str):
        return contenu
    if isinstance(contenu, list):
        return "\n".join(
            bloc.get("text", "") if isinstance(bloc, dict) else str(bloc) for bloc in contenu
        )
    return str(contenu or "")


def _historique(history: list[dict]) -> list:
    """Reconstruit la conversation pour l'agent à partir de l'affichage Gradio.

    Les encadrés d'outils (messages avec un titre) sont ignorés : l'agent garde les
    questions et ses réponses, pas les résultats bruts des outils. Une transcription
    de podcast renvoyée à chaque tour dépasserait vite la limite de l'offre Groq.
    """
    messages = []
    for message in history:
        if (message.get("metadata") or {}).get("title"):
            continue
        texte = _texte(message.get("content"))
        if message.get("role") == "user":
            messages.append(HumanMessage(texte))
        elif message.get("role") == "assistant" and texte:
            messages.append(AIMessage(texte))
    return messages


def _contenu_outil(arguments: dict, resultat: str) -> str:
    if len(resultat) > MAX_RESULTAT_AFFICHE:
        resultat = f"{resultat[:MAX_RESULTAT_AFFICHE]}… [{len(resultat)} caractères au total]"
    return f"Arguments : `{arguments}`\n\nRésultat :\n```\n{resultat}\n```"


def repondre(message: str, history: list[dict]):
    """Fait tourner l'agent et affiche chaque étape au fur et à mesure."""
    affichage: list[gr.ChatMessage] = []
    encadres: dict[str, tuple[gr.ChatMessage, dict]] = {}  # id d'appel -> (encadré, arguments)
    entree = {"messages": [*_historique(history), HumanMessage(message)]}
    try:
        # stream_mode="updates" : on reçoit la sortie de chaque nœud du graphe dès qu'il finit.
        for etape in GRAPH.stream(entree, stream_mode="updates"):
            for sortie in etape.values():
                for msg in sortie["messages"]:
                    if isinstance(msg, AIMessage):
                        for appel in msg.tool_calls:
                            encadre = gr.ChatMessage(
                                content=f"Arguments : `{appel['args']}`\n\nEn cours…",
                                metadata={"title": f"🛠️ Outil : {appel['name']}", "status": "pending"},
                            )
                            encadres[appel["id"]] = (encadre, appel["args"])
                            affichage.append(encadre)
                        if not msg.tool_calls and msg.content:
                            affichage.append(gr.ChatMessage(content=msg.content))
                    elif isinstance(msg, ToolMessage) and msg.tool_call_id in encadres:
                        encadre, arguments = encadres[msg.tool_call_id]
                        encadre.content = _contenu_outil(arguments, str(msg.content))
                        encadre.metadata["status"] = "done"
                        if msg.status == "error":
                            encadre.metadata["title"] += " (erreur)"
            yield affichage
    except Exception as exc:  # erreur Groq, réseau… : on l'affiche au lieu de planter
        affichage.append(gr.ChatMessage(content=f"⚠️ Erreur : {type(exc).__name__} : {exc}"))
        yield affichage


demo = gr.ChatInterface(
    fn=repondre,
    title="Mon agent LangGraph",
    description=(
        "Calculatrice, date et heure, météo et podcasts (lister, faire jouer, transcrire). "
        "Les encadrés 🛠️ montrent les outils appelés : clique dessus pour voir le détail."
    ),
    examples=EXEMPLES,
    examples_label="Exemples",
    analytics_enabled=False,
)


if __name__ == "__main__":
    # 127.0.0.1 : accessible uniquement depuis cet ordinateur, pas depuis le réseau.
    demo.launch(server_name="127.0.0.1", inbrowser=True)
