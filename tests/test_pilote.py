"""Pilote automatique : diagnostic des médias et recherche ciblée (sans réseau ni IA)."""
import json

import pilote

BASE = {"nom": "X", "section": "dev", "jour": "2026-11-24", "nuits": 4, "pannes": 0, "pannes_de_suite": 0,
        "nuits_mesurees": 4, "lus": 40, "utiles": 0, "retenus": 0, "ecartes": 0,
        "nuits_detaillees": 4, "recents": 0, "dernier": "2026-11-10"}


def test_media_calme_pas_mis_en_pause():
    assert pilote._diagnostic(BASE) is None


def test_media_en_panne():
    assert "en panne" in pilote._diagnostic({**BASE, "pannes_de_suite": 3})


def test_flux_abandonne():
    assert "abandonné" in pilote._diagnostic({**BASE, "dernier": "2026-08-01"})


def test_flux_hors_sujet():
    assert "hors sujet" in pilote._diagnostic({**BASE, "recents": 12, "dernier": "2026-11-24"})


def test_anciennes_veilles_ne_suffisent_pas():
    # Sans le détail des articles récents (veilles d'avant le 24/11), aucun verdict « muet ».
    assert pilote._diagnostic({**BASE, "nuits_detaillees": 0, "recents": 0, "dernier": ""}) is None


def _veille(dossier, code, jour, n, google):
    (dossier / f"veille-ia-{code}-{jour}.json").write_text(
        json.dumps({"nombre_articles": n, "liens_google": google}), encoding="utf-8")


def test_sections_faibles(tmp_path, monkeypatch):
    monkeypatch.setattr(pilote, "VEILLES", tmp_path)
    for j in ("2026-11-22", "2026-11-23", "2026-11-24"):
        _veille(tmp_path, "cn", j, 50, 44)  # 12 % de liens directs
        _veille(tmp_path, "fr", j, 50, 15)  # 70 %
    etat = {"decouvertes_ciblees": {}}
    faibles = pilote._sections_faibles("2026-11-24", etat)
    assert [code for code, _ in faibles] == ["cn"]
    # Une recherche ciblée récente : on attend avant d'en relancer une.
    etat["decouvertes_ciblees"]["cn"] = "2026-11-22"
    assert pilote._sections_faibles("2026-11-24", etat) == []


def test_une_seule_nuit_faible_ne_suffit_pas(tmp_path, monkeypatch):
    monkeypatch.setattr(pilote, "VEILLES", tmp_path)
    _veille(tmp_path, "cn", "2026-11-22", 50, 10)
    _veille(tmp_path, "cn", "2026-11-23", 50, 10)
    _veille(tmp_path, "cn", "2026-11-24", 50, 45)
    assert pilote._sections_faibles("2026-11-24", {"decouvertes_ciblees": {}}) == []


def test_raison_imposee_selon_le_type():
    assert "essai" in pilote.RAISON_IMPOSEE["adopter"]
    assert "fermeture" in pilote.RAISON_IMPOSEE["fermer_section"]
