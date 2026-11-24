"""Rubrique éphémère, quota Groq, briefing, goûts, liens évidents, sécurité de la page."""
import json
from pathlib import Path

import agent
import briefing
import consommation
import gouts
import interprete


# ------------------------------------------------------------------ rubrique éphémère
def test_section_ephemere(tmp_path, monkeypatch):
    etat = tmp_path / "etat.json"
    sources = tmp_path / "sources.json"
    seul_en_france = next(n for n in agent.FLUX_FR
                          if not any(n in d for d in (agent.FLUX_US, agent.FLUX_CN, agent.FLUX_DEV)))
    etat.write_text(json.dumps({
        "section_ephemere": {"entite": "Jensen Huang", "depuis": "2026-11-24", "pic": 14,
                             "termes": ["Jensen Huang", "Huang Jensen PDG", "黄仁勋 (Jensen Huang)",
                                        "Jensen Huang Nvidia", "PDG de Nvidia"]},
        "pauses": {"fr": {seul_en_france: {"depuis": "2026-11-24", "motif": "test"}}}}), encoding="utf-8")
    sources.write_text(json.dumps({"ajoutees": {"dev": {"Média ajouté": "https://exemple.org/rss"}}}),
                       encoding="utf-8")
    monkeypatch.setattr(agent, "FICHIER_PILOTE", etat)
    monkeypatch.setattr(agent, "FICHIER_SOURCES", sources)
    r = agent.section_ephemere()
    assert r.requete_google.startswith('"Jensen Huang"')  # le nom principal d'abord
    assert seul_en_france not in r.flux_medias  # pause du pilote respectée
    assert "Média ajouté" in r.flux_medias  # ajout de sources.json repris
    assert r.mots_ia.search("Le PDG de Nvidia s'exprime")


def test_pas_de_section_ephemere(tmp_path, monkeypatch):
    etat = tmp_path / "etat.json"
    etat.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(agent, "FICHIER_PILOTE", etat)
    assert agent.section_ephemere() is None


# ------------------------------------------------------------------ quota Groq
def test_garde_fou_quota(monkeypatch):
    monkeypatch.setattr(consommation, "part_groq_du_jour", lambda: 90.0)
    monkeypatch.setattr(consommation, "_etape", lambda: "briefing")
    assert agent.economiser_groq()
    monkeypatch.setattr(consommation, "_etape", lambda: "agent")  # la veille garde Groq
    assert not agent.economiser_groq()
    monkeypatch.setattr(consommation, "_etape", lambda: "briefing")
    monkeypatch.setattr(consommation, "part_groq_du_jour", lambda: 40.0)
    assert not agent.economiser_groq()


def test_part_du_quota(tmp_path, monkeypatch):
    monkeypatch.setattr(consommation, "DOSSIER", tmp_path)
    assert consommation.part_groq_du_jour() == 0
    from datetime import datetime
    jour = datetime.now().strftime("%Y-%m-%d")
    (tmp_path / f"consommation-{jour}.json").write_text(json.dumps(
        {"fournisseurs": {"groq": {"entree": 150_000, "sortie": 20_000}}}), encoding="utf-8")
    assert consommation.part_groq_du_jour() == 85


# ------------------------------------------------------------------ briefing
def test_nettoyer_pour_la_voix():
    t = briefing.nettoyer("**Titre**\n- un point https://exemple.org/x\n# fin")
    assert "*" not in t and "http" not in t and "#" not in t and "-" not in t.split()[0]


def test_dimanche():
    assert briefing.est_dimanche("2026-11-29") and not briefing.est_dimanche("2026-11-24")


# ------------------------------------------------------------------ goûts
def test_gouts(tmp_path, monkeypatch):
    monkeypatch.setattr(gouts, "PROFIL", tmp_path / "profil.json")
    assert gouts.consigne_gouts() == ""  # sans profil, rien ne change
    (tmp_path / "profil.json").write_text(json.dumps(
        {"aime": ["agents de code"], "moins": ["valorisations boursières"]}), encoding="utf-8")
    c = gouts.consigne_gouts()
    assert "agents de code" in c and "valorisations boursières" in c and "un point au plus" in c


def test_exports_fusionnes(tmp_path, monkeypatch):
    monkeypatch.setattr(gouts, "DOSSIER", tmp_path)
    a = {"titre": "A", "lien": "https://a"}
    (tmp_path / "mes-gouts-2026-11-20.json").write_text(json.dumps({"aimes": [a]}), encoding="utf-8")
    (tmp_path / "mes-gouts-2026-11-24.json").write_text(json.dumps({"aimes": [a], "lus": [a]}), encoding="utf-8")
    e = gouts.lire_exports()
    assert len(e["aimes"]) == 1 and len(e["lus"]) == 1 and e["moins"] == []


# ------------------------------------------------------------------ interprète
def test_liens_evidents():
    assert interprete.lien_evident("Claude", "Claude Code")
    assert interprete.lien_evident("OpenAI", "ChatGPT")
    assert interprete.lien_evident("Claude", "Opus 5.5")
    assert interprete.lien_evident("Gemini 4 Neon", "Google DeepMind")
    assert interprete.lien_evident("Nvidia", "Anthropic", deja_relies=True)
    assert not interprete.lien_evident("Nvidia", "Anthropic")
    assert not interprete.lien_evident("Meta", "Metaculus")  # mot entier seulement


# ------------------------------------------------------------------ page publiée
def test_csp_autorise_le_briefing_audio():
    import publier
    page = (Path(__file__).parent.parent / "interface.html").read_text(encoding="utf-8")
    page = publier._avec_csp(page.replace("</head>", publier.TETE).replace("</body>", publier.PIED))
    assert "media-src 'self' blob:" in page and "default-src 'none'" in page


def test_manifeste_partage():
    m = json.loads((Path(__file__).parent.parent / "pwa" / "manifest.json").read_text(encoding="utf-8"))
    assert m["share_target"]["params"]["url"] == "partage_url"


# ------------------------------------------------------------------ relecture du briefing
SOURCES = ("Nvidia : le retour de Jensen Huang relance la machine boursière. Le retour surprise de "
           "Jensen Huang a déclenché un puissant rebond des valeurs technologiques.")


def test_phrases_causales():
    texte = "Bonjour. Le succès d'Anthropic a entraîné un rebond de Nvidia. Il fait beau."
    assert briefing.phrases_causales(texte) == ["Le succès d'Anthropic a entraîné un rebond de Nvidia."]


def test_lien_de_cause_verifie_par_le_code():
    vrai = briefing.Verdict(numero=1, cause="le retour de Jensen Huang", remplacement="x",
                            citation="Le retour surprise de Jensen Huang a déclenché un puissant rebond")
    invente = briefing.Verdict(numero=1, cause="le succès d'Anthropic", remplacement="x",
                               citation="Le retour surprise de Jensen Huang a déclenché un puissant rebond")
    fausse_citation = briefing.Verdict(numero=1, cause="le retour de Jensen Huang", remplacement="x",
                                       citation="Jensen Huang a provoqué une hausse de 40 % du Nasdaq")
    assert briefing.etaye(vrai, SOURCES)
    assert not briefing.etaye(invente, SOURCES)  # la citation ne parle pas d'Anthropic
    assert not briefing.etaye(fausse_citation, SOURCES)  # citation absente des sources
