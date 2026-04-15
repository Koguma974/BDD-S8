import socket
import json
import mysql.connector
import os

def run_server():
    db = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user="root",
        password="ensibs",
        database="TP_SecuBDD"
    )
    cursor = db.cursor()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(('0.0.0.0', 5000))
    srv.listen(1)

    while True:
        conn, addr = srv.accept()
        data = conn.recv(8192).decode()
        if not data: continue
        
        req = json.loads(data)
        action = req.get('action')

        if action == 'add':
            cursor.execute(
                "INSERT INTO employees (id, name, salary_ope, salary_paillier) VALUES (%s, %s, %s, %s)",
                (req['id'], req['name'], req['s_ope'], req['s_paillier'])
            )
            db.commit()
            conn.send(b"OK")

        elif action == 'list':
            cursor.execute("SELECT id, name FROM employees")
            conn.send(json.dumps(cursor.fetchall()).encode())

        elif action == 'compare':
            cursor.execute(
                "SELECT name FROM employees WHERE id IN (%s, %s) ORDER BY salary_ope DESC", 
                (req['id1'], req['id2'])
            )
            res = cursor.fetchall()
            conn.send(json.dumps(res).encode())

        elif action == 'sum':
            cursor.execute("SELECT salary_paillier FROM employees")
            encrypted_salaries = [int(r[0]) for r in cursor.fetchall()]
            n_sq = int(req['n_sq'])
            result_encrypted = 1
            for s in encrypted_salaries:
                result_encrypted = (result_encrypted * s) % n_sq
            conn.send(str(result_encrypted).encode())

        conn.close()

if __name__ == "__main__":
    run_server()