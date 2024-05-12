import sqlite3

def calculate_interest(balance):
    # Calcula els interessos com un 1% del saldo actual
    return round(balance * 0.01, 2)

# Connexió amb la base de dades
conn = sqlite3.connect("bigger.db")
cursor = conn.cursor()

# Obtenim el saldo total dels comptes de tipus 'C' abans de la liquidació
cursor.execute("SELECT SUM(balance) FROM comptes WHERE type = 'C'")
total_before = cursor.fetchone()[0]

# Obtenim el saldo del compte del banc
cursor.execute("SELECT balance FROM comptes WHERE type = 'S' ORDER BY acc_id ASC LIMIT 1")
bank_balance_before = cursor.fetchone()[0]

# Calculem els interessos per a cada compte de tipus 'C' i transferim-los
cursor.execute("SELECT acc_id, balance FROM comptes WHERE type = 'C'")
for row in cursor.fetchall():
    acc_id, balance = row
    interest = calculate_interest(balance)
    cursor.execute("UPDATE comptes SET balance = balance + ? WHERE type = 'S'", (interest,))
    cursor.execute("UPDATE comptes SET balance = balance - ? WHERE acc_id = ?", (interest, acc_id))

# Obtenim el saldo total dels comptes de tipus 'C' després de la liquidació
cursor.execute("SELECT SUM(balance) FROM comptes WHERE type = 'C'")
total_after = cursor.fetchone()[0]

# Obtenim el saldo del compte del banc després de la transferència d'interessos
cursor.execute("SELECT balance FROM comptes WHERE type = 'S' ORDER BY acc_id ASC LIMIT 1")
bank_balance_after = cursor.fetchone()[0]

# Verifiquem que la suma dels saldos sigui la mateixa abans i després de la liquidació
assert round(total_before, 2) == round(total_after, 2), "La suma dels saldos dels comptes 'C' ha canviat després de la liquidació"
assert round(bank_balance_before, 2) == round(bank_balance_after, 2), "El saldo del compte del banc ha canviat després de la liquidació"

conn.commit()

fer = input("Vols fer la transferencia? (SI/NO): ")

if fer.upper() == "SI":
    # Confirmem els canvis a la base de dades
    conn.commit()
    print("Liquidació d'interessos completada amb èxit.")
else:
    conn.rollback()
    print("Transferència cancel·lada.")

# Tanquem la connexió
conn.close()