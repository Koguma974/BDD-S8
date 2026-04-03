import socket
import json
import os
import pickle
from phe import paillier
from pyope.ope import OPE

KEY_FILE = "secret.key"

if not os.path.exists(KEY_FILE):
    pub, priv = paillier.generate_paillier_keypair()
    ope = OPE(os.urandom(16))
    with open(KEY_FILE, 'wb') as f:
        pickle.dump((pub, priv, ope), f)
else:
    with open(KEY_FILE, 'rb') as f:
        pub, priv, ope = pickle.load(f)

def talk(data):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('127.0.0.1', 5000))
    c.send(json.dumps(data).encode())
    res = c.recv(8192).decode()
    c.close()
    return res

def main():
    while True:
        print("1. Ajouter employé\n2. Lister employés\n3. Comparer deux salaires\n4. Somme totale\n5. Quitter")
        choice = input("> ")

        if choice == '1':
            idx = int(input("ID: "))
            nom = input("Nom: ")
            sal = int(input("Salaire: "))
            talk({
                'action': 'add', 'id': idx, 'name': nom,
                's_ope': ope.encrypt(sal),
                's_paillier': str(pub.encrypt(sal).ciphertext())
            })

        elif choice == '2':
            print("Liste des employés:")
            for r in json.loads(talk({'action': 'list'})):
                print(f"[{r[0]}] {r[1]}")

        elif choice == '3':
            id1, id2 = input("ID 1: "), input("ID 2: ")
            res = json.loads(talk({'action': 'compare', 'id1': id1, 'id2': id2}))
            if res:
                print(f"L'employé le mieux payé est : {res[0][0]}")

        elif choice == '4':
            enc_sum = talk({'action': 'sum', 'n_sq': pub.nsquare})
            total = priv.decrypt(paillier.EncryptedNumber(pub, int(enc_sum)))
            print(f"Somme des salaire: {total}")

        elif choice == '5': break

if __name__ == "__main__":
    main()