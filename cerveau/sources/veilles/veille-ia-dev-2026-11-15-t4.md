# Veille Outils & code 2026-11-15 : Infrastructure et déploiement IA

Région : Outils & code · Date : 2026-11-15

Plusieurs titres décrivent des solutions d’infrastructure cloud (AWS Bedrock, SageMaker Canvas, DocumentDB, Amazon Emulator) et des patterns d’architecture pour accélérer le démarrage des sessions IA et gérer les modèles à grande échelle.

- **AWS Emulator proves agents need a verification loop. Realism is the hard part.** (The New Stack, note 8/10)
  This week, Amazon Web Services released AWS Emulator, a local copy of AWS that coding agents can test against. It The post AWS Emulator proves agents need a verification loop. Realism is the hard part. appeared first on The New Stack .
- **Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1** (AWS Machine Learning, note 6/10)
  GS Caltex connects Amazon SageMaker Canvas to Amazon SageMaker Pipelines so process engineers' no-code models run in production. This post shows how ML engineers reuse validated preprocessing flows and models, cutting deployment from about a week to a few hours and running batch inference every 30 m
- **datasette-cluster-map 0.19** (Simon Willison, note 5/10)
  Release: datasette-cluster-map 0.19 One of the oldest Datasette plugins, and still one of my favorites. It now works with Datasette 1.0a42, and depends on the new datasette-leaflet to ensure OpenStreetMap tiles are requested with a referrer header. Here's a map of power plants owned by California's
- **datasette-leaflet 0.3** (Simon Willison, note 5/10)
  Release: datasette-leaflet 0.3 OpenStreetMap have a very reasonable policy that hits to their hosted tile server should send a referrer header . Datasette table pages used the Referrer-Policy: no-referrer HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy. datas
