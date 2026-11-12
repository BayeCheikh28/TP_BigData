import os
import sqlite3
import pandas as pd

RAW_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "nbaallelo.csv")
DB_FILE = os.path.join(os.path.dirname(__file__), "..", "db", "nba.db")


def load_raw():
    df = pd.read_csv(RAW_FILE)
    df["date_game"] = pd.to_datetime(df["date_game"])
    return df


def build_database():
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    df = load_raw()

    conn = sqlite3.connect(DB_FILE)
    df.to_sql("games", conn, if_exists="replace", index=False)

    teams = df[["team_id", "fran_id"]].drop_duplicates().rename(
        columns={"team_id": "team_id", "fran_id": "team_name"}
    )
    teams.to_sql("teams", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print(f"Base de donnees creee : {DB_FILE}")
    print(f"Table games : {len(df)} lignes")
    print(f"Table teams : {len(teams)} lignes")


if __name__ == "__main__":
    build_database()
