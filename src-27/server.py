import socket
import json
import sqlite3

def init_db():
    conn = sqlite3.connect('q27.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY, name TEXT, salary_ope INTEGER, salary_paillier TEXT)''')
    conn.commit()
    conn.close()

def run_server():
    init_db()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(('0.0.0.0', 5000))
    srv.listen(1)
    
    while True:
        conn, addr = srv.accept()
        data = conn.recv(8192).decode()
        if not data: continue
        
        req = json.loads(data)
        action = req.get('action')

        db = sqlite3.connect('q27.db')
        cursor = db.cursor()

        if action == 'add':
            cursor.execute(
                "INSERT INTO employees (id, name, salary_ope, salary_paillier) VALUES (?, ?, ?, ?)",
                (req['id'], req['name'], req['s_ope'], str(req['s_paillier']))
            )
            db.commit()
            conn.send(b"OK")

        elif action == 'list':
            cursor.execute("SELECT id, name FROM employees")
            conn.send(json.dumps(cursor.fetchall()).encode())

        elif action == 'compare':
            cursor.execute(
                "SELECT name FROM employees WHERE id IN (?, ?) ORDER BY salary_ope DESC", 
                (req['id1'], req['id2'])
            )
            res = cursor.fetchall()
            conn.send(json.dumps(res).encode())

        elif action == 'sum':
            cursor.execute("SELECT salary_paillier FROM employees")
            encrypted_salaries = [int(r[0]) for r in cursor.fetchall()]
            
            if not encrypted_salaries:
                conn.send(b"1")
            else:
                n_sq = int(req['n_sq'])
                result_encrypted = 1
                for s in encrypted_salaries:
                    result_encrypted = (result_encrypted * s) % n_sq
                conn.send(str(result_encrypted).encode())

        db.close()
        conn.close()

if __name__ == "__main__":
    run_server()