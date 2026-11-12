import ingestion
import persistence
import processing

if __name__ == "__main__":
    print("Etape 1 : Ingestion")
    ingestion.download()

    print("Etape 2 : Persistance")
    persistence.build_database()

    print("Etape 3 : Traitement")
    processing.run_all()

    print("Pipeline termine. Lancer le dashboard avec : streamlit run src/dashboard.py")
