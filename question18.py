import mysql.connector

print("Collez le listing ci-dessous, puis appuyez sur Entrée + Ctrl+D :")
listing = []
try:
    while True:
        line = input()
        listing.append(line)
except EOFError:
    pass

def parse_value(v):
    v = v.strip()
    if v == r'\N':
        return None
    return v.strip("'")

data = []
for line in listing:
    if not line.strip():
        continue
    fields = line.split('\t')
    row = tuple(parse_value(f) for f in fields)
    data.append(row)

conn = mysql.connector.connect(
    host='localhost',                       # A adapter btw
    user='root',                            # A adapter btw
    password='ensibs',                      # A adapter btw
    database='TP_SecuBDD_Tayllamin_Justine'
)

cursor = conn.cursor()

query = """
    INSERT INTO animaux (nom, proprietaire, espece, genre, naissance, mort)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(query, data)
conn.commit()

print(f"{cursor.rowcount} lignes insérées avec succès.")

cursor.close()
conn.close()