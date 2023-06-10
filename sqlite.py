import sqlite3
import constants_car as CC

class Cars_Database():
    def __init__(self, database_name, table_name):
        self.database = sqlite3.connect(database_name)
        self.cursor = self.database.cursor()
        self.table_name = table_name
        self.CreateTable(self.table_name)

    def CreateTable(self, table_name):
        raws_names = []
        for i in CC.CSV_HEADER_DATABASE:
            raws_names.append(str(i))
        raws_names_string = ', '.join(raws_names)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + "("+raws_names_string+")")

    def Insert(self, table_name, list_elements):
        car_ads_list = []
        car_ads_string = ""
        for car_ad in list_elements:
            raws_list = []
            for raw in car_ad:
                if str(raw).isdigit():
                    raws_list.append(str(raw))
                else:
                    raws_list.append('\''+str(raw)+'\'')
            raws_list_string = ', '.join(raws_list)
            raws_list_string = "("+raws_list_string+")"
            car_ads_list.append(raws_list_string)
        car_ads_string = ', '.join(car_ads_list)

        self.cursor.execute(""
                    "INSERT INTO "+ table_name+ " VALUES"+
                            car_ads_string+""
                "")

        self.database.commit()

    def ShowDataInTable(self, table_name):
        res = self.cursor.execute("SELECT brand FROM "+table_name)
        m = res.fetchall()

    def Close(self):
        self.database.close()

#test_database = Cars_Database("cars_ad.db", "cars_table")

#test_list = []
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_database.Insert(test_database.table_name,test_list)
#test_database.ShowDataInTable(test_database.table_name)