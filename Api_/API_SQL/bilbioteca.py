import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = sqlite3.connect('biblioteca.db')

cursor = engine.cursor()

#cursor.execute("CREATE TABLE Aluno (id INTEGER PRIMARY KEY,nome TEXT NOT NULL,email TEXT NOT NULL UNIQUE)")

#cursor.execute("INSERT INTO Aluno VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com')")

#cursor.execute("INSERT INTO Aluno VALUES (2,'Helena O. S.', 'helena@exemplo.com')")

#cursor.execute("INSERT INTO Aluno  VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com')")

#engine.commit()

cursor.execute("CREATE TABLE Livro (id_livro INTEGER PRIMARY KEY,id_aluno INTEGER,descricao TEXT NOT NULL,FOREIGN KEY(id_aluno) REFERENCES Aluno(id)")

# cursor.execute("INSERT INTO Livro VALUES (1,1,'Python completo e total')")
        
# cursor.execute("INSERT INTO Livro VALUES (2,'Memorias póstumas de brás cubas')")

# cursor.execute( "INSERT INTO Livro VALUES (3,2,'Gravidade')")

# engine.commit()         
    


