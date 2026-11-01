"""Agent ReAct LangGraph : répond à une question à l'aide d'une calculatrice et de l'horloge."""

import argparse
import ast
import math
import operator
from datetime import datetime

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

MODEL = "openai/gpt-oss-120b"

SYSTEM_PROMPT = (
    "Tu es un assistant qui répond dans la langue de l'utilisateur. "
    "Utilise toujours l'outil calculatrice pour les calculs et l'outil "
    "date_heure_actuelles pour la date ou l'heure : ne les devine jamais."
)

MAX_EXPRESSION_LENGTH = 200
MAX_POWER_BITS = 10_000  # taille maximale d'un entier obtenu par puissance

BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}
UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}
FUNCTIONS = {
    "abs": abs,
    "round": round,
    "sqrt": math.sqrt,
    "log": math.log,
    "exp": math.exp,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
}
CONSTANTS = {"pi": math.pi, "e": math.e}

JOURS = ("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche")


def _safe_pow(base: int | float, exponent: int | float) -> int | float:
    # Les grands entiers sont bornés a priori : 9**9**9 ferait saturer la mémoire.
    if isinstance(base, int) and isinstance(exponent, int):
        if base.bit_length() * abs(exponent) > MAX_POWER_BITS:
            raise ValueError("Puissance trop grande.")
    result = base**exponent
    if isinstance(result, complex):
        raise ValueError("Le résultat n'est pas un nombre réel.")
    return result


def _evaluate(node: ast.AST) -> int | float:
    """Évalue un arbre syntaxique en n'acceptant qu'une liste blanche de nœuds."""
    match node:
        case ast.Constant(value=value) if type(value) in (int, float):
            return value
        case ast.Name(id=name) if name in CONSTANTS:
            return CONSTANTS[name]
        case ast.UnaryOp(op=op, operand=operand) if type(op) in UNARY_OPERATORS:
            return UNARY_OPERATORS[type(op)](_evaluate(operand))
        case ast.BinOp(left=left, op=ast.Pow(), right=right):
            return _safe_pow(_evaluate(left), _evaluate(right))
        case ast.BinOp(left=left, op=op, right=right) if type(op) in BINARY_OPERATORS:
            return BINARY_OPERATORS[type(op)](_evaluate(left), _evaluate(right))
        case ast.Call(func=ast.Name(id=name), args=args, keywords=[]) if name in FUNCTIONS:
            return FUNCTIONS[name](*(_evaluate(arg) for arg in args))
    raise ValueError(f"Élément non autorisé : {type(node).__name__}")


def evaluate_expression(expression: str) -> str:
    """Calcule une expression mathématique sans jamais exécuter de code."""
    if len(expression) > MAX_EXPRESSION_LENGTH:
        raise ValueError("Expression trop longue.")
    result = _evaluate(ast.parse(expression, mode="eval").body)
    # 12 chiffres significatifs : masque le bruit des flottants (0.1 + 0.2).
    return f"{result:.12g}" if isinstance(result, float) else str(result)


@tool
def calculatrice(expression: str) -> str:
    """Calcule une expression mathématique et renvoie le résultat.

    Syntaxe : + - * / // ** et parenthèses, avec le point comme séparateur décimal.
    Fonctions : abs, round, sqrt, log, exp, sin, cos, tan. Constantes : pi, e.
    Attention : % désigne le modulo. Pour un pourcentage, écrire 17 % de 2340
    sous la forme 0.17 * 2340.
    """
    return evaluate_expression(expression)


@tool
def date_heure_actuelles() -> str:
    """Renvoie la date, le jour de la semaine et l'heure actuels (fuseau local)."""
    now = datetime.now().astimezone()
    return f"{JOURS[now.weekday()]} {now.isoformat(timespec='seconds')}"


TOOLS = [calculatrice, date_heure_actuelles]


def build_graph():
    llm = ChatGroq(model=MODEL).bind_tools(TOOLS)

    def call_model(state: MessagesState) -> dict:
        messages = [SystemMessage(SYSTEM_PROMPT), *state["messages"]]
        return {"messages": [llm.invoke(messages)]}

    graph = StateGraph(MessagesState)
    graph.add_node("model", call_model)
    # handle_tool_errors : l'erreur est renvoyée au modèle, qui peut se corriger.
    graph.add_node("tools", ToolNode(TOOLS, handle_tool_errors=True))
    graph.add_edge(START, "model")
    graph.add_conditional_edges("model", tools_condition)
    graph.add_edge("tools", "model")
    return graph.compile()


def print_tool_trace(messages: list) -> None:
    """Affiche chaque appel d'outil avec ses arguments et son résultat."""
    results = {m.tool_call_id: m.content for m in messages if isinstance(m, ToolMessage)}
    calls = [c for m in messages if isinstance(m, AIMessage) for c in m.tool_calls]
    print(f"Outils appelés ({len(calls)}) :")
    for call in calls:
        print(f"  - {call['name']}({call['args']}) -> {results.get(call['id'])}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", help="Question à poser à l'agent")
    args = parser.parse_args()

    load_dotenv()
    result = build_graph().invoke({"messages": [("user", args.question)]})
    print_tool_trace(result["messages"])
    print(f"\nRéponse :\n{result['messages'][-1].content}")


if __name__ == "__main__":
    main()
