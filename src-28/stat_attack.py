import random
import statistics
import sqlite3
import matplotlib.pyplot as plt
from pyope.ope import OPE

def setup_database(mu, sigma, n, db_name="entreprise.db"):
    vrais_salaires = [max(1200, int(random.gauss(mu, sigma))) for _ in range(n)]
    chiffreur = OPE(b"clef_secrete")
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS employes")
    cursor.execute("CREATE TABLE employes (id INTEGER PRIMARY KEY, salaire_ope TEXT)")
    for s in vrais_salaires:
        cursor.execute("INSERT INTO employes (salaire_ope) VALUES (?)", (str(chiffreur.encrypt(s)),))
    conn.commit()
    conn.close()
    return vrais_salaires

def executer_attaque(mu, sigma, n, db_name="entreprise.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT salaire_ope FROM employes")
    salaires_chiffres = [int(row[0]) for row in cursor.fetchall()]
    conn.close()
    chiffres_tries = sorted(salaires_chiffres)
    dist_publique = sorted([max(1200, int(random.gauss(mu, sigma))) for _ in range(n)])
    mapping_attaque = {chiffres_tries[i]: dist_publique[i] for i in range(n)}
    return salaires_chiffres, mapping_attaque

def main():
    mu, sigma, n, db_name = 2500, 400, 1000, "entreprise.db"
    vrais_salaires = setup_database(mu, sigma, n, db_name)
    salaires_chiffres, mapping_attaque = executer_attaque(mu, sigma, n, db_name)
    erreurs = [abs(vrai - mapping_attaque[chiffre]) for vrai, chiffre in zip(vrais_salaires, salaires_chiffres)]
    print(f"Marge d'erreur moyenne : {statistics.mean(erreurs):.2f} euros")
    paires_triees = sorted([(vrai, mapping_attaque[chiffre]) for vrai, chiffre in zip(vrais_salaires, salaires_chiffres)])
    vrais_tries, predits_tries = [p[0] for p in paires_triees], [p[1] for p in paires_triees]
    plt.figure(figsize=(10, 6))
    plt.plot(range(n), vrais_tries, label="Vrais Salaires", color="blue", linewidth=2)
    plt.plot(range(n), predits_tries, label="Salaires Prédits", color="red", linestyle="dashed", linewidth=2)
    plt.fill_between(range(n), vrais_tries, predits_tries, color='red', alpha=0.1, label="Zone d'erreur")
    plt.title(f"Attaque OPE sur SQLite (n={n})")
    plt.xlabel("Index des employés")
    plt.ylabel("Salaire en euros")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == '__main__':
    main()
