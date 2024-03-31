import sqlite3


class EquipmentManagementSystem:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ProductionRoom (
                                code INTEGER PRIMARY KEY,
                                description TEXT,
                                equipment_area REAL
                              )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS EquipmentType (
                                code INTEGER PRIMARY KEY,
                                description TEXT,
                                area REAL
                              )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS EquipmentContract (
                                number INTEGER PRIMARY KEY,
                                production TEXT,
                                equipment_type TEXT,
                                quantity INTEGER,
                                production_code INTEGER,
                                equipment_type_code INTEGER,
                                FOREIGN KEY (production_code) REFERENCES ProductionRoom(code),
                                FOREIGN KEY (equipment_type_code) REFERENCES EquipmentType(code)
                              )''')
        self.conn.commit()

    def add_production_room(self, description, equipment_area):
        self.cursor.execute("INSERT INTO ProductionRoom (description, equipment_area) VALUES (?, ?)",
                            (description, equipment_area))
        self.conn.commit()

    def add_equipment_type(self, description, area):
        self.cursor.execute("INSERT INTO EquipmentType (description, area) VALUES (?, ?)", (description, area))
        self.conn.commit()

    # изменить с учетом на площадь производственного помещения, чтобы в нем помещалось оборудование
    def add_equipment_contract(self, production_code, equipment_type_code, quantity):
        self.cursor.execute("SELECT description FROM ProductionRoom WHERE code=?", (production_code,))
        production_description = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT description FROM EquipmentType WHERE code=?", (equipment_type_code,))
        equipment_description = self.cursor.fetchone()[0]

        self.cursor.execute(
            "INSERT INTO EquipmentContract (number, production, equipment_type, quantity, production_code, equipment_type_code) VALUES (NULL, ?, ?, ?, ?, ?)",
            (production_description, equipment_description, quantity, production_code, equipment_type_code))
        self.conn.commit()

    def get_contracts(self):
        self.cursor.execute('''SELECT production, equipment_type, quantity FROM EquipmentContract''')
        contracts = self.cursor.fetchall()
        return contracts

    def check_production_room_code(self, code):
        self.cursor.execute("SELECT COUNT(*) FROM ProductionRoom WHERE code=?", (code,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def check_equipment_type_code(self, code):
        self.cursor.execute("SELECT COUNT(*) FROM EquipmentType WHERE code=?", (code,))
        count = self.cursor.fetchone()[0]
        return count > 0
