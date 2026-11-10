// Service worker de l'app Veille IA (version en ligne).
// Stratégie « réseau d'abord » : on charge toujours la version la plus récente, et on en
// garde une copie ; sans connexion, on affiche la dernière copie (la dernière veille consultée).

const CACHE = "veille-ia-v2"; // changer le numéro à chaque refonte : vide l'ancien cache sur les téléphones
const COQUILLE = ["./", "./index.html", "./manifest.json", "./icones/icone-192.png", "./icones/icone-512.png"];

self.addEventListener("install", (evenement) => {
  evenement.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(COQUILLE)));
  self.skipWaiting();
});

self.addEventListener("activate", (evenement) => {
  // Supprime les caches des anciennes versions.
  evenement.waitUntil(
    caches.keys().then((cles) => Promise.all(cles.filter((c) => c !== CACHE).map((c) => caches.delete(c))))
  );
  self.clients.claim();
});

self.addEventListener("fetch", (evenement) => {
  const requete = evenement.request;
  // Seulement nos propres fichiers : les miniatures YouTube et pochettes Apple passent tout droit.
  if (requete.method !== "GET" || new URL(requete.url).origin !== self.location.origin) return;
  evenement.respondWith(
    fetch(requete)
      .then((reponse) => {
        if (reponse.ok) {
          const copie = reponse.clone();
          caches.open(CACHE).then((cache) => cache.put(requete, copie));
        }
        return reponse;
      })
      .catch(() => caches.match(requete).then((enCache) => enCache || caches.match("./index.html")))
  );
});
