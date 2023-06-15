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
                    "INSERT or REPLACE INTO "+ table_name+ " VALUES"+
                            car_ads_string+""
                "")

        self.database.commit()

    def RemoveLinks(self, table_name, links_list):
        for i in range(len(links_list)):
            links_list[i] = 'link = \'' + links_list[i] + '\''
        sql_request = ' OR '.join(links_list)
        print(sql_request)

        self.cursor.execute(""
                        "DELETE from "+table_name+" where " +sql_request +
                        "")
        self.database.commit()

    def ShowDataInTable(self, table_name):
        res = self.cursor.execute("SELECT brand FROM "+table_name)
        m = res.fetchall()

    def SelectListOfDatasByColumn(self, table_name, column_name):
        self.cursor.execute("SELECT "+column_name+" FROM "+table_name + " ORDER BY data_creation ASC")
        rows = self.cursor.fetchall()
        return rows

    def IsRawWithDataExist(self, table_name, column_name, data):
        res = self.cursor.execute("SELECT EXISTS(SELECT * FROM " + table_name + " WHERE "+column_name + "=\'"+data+"\')")
        rows = self.cursor.fetchall()
        return rows[0][0]
        #return rows

    def Close(self):
        self.database.close()


#test_database = Cars_Database(CC.DB_NAME, CC.DB_TABLE_NAME)
#test_database.IsRawWithDataExist(CC.DB_TABLE_NAME,"link","https://www.olx.ua/d/uk/obyavlenie/shevrole-kaptva-2008-r-2-0-dizel-IDSb5cI.html")
#test_database.SelectListOfDatasByColumn(CC.DB_TABLE_NAME,"link")
# link_list = []
#
# link1 = "https://www.olx.ua/d/uk/obyavlenie/bmw-x5-hybrid-plug-in-2016-IDSaUTp.html"
# link2 = "https://www.olx.ua/d/uk/obyavlenie/seat-altea-xl-tsi-IDOs4RU.html"
# link3 = "https://www.olx.ua/d/uk/obyavlenie/2015-jeep-cherokee-trailhawk-IDSaUOR.html"
# link4= "https://www.olx.ua/d/uk/obyavlenie/srochno-vaz-2114-srochno-IDS9c9I.html"
# link_list.append(link1)
# link_list.append(link2)
# test_database.RemoveLinks(CC.DB_TABLE_NAME, link_list)
#test_list = []
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_database.Insert(test_database.table_name,test_list)
#test_database.ShowDataInTable(test_database.table_name)