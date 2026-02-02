import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS "cards" (
    "card_id"    INTEGER PRIMARY KEY AUTOINCREMENT,
"question"   TEXT,
"answer"     TEXT,
"note"       TEXT,
"weight"     REAL,
"deck_id"    INTEGER,
FOREIGN KEY ("deck_id") REFERENCES "decks"("deck_id")
)"""

cursor.execute(command1)


command2 = """CREATE TABLE IF NOT EXISTS "decks" (
    "deck_id"       INTEGER,
    "name"          TEXT,
    "description"   TEXT,
    "cards_number"  INTEGER,
    PRIMARY KEY("deck_id" AUTOINCREMENT)
)"""

cursor.execute(command2)