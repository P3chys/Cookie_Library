-- SQLite
CREATE TABLE Kniha(
isbn TEXT PRIMARY KEY NOT NULL, 
nazev TEXT NOT NULL, 
autor TEXT NOT NULL, 
rok INTEGER NOT NULL, 
pocet INTEGER NOT NULL
);

CREATE TABLE Zakaznik(
rc INTEGER UNIQUE PRIMARY KEY NOT NULL, 
jmeno TEXT NOT NULL, 
prijmeni TEXT NOT NULL
);

CREATE TABLE Vypujcka(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
isbn TEXT NOT NULL, 
rc INTEGER NOT NULL,
datum_vypujceni TEXT NOT NULL,
FOREIGN KEY(isbn) REFERENCES Kniha(isbn), 
FOREIGN KEY (rc) REFERENCES Zakaznik(rc),
UNIQUE (isbn,rc)
);

CREATE TABLE Vypujcka_old(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
isbn TEXT NOT NULL, 
rc INTEGER NOT NULL,
datum_vypujceni TEXT NOT NULL,
FOREIGN KEY(isbn) REFERENCES Kniha(isbn), 
FOREIGN KEY (rc) REFERENCES Zakaznik(rc)
);

DELETE FROM Kniha;
DELETE FROM Zakaznik;
DELETE FROM Vypujcka;