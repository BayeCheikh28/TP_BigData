# Projet Big Data - Analyse de l'historique NBA

## Sujet choisi

Ce projet exploite l'historique complet des matchs de la NBA depuis 1946
(source : FiveThirtyEight, dataset `nbaallelo.csv`, plus de 126 000 lignes).
Chaque ligne represente la participation d'une equipe a un match, avec son
score, celui de l'adversaire, son classement Elo avant/apres le match, le
lieu de la rencontre et le resultat.

L'objectif est de mettre en place une chaine complete : ingestion des
donnees brutes, persistance dans une base de donnees, traitement par
agregations SQL/pandas, puis restitution via un tableau de bord interactif.

## Architecture Big Data

```
          +----------------+
          |  Source CSV     |
          |  (GitHub raw)   |
          +--------+-------+
                   |
                   v  ingestion.py (requests)
          +----------------+
          | data/raw/*.csv |
          +--------+-------+
                   |
                   v  persistence.py (pandas + sqlite3)
          +----------------+
          |   db/nba.db     |
          |  table games    |
          |  table teams    |
          +--------+-------+
                   |
                   v  processing.py (requetes SQL + pandas)
          +----------------------+
          | data/processed/*.csv |
          +----------+-----------+
                      |
                      v  dashboard.py (Streamlit + Plotly)
          +----------------------+
          |  Tableau de bord web  |
          +----------------------+
```

- **Ingestion** : `src/ingestion.py` telecharge le fichier CSV source depuis
  GitHub et le place dans `data/raw/`.
- **Persistance** : `src/persistence.py` charge le CSV avec pandas, nettoie
  les types (dates) et ecrit deux tables dans une base SQLite (`games` et
  `teams`).
- **Traitement** : `src/processing.py` execute des requetes SQL sur la base
  pour produire des agregations (victoires par equipe, score moyen par
  saison, nombre de matchs par saison, taux de victoire domicile/exterieur,
  classement Elo moyen) et les enregistre dans `data/processed/`.
- **Visualisation** : `src/dashboard.py` affiche ces agregations sous forme
  de graphes interactifs avec Streamlit et Plotly.

## Diagramme d'activites

```
[Debut]
   |
   v
Telecharger le CSV source
   |
   v
Nettoyer et typer les donnees (dates)
   |
   v
Charger les donnees dans SQLite
   |
   v
Executer les requetes d'agregation
   |
   v
Exporter les resultats en CSV
   |
   v
Afficher le dashboard interactif
   |
   v
[Fin]
```

## Technologies utilisees

| Etape | Technologie | Justification |
|---|---|---|
| Ingestion | Python + requests | Simplicite, pas besoin d'outil distribue pour un volume de quelques dizaines de Mo |
| Persistance | SQLite | Base embarquee, sans serveur a installer, suffisante pour ~126 000 lignes |
| Traitement | pandas + SQL | Agregations rapides et lisibles, pas besoin de Spark pour ce volume |
| Visualisation | Streamlit + Plotly | Mise en place rapide d'un dashboard interactif en Python pur |

## Resultats obtenus

Le dashboard presente :
- le classement des 15 franchises les plus victorieuses de l'histoire,
- le classement des 15 franchises avec le meilleur score Elo moyen,
- l'evolution du score moyen marque par saison,
- le nombre de matchs joues par saison,
- la repartition victoires/defaites selon le lieu du match (domicile ou exterieur).

## Limites et perspectives

- Le dataset s'arrete en 2015, les saisons recentes ne sont pas couvertes.
- Les donnees sont agregees au niveau match, sans detail joueur par joueur.
- Une evolution possible serait de brancher un dataset plus recent (NBA API)
  et d'ajouter des indicateurs par joueur.

## Installation et execution

```bash
pip install -r requirements.txt

python src/main.py

streamlit run src/dashboard.py
```

## Structure du projet

```
TP_BigData/
  data/
    raw/        donnees brutes telechargees
    processed/  resultats des agregations
  db/           base de donnees SQLite
  src/
    ingestion.py
    persistence.py
    processing.py
    dashboard.py
    main.py
  requirements.txt
  README.md
```
