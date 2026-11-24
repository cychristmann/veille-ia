"""Paris du pilote : comptage, estimation historique, choix de la méthode (sans IA)."""
import json
import re

import pytest

import paris


@pytest.fixture
def veilles(tmp_path, monkeypatch):
    """Nvidia cité 10 fois par jour du 10 au 24/11 (sauf le 20 : pas de veille)."""
    monkeypatch.setattr(paris, "VEILLES", tmp_path)
    monkeypatch.setattr(paris, "_ENTITES", {"Nvidia": re.compile(r"(?<!\w)Nvidia(?!\w)", re.I)})
    paris.oublier_textes()
    for j in range(10, 25):
        if j == 20:
            continue
        articles = [{"titre": f"Nvidia annonce {i}"} for i in range(10)] + [{"titre": "Autre chose"}]
        (tmp_path / f"veille-ia-us-2026-11-{j}.json").write_text(
            json.dumps({"themes": [{"articles": articles}]}), encoding="utf-8")
    yield tmp_path
    paris.oublier_textes()


def test_compter(veilles):
    assert paris.compter("Nvidia", ["us"], ["2026-11-23", "2026-11-24"]) == (20, 2)
    assert paris.compter("Nvidia", ["us"], ["2026-11-20"]) == (0, 0)  # jour sans veille


def test_entite_disparue_ne_plante_pas(veilles):
    assert paris.compter("Inconnue", ["us"], ["2026-11-24"]) == (0, 1)
    assert paris.compter("Inconnue", ["us"], ["2026-11-24"], termes=["Nvidia"]) == (10, 1)


def test_estimation_historique(veilles):
    gagnant = {"entite": "Nvidia", "sections": ["us"], "comparaison": "au_moins", "seuil": 15, "horizon": 2}
    perdant = {**gagnant, "seuil": 40}
    p, g, n = paris.estimation_historique(gagnant, "2026-11-24")
    assert n > 3 and g == n and p > 0.8
    p, g, n = paris.estimation_historique(perdant, "2026-11-24")
    assert g == 0 and p < paris.SEUIL_REFUS


def test_pas_de_regard_vers_le_futur(veilles):
    p = {"entite": "Nvidia", "sections": ["us"], "comparaison": "au_moins", "seuil": 5, "horizon": 1}
    _, _, n = paris.estimation_historique(p, "2026-11-12")
    assert n == 3  # 10, 11 et 12/11 seulement


def test_enonce_ecrit_par_le_code():
    p = paris.Pari(entite="Nvidia", sections=["us"], comparaison="au_plus", seuil=12, horizon=3,
                   probabilite=0.7, enonce="Nvidia dépassera 12", raisonnement="")
    assert paris._enonce(p) == "Nvidia : au plus 12 articles (États-Unis) sur les 3 prochains jours"
    assert paris._incoherent(p)  # la phrase de l'IA dit l'inverse des chiffres


def _pari(proba_ia, stat, gagne):
    return {"statut": "gagne" if gagne else "perdu", "probabilite_ia": proba_ia, "probabilite": proba_ia,
            "probabilite_stat": stat, "comparaison": "au_moins"}


def test_choix_de_la_methode():
    # L'IA annonce toujours 80 %, l'historique voit juste : l'historique doit l'emporter.
    d = {"paris": [_pari(0.8, 0.9, True) for _ in range(5)] + [_pari(0.8, 0.1, False) for _ in range(5)]}
    methode, briers = paris.choisir_methode(d)
    assert methode == "historique" and briers["historique"] < briers["ia"]


def test_trop_peu_de_paris_pour_choisir():
    assert paris.choisir_methode({"paris": [_pari(0.8, 0.5, True)]}) == ("melange", {})


def test_correction_de_confiance_bornee():
    d = {"paris": [_pari(0.9, 0.5, i % 2 == 0) for i in range(12)]}
    assert paris.K_MIN <= paris.facteur_confiance(d) < 1
