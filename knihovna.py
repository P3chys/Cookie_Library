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
    
    def pridejKnihu(self):
        kniha = (self.isbn,self.nazev,self.autor,self.rok,self.pocet)
        try:
            insert = "INSERT INTO Kniha (isbn,nazev, autor, rok, pocet) VALUES (?, ?, ?, ?, ?)"
            cursor = conn.cursor()
            cursor.execute(insert,kniha)
            conn.commit()
        except:
            print("Kniha ",self.nazev," jiz existuje v Databazi")
        else:
            print("Kniha ",self.nazev," pridana")

    def kontrolaPoctu(isbn):
        select = "SELECT pocet from Kniha where isbn = ?"
        cursor = conn.cursor()
        cursor.execute(select,[isbn])
        pocet = cursor.fetchone()[0]
        return pocet
    
    def pridejPocet(isbn):
        update = "UPDATE Kniha SET pocet = pocet+1 WHERE isbn = ? "
        cursor = conn.cursor()
        cursor.execute(update,[isbn])
        conn.commit()
        print("pocet zvysen")

    def uberPocet(isbn):
        update = "UPDATE Kniha SET pocet = pocet-1 WHERE isbn = ?"
        cursor = conn.cursor()
        cursor.execute(update,[isbn])
        conn.commit()
        print("pocet snizen")
        
class Zakaznik():
    def __init__(self,jmeno,prijmeni, rc):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rc = rc
        Zakaznik.pridejZakaznika(self)
    
    def pridejZakaznika(self):
        try:
            zakaznik = (self.rc,self.jmeno,self.prijmeni)
            insert = "INSERT INTO Zakaznik (rc, jmeno, prijmeni) VALUES (?, ?, ?)"
            cursor = conn.cursor()
            cursor.execute(insert,zakaznik)
            conn.commit()
        except:
            print("Zakaznik ",self.rc," jiz existuje v Databazi ")
        else:
            print("Zakaznik ",self.rc," pridan ")

class Vypujcka():
    
    
    def kontrolaVypujcky(isbn,rc):
        select = "SELECT COUNT(*) FROM Vypujcka WHERE isbn = ? AND rc = ?"
        cursor = conn.cursor()
        cursor.execute(select,(isbn,rc))
        pocet = cursor.fetchone()[0]
        return pocet

    def zalozVypujcku(rc,isbn):
        if(Kniha.kontrolaPoctu(isbn)>0 and Vypujcka.kontrolaVypujcky(isbn,rc)==0):
            insert = "INSERT INTO Vypujcka(isbn,rc,datum_vypujceni) VALUES(?,?,DATETIME('now'))"
            cursor = conn.cursor()
            cursor.execute(insert,[isbn,rc])
            conn.commit()
            Kniha.uberPocet(isbn)
            print("Vypujcka zalozena")
        else:
            print("Nelze zalozit vypujcku, jiz existuje nebo neni dostatek knih")


    def uzavriVypujcku(rc, isbn):
        if(Vypujcka.kontrolaVypujcky(isbn,rc)==1):
            insert = """
            INSERT INTO Vypujcka_old(isbn,rc,datum_vypujceni) 
            SELECT isbn, rc, datum_vypujceni FROM Vypujcka WHERE isbn = ? AND rc = ?
            """
            cursor = conn.cursor()
            cursor.execute(insert,(isbn,rc))
            conn.commit()

            delete = "DELETE FROM Vypujcka WHERE isbn=? AND rc = ?"
            cursor = conn.cursor()
            cursor.execute(delete,(isbn, rc))
            conn.commit()
            print("Vypujcka uzavrena")
            Kniha.pridejPocet(isbn)
        
        else:
            print("Vypujcka teto knihy pro tohoto cloveka neexistuje")
            



Kniha("nejakerandomisbn","How to python","Adam",2022,1)
Zakaznik("Adam", "Pech", 9909094349)
Vypujcka.uzavriVypujcku(9909094349,"nejakerandomisbn")




