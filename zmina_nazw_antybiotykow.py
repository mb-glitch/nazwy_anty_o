import pymssql

class ZmienNazwy:
    # połączenie z serwerem
    SERVER = "192.168.0.128"
    PORT = 1433
    USER = "ADMIN"
    PASSWORD = "***"
    DATABASE = "lab3000"

    antybiotyki = [
        {"ID_ANTYBIOTYKU": 1, "NAZWA_ANTYBIOT": "5-FLUOROCYTOZYNA", "NAZWA_POLSKA": "5-Fluorocytozyna"},
        {"ID_ANTYBIOTYKU": 2, "NAZWA_ANTYBIOT": "AMFOTERYCYNA B", "NAZWA_POLSKA": "Amfoterycyna B"},
        {"ID_ANTYBIOTYKU": 3, "NAZWA_ANTYBIOT": "AMPICILLIN", "NAZWA_POLSKA": "Ampicylina"},
        {"ID_ANTYBIOTYKU": 4, "NAZWA_ANTYBIOT": "AMOXICILLIN/CLAVULAN", "NAZWA_POLSKA": "Amoksycylina-kwas klawulanowy"},
        {"ID_ANTYBIOTYKU": 5, "NAZWA_ANTYBIOT": "AMOXICILLIN", "NAZWA_POLSKA": "Amoksycylina"},
        {"ID_ANTYBIOTYKU": 6, "NAZWA_ANTYBIOT": "AMIKACIN", "NAZWA_POLSKA": "Amikacyna"},
        {"ID_ANTYBIOTYKU": 7, "NAZWA_ANTYBIOT": "AZTREONAM", "NAZWA_POLSKA": "Aztreonam"},
        {"ID_ANTYBIOTYKU": 9, "NAZWA_ANTYBIOT": "AZITHROMYCIN", "NAZWA_POLSKA": "Azytromycyna"},
        {"ID_ANTYBIOTYKU": 10, "NAZWA_ANTYBIOT": "CHLORAMPHENICOL", "NAZWA_POLSKA": "Chloramfenikol"},
        {"ID_ANTYBIOTYKU": 11, "NAZWA_ANTYBIOT": "CEFTAZIDIME", "NAZWA_POLSKA": "Ceftazydym"},
        {"ID_ANTYBIOTYKU": 13, "NAZWA_ANTYBIOT": "CLINDAMYCIN", "NAZWA_POLSKA": "Klindamycyna"},
        {"ID_ANTYBIOTYKU": 14, "NAZWA_ANTYBIOT": "CEFACLOR", "NAZWA_POLSKA": "Cefaklor"},
        {"ID_ANTYBIOTYKU": 15, "NAZWA_ANTYBIOT": "CEPHALOTHIN", "NAZWA_POLSKA": "Cefalotin"},
        {"ID_ANTYBIOTYKU": 16, "NAZWA_ANTYBIOT": "CEFIXIME", "NAZWA_POLSKA": "Cefiksym"},
        {"ID_ANTYBIOTYKU": 18, "NAZWA_ANTYBIOT": "CIPROFLOXACIN", "NAZWA_POLSKA": "Cyprofloksacyna"},
        {"ID_ANTYBIOTYKU": 19, "NAZWA_ANTYBIOT": "CLARITROMYCIN", "NAZWA_POLSKA": "Klarytromycyna"},
        {"ID_ANTYBIOTYKU": 20, "NAZWA_ANTYBIOT": "CEFTRIAXONE", "NAZWA_POLSKA": "Ceftriakson"},
        {"ID_ANTYBIOTYKU": 22, "NAZWA_ANTYBIOT": "CEFOTAXIME", "NAZWA_POLSKA": "Cefotaksym"},
        {"ID_ANTYBIOTYKU": 23, "NAZWA_ANTYBIOT": "CEFUROXIME", "NAZWA_POLSKA": "Cefuroksym"},
        {"ID_ANTYBIOTYKU": 24, "NAZWA_ANTYBIOT": "CEFAZOLIN", "NAZWA_POLSKA": "Cefazolina"},
        {"ID_ANTYBIOTYKU": 25, "NAZWA_ANTYBIOT": "DOXYCYCLINE", "NAZWA_POLSKA": "Doksycyklina"},
        {"ID_ANTYBIOTYKU": 26, "NAZWA_ANTYBIOT": "ERYTHROMYCIN", "NAZWA_POLSKA": "Erytromycyna"},
        {"ID_ANTYBIOTYKU": 28, "NAZWA_ANTYBIOT": "NITROFURANTOIN", "NAZWA_POLSKA": "Nitrofurantoina"},
        {"ID_ANTYBIOTYKU": 29, "NAZWA_ANTYBIOT": "CEFEPIME", "NAZWA_POLSKA": "Cefepim"},
        {"ID_ANTYBIOTYKU": 30, "NAZWA_ANTYBIOT": "FLUCONAZOLE", "NAZWA_POLSKA": "Flukonazol"},
        {"ID_ANTYBIOTYKU": 31, "NAZWA_ANTYBIOT": "FOSFOMYCINE", "NAZWA_POLSKA": "Fosfomycyna"},
        {"ID_ANTYBIOTYKU": 32, "NAZWA_ANTYBIOT": "CEFOXITIN", "NAZWA_POLSKA": "Cefoksytyna"},
        {"ID_ANTYBIOTYKU": 34, "NAZWA_ANTYBIOT": "GENTAMYCIN", "NAZWA_POLSKA": "Gentamycyna"},
        {"ID_ANTYBIOTYKU": 35, "NAZWA_ANTYBIOT": "GENTAMYCIN 120", "NAZWA_POLSKA": "Gentamycyna 120"},
        {"ID_ANTYBIOTYKU": 36, "NAZWA_ANTYBIOT": "ITRAKONAZOL", "NAZWA_POLSKA": "Itrakonazol"},
        {"ID_ANTYBIOTYKU": 37, "NAZWA_ANTYBIOT": "IMIPENEM", "NAZWA_POLSKA": "Imipenem"},
        {"ID_ANTYBIOTYKU": 39, "NAZWA_ANTYBIOT": "KETOKONAZOL", "NAZWA_POLSKA": "Ketokonazol"},
        {"ID_ANTYBIOTYKU": 41, "NAZWA_ANTYBIOT": "MEROPENEM", "NAZWA_POLSKA": "Meropenem"},
        {"ID_ANTYBIOTYKU": 43, "NAZWA_ANTYBIOT": "MIKONAZOL", "NAZWA_POLSKA": "Mikonazol"},
        {"ID_ANTYBIOTYKU": 44, "NAZWA_ANTYBIOT": "MOXALACTAM", "NAZWA_POLSKA": "Latamoxef"},
        {"ID_ANTYBIOTYKU": 49, "NAZWA_ANTYBIOT": "NETILMYCIN", "NAZWA_POLSKA": "Netylmycyna"},
        {"ID_ANTYBIOTYKU": 50, "NAZWA_ANTYBIOT": "TOBRAMYCIN", "NAZWA_POLSKA": "Tobramycyna"},
        {"ID_ANTYBIOTYKU": 51, "NAZWA_ANTYBIOT": "NORFLOXACIN", "NAZWA_POLSKA": "Norfloksacyna"},
        {"ID_ANTYBIOTYKU": 53, "NAZWA_ANTYBIOT": "OFLOXACIN", "NAZWA_POLSKA": "Ofloksacyna"},
        {"ID_ANTYBIOTYKU": 54, "NAZWA_ANTYBIOT": "OXACILLIN", "NAZWA_POLSKA": "Oksacylina"},
        {"ID_ANTYBIOTYKU": 55, "NAZWA_ANTYBIOT": "PENICILLIN", "NAZWA_POLSKA": "Penicylina"},
        {"ID_ANTYBIOTYKU": 59, "NAZWA_ANTYBIOT": "PIPERACILLIN", "NAZWA_POLSKA": "Piperacylina"},
        {"ID_ANTYBIOTYKU": 60, "NAZWA_ANTYBIOT": "RIFAMPIN", "NAZWA_POLSKA": "Ryfampicyna"},
        {"ID_ANTYBIOTYKU": 61, "NAZWA_ANTYBIOT": "STREPTOMYCIN 300", "NAZWA_POLSKA": "Streptomycyna 300"},
        {"ID_ANTYBIOTYKU": 62, "NAZWA_ANTYBIOT": "AMPICILLIN/SULBACTAM", "NAZWA_POLSKA": "Ampicylina-sulbaktam"},
        {"ID_ANTYBIOTYKU": 64, "NAZWA_ANTYBIOT": "TRIMETH/SULFAMET.", "NAZWA_POLSKA": "Trimetoprim-sulfametoksazol"},
        {"ID_ANTYBIOTYKU": 66, "NAZWA_ANTYBIOT": "TETRACYCLINE", "NAZWA_POLSKA": "Tetracyklina"},
        {"ID_ANTYBIOTYKU": 67, "NAZWA_ANTYBIOT": "TEIKOPLANIN", "NAZWA_POLSKA": "Teikoplanina"},
        {"ID_ANTYBIOTYKU": 68, "NAZWA_ANTYBIOT": "TICARCILLIN", "NAZWA_POLSKA": "Tykarcylina"},
        {"ID_ANTYBIOTYKU": 69, "NAZWA_ANTYBIOT": "TICARCILLIN/CLAVULAN", "NAZWA_POLSKA": "Tykarcylina-kwas klawulanowy"},
        {"ID_ANTYBIOTYKU": 70, "NAZWA_ANTYBIOT": "TRIMETHOPRIM", "NAZWA_POLSKA": "Trimetoprym"},
        {"ID_ANTYBIOTYKU": 71, "NAZWA_ANTYBIOT": "PIPERACILLIN/TAZOBACTAM", "NAZWA_POLSKA": "Piperacylina-tazobaktam"},
        {"ID_ANTYBIOTYKU": 72, "NAZWA_ANTYBIOT": "VANCOMYCIN", "NAZWA_POLSKA": "Wankomycyna"},
        {"ID_ANTYBIOTYKU": 75, "NAZWA_ANTYBIOT": "FUSIDIC ACID", "NAZWA_POLSKA": "Kwas fusydynowy"},
        {"ID_ANTYBIOTYKU": 76, "NAZWA_ANTYBIOT": "CHINOPRISTINA", "NAZWA_POLSKA": "Chinupristina"},
        {"ID_ANTYBIOTYKU": 79, "NAZWA_ANTYBIOT": "LEWOFLOXACIN", "NAZWA_POLSKA": "Lewofloksacyna"},
        {"ID_ANTYBIOTYKU": 81, "NAZWA_ANTYBIOT": "LINEZOLID", "NAZWA_POLSKA": "Linezolid"},
        {"ID_ANTYBIOTYKU": 82, "NAZWA_ANTYBIOT": "VORICONAZOL", "NAZWA_POLSKA": "Voriconazol"},
        {"ID_ANTYBIOTYKU": 83, "NAZWA_ANTYBIOT": "COLISTIN", "NAZWA_POLSKA": "Kolistyna"},
        {"ID_ANTYBIOTYKU": 84, "NAZWA_ANTYBIOT": "TIGECYCLINE", "NAZWA_POLSKA": "Tigecyklina"},
        {"ID_ANTYBIOTYKU": 86, "NAZWA_ANTYBIOT": "MOXIFLOXACIN", "NAZWA_POLSKA": "Moksifloksacyna"},
        {"ID_ANTYBIOTYKU": 87, "NAZWA_ANTYBIOT": "GENTAMYCIN 30", "NAZWA_POLSKA": "Gentamycyna 30"},
        {"ID_ANTYBIOTYKU": 89, "NAZWA_ANTYBIOT": "METYCYLINA", "NAZWA_POLSKA": "Metycylina"},
        ]

    sql_polskie_na_miedzynarodowe = "update antybiotyki set NAZWA_ANTYBIOT='{NAZWA_ANTYBIOT}' where ID_ANTYBIOTYKU={ID_ANTYBIOTYKU}"
    sql_miedzynarodowe_na_polskie = "update antybiotyki set NAZWA_ANTYBIOT='{NAZWA_POLSKA}' where ID_ANTYBIOTYKU={ID_ANTYBIOTYKU}"

    def __init__(self):
        self.conn = None

    def connect(self):
        # charakterystyka usawienia połączenia z bazą
        self.conn = pymssql.connect(
        server = self.SERVER,
        port = self.PORT,
        user = self.USER,
        password = self.PASSWORD,
        database = self.DATABASE,
        charset = 'cp1250')

    def disconnect_from_db(self):
        self.conn.close()

    def zmien_na_polskie(self):
        if not self.conn:
            self.connect()
        for antybiotyk in self.antybiotyki:
            sql = self.sql_miedzynarodowe_na_polskie.format(NAZWA_POLSKA=antybiotyk['NAZWA_POLSKA'],
                                                    ID_ANTYBIOTYKU=antybiotyk['ID_ANTYBIOTYKU'])
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
        self.conn.commit()
        self.disconnect_from_db()

    def zmien_na_miedzynarodowe(self):
        if not self.conn:
            self.connect()
        for antybiotyk in self.antybiotyki:
            sql = self.sql_polskie_na_miedzynarodowe.format(NAZWA_ANTYBIOT=antybiotyk['NAZWA_ANTYBIOT'],
                                                    ID_ANTYBIOTYKU=antybiotyk['ID_ANTYBIOTYKU'])

            with self.conn.cursor() as cursor:
                cursor.execute(sql)
        self.conn.commit()
        self.disconnect_from_db()




    

