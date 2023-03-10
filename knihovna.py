from db_init import connect

conn = connect()

class Kniha():
    def __init__(self,isbn,nazev,autor,rok,pocet):
        self.nazev = nazev
        self.autor = autor
        self.rok = rok
        self.pocet = pocet
        self.isbn = isbn
        Kniha.pridejKnihu(self)

    def kontrolaExistence(isbn):
        select = "SELECT count(*) FROM Kniha WHERE isbn = ?"
        cursor = conn.cursor()
        cursor.execute(select,[isbn])
        pocet = cursor.fetchone()[0]
        return pocet
    
    def pridejKnihu(self):
        kniha = (self.isbn,self.nazev,self.autor,self.rok,self.pocet)
        if(Kniha.kontrolaExistence(self.isbn)==0):
            insert = "INSERT INTO Kniha (isbn,nazev, autor, rok, pocet) VALUES (?, ?, ?, ?, ?)"
            cursor = conn.cursor()
            cursor.execute(insert,kniha)
            conn.commit()
            print("Kniha ",self.nazev," pridana ")

    
    def pridejPocet(self):
        update = "UPDATE Kniha SET pocet = pocet+1 WHERE isbn = ? "
        cursor = conn.cursor()
        cursor.execute(update,[self.isbn])
        conn.commit()

    def uberPocet(self):
        update = "UPDATE Kniha SET pocet = pocet-1 WHERE isbn = ?"
        cursor = conn.cursor()
        cursor.execute(update,[self.isbn])
        conn.commit()
        
class Zakaznik():
    def __init__(self,jmeno,prijmeni, rc):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rc = rc
        Zakaznik.pridejZakaznika(self)

    def kontrolaExistence(rc):
        select = "SELECT count(*) FROM Zakaznik WHERE rc=?"
        cursor = conn.cursor()
        cursor.execute(select,[rc])
        pocet = cursor.fetchone()[0]
        return pocet
    
    def pridejZakaznika(self):
        zakaznik = (self.rc,self.jmeno,self.prijmeni)
        if(Zakaznik.kontrolaExistence(self.rc)==0):
            insert = "INSERT INTO Zakaznik (rc, jmeno, prijmeni) VALUES (?, ?, ?)"
            cursor = conn.cursor()
            cursor.execute(insert,zakaznik)
            conn.commit()
            print("Zakaznik ",self.rc," pridan ")


class Vypujcka():
    def kontrolaPoctu(isbn):
        select = "SELECT pocet from Kniha where isbn = ?"
        cursor = conn.cursor()
        cursor.execute(select,[isbn])
        pocet = cursor.fetchone()[0]
        return pocet
    

    def zalozVypujcku(zakaznik,kniha):
        if(Vypujcka.kontrolaPoctu(kniha.isbn)>0):
            insert = "INSERT INTO Vypujcka(isbn,rc) VALUES(?,?)"
            cursor = conn.cursor()
            cursor.execute(insert,[kniha.isbn,zakaznik.rc])
            conn.commit()
            kniha.uberPocet()
        else:
            print("Neni dostatek knih")
                



k = Kniha("nejakerandomisbn","How to python","Adam",2022,1)
z = Zakaznik("Adam", "Pech", 9909094349)

Vypujcka.zalozVypujcku(z,k)


