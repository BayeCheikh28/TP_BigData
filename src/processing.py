import os
import sqlite3
import pandas as pd

DB_FILE = os.path.join(os.path.dirname(__file__), "..", "db", "nba.db")
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")


def get_connection():
    return sqlite3.connect(DB_FILE)


def victoires_par_equipe():
    conn = get_connection()
    query = """
        SELECT fran_id AS equipe, COUNT(*) AS victoires
        FROM games
        WHERE game_result = 'W'
        GROUP BY fran_id
        ORDER BY victoires DESC
        LIMIT 15
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def score_moyen_par_saison():
    conn = get_connection()
    query = """
        SELECT year_id AS saison, AVG(pts) AS score_moyen
        FROM games
        GROUP BY year_id
        ORDER BY saison
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def matchs_par_saison():
    conn = get_connection()
    query = """
        SELECT year_id AS saison, COUNT(*) AS nb_matchs
        FROM games
        GROUP BY year_id
        ORDER BY saison
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def taux_victoire_domicile_exterieur():
    conn = get_connection()
    query = """
        SELECT game_location AS lieu, game_result AS resultat, COUNT(*) AS nb
        FROM games
        WHERE game_location IN ('H', 'A')
        GROUP BY game_location, game_result
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def elo_moyen_par_equipe():
    conn = get_connection()
    query = """
        SELECT fran_id AS equipe, AVG(elo_n) AS elo_moyen
        FROM games
        GROUP BY fran_id
        ORDER BY elo_moyen DESC
        LIMIT 15
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def run_all():
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    victoires_par_equipe().to_csv(os.path.join(PROCESSED_DIR, "victoires_par_equipe.csv"), index=False)
    score_moyen_par_saison().to_csv(os.path.join(PROCESSED_DIR, "score_moyen_par_saison.csv"), index=False)
    matchs_par_saison().to_csv(os.path.join(PROCESSED_DIR, "matchs_par_saison.csv"), index=False)
    taux_victoire_domicile_exterieur().to_csv(os.path.join(PROCESSED_DIR, "domicile_exterieur.csv"), index=False)
    elo_moyen_par_equipe().to_csv(os.path.join(PROCESSED_DIR, "elo_moyen_par_equipe.csv"), index=False)

    print("Agregations terminees, fichiers enregistres dans data/processed")


if __name__ == "__main__":
    run_all()
