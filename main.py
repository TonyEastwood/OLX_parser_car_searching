import constants_car as CC
import sqlite as SQ

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os.path
import threading
import inspect
import pickle

# cars_list = []
# with open('cars.csv', encoding='UTF8', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         car_list = []
#
#         for i in CC.CSV_HEADER:
#
#             if row[i] == '':
#                 car_list.append(" ")
#                 continue
#             row[i] = row[i].replace('\'','')
#             if i == "ціна":
#                 row[i] = row[i].replace(' ', '')
#                 if "$" in row[i]:
#                     row[i] = int(row[i].replace('$',''))
#                 elif "грн." in row[i]:
#                     row[i] = row[i].replace("грн.",'')
#                     row[i] = int(int(row[i]) / CC.EXCHANGE_RATE_HRYVNA_DOLLAR)
#                 elif "€" in row[i]:
#                     row[i] = int(row[i].replace('€', ''))
#                     row[i] = int(int(row[i]) * CC.EXCHANGE_RATE_EURO_DOLLAR)
#                 else:
#                     row[i] = 0
#             if i == "об'єм двигуна":
#                 row[i] = row[i].replace(' ', '')
#                 row[i] = float(row[i].replace('л.', ''))
#             if i == "рік випуску":
#                 row[i] = int(row[i].replace(' ', ''))
#             if i == "пробіг":
#                 row[i] = row[i].replace(' ', '')
#                 if "тис.км." in row[i]:
#                     row[i] = row[i].replace('тис.км.', '')
#                     row[i] = int(row[i])*1000
#             if i == "кількість місць":
#                 row[i] = row[i].replace(' ', '')
#                 if row[i] == '8ібільше':
#                     row[i] = 8
#                 else:
#                     row[i]= int(row[i])
#             if i == "кількість дверей":
#                 row[i] = row[i].replace(' ', '')
#                 row[i]= int(row[i])
#             if i == "розмитнена":
#                 row[i] = row[i].replace(' ', '')
#                 if row[i].lower() == 'так':
#                     row[i] = 'так'
#                 else:
#                     row[i] = 'ні'
#             if i == "дата створення":
#                 row[i] = int(row[i])
#
#             car_list.append(row[i])
#         car_list.append("локация")
#         #print(car_list)
#         cars_list.append(car_list)
# #print(cars_list)
# test_database = SQ.Cars_Database("cars_ad.db", "cars_table")
# test_database.Insert("cars_table", cars_list)
#test_list = []
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_list.append(CC.CSV_HEADER_DATABASETE)
#test_database.Insert(test_database.table_name,test_list)
#test_database.ShowDataInTable(test_database.table_name)


#URL = "https://www.olx.ua/d/transport/legkovye-avtomobili/"
URL = "https://www.olx.ua/d/uk/transport/legkovye-avtomobili/"
#URL = "https://www.olx.ua/d/uk/transport/legkovye-avtomobili/"
#URL = "https://www.olx.ua/d/uk/obyavlenie/great-wall-voleex-c30-IDO5vuR.html"
#URL = "https://www.olx.ua/d/uk/obyavlenie/prodam-volvo-v50-2-0-IDRhsbP.html"
#https://www.olx.ua/d/uk/obyavlenie/prodam-ford-fiesta-2007-rk-mozhliva-rozstrochka-kredit-IDS2mdv.html
cars_list = []
invalid_links = []
all_links_from_database = []

cars_database = SQ.Cars_Database(CC.DB_NAME, CC.DB_TABLE_NAME)


def GetAllPageElements(browser, searching_type, searching_value, waiting_time):
    try:
        elements = WebDriverWait(browser, waiting_time).until(
            EC.presence_of_all_elements_located((searching_type, searching_value)))
    except NoSuchElementException:
        print(GetCurrentLine() + "no such element")
        return ([],CC.TYPE_OPERATION_RESULT.NO_SUCH_ELEMENT_EXCEPTION)
    except TimeoutException:
        print(GetCurrentLine() + "too long to open page")
        return ([], CC.TYPE_OPERATION_RESULT.TIMEOUT_EXCEPTION)
    except:
        print(GetCurrentLine() + "Unknown error")
        return ([], CC.TYPE_OPERATION_RESULT.UNKNOWN_EXCEPTION)

    return (elements, CC.TYPE_OPERATION_RESULT.SUCCEED)

def GetPageElement(browser, searching_type, searching_value, waiting_time):
    try:
        element = WebDriverWait(browser, waiting_time).until(
            EC.presence_of_element_located((searching_type, searching_value)))
    except NoSuchElementException:
        print(GetCurrentLine() + "no such element")
        return (None,CC.TYPE_OPERATION_RESULT.NO_SUCH_ELEMENT_EXCEPTION)
    except TimeoutException:
        print(GetCurrentLine() + "too long to open page")
        return (None, CC.TYPE_OPERATION_RESULT.TIMEOUT_EXCEPTION)
    except:
        print(GetCurrentLine() + "Unknown error")
        return (None, CC.TYPE_OPERATION_RESULT.UNKNOWN_EXCEPTION)

    return (element, CC.TYPE_OPERATION_RESULT.SUCCEED)

def GetCurrentLine():
    """Returns the current line number in our program."""
    return "["+str(inspect.currentframe().f_back.f_lineno)+"] "


def UpdateLinksFromDatabase():
    global all_links_from_database
    all_links_from_database.clear()
    all_links_from_database = cars_database.SelectListOfDatasByColumn(CC.DB_TABLE_NAME,"link")

#def WriteCarsToCSVFile():
    # global cars_list
    # is_file_exist =  os.path.exists('cars.csv')
    #
    #
    # with open('cars.csv', 'a', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #
    #     if not is_file_exist:
    #         writer.writerow(CC.CSV_HEADER)
    #
    #     for car in cars_list:
    #         writer.writerow([car.creation_date, car.link, car.price, car.brand, car.model, car.release_year, car.engine_capacity, CC.FUEL[car.type_of_fuel],
    #                          car.mileage, car.color, CC.TRANSMISSION[car.transmission], CC.DRIVE[car.type_of_drive], CC.BODY[car.body_type],
    #                          car.came_from, car.seats, car.door, car.is_rastamozhena, car.state])

def GetMonthNumFromString(month):
    if month == "січня":
        return "01"
    elif month == "лютого":
        return "02"
    elif month == "березня":
        return "03"
    elif month == "квітня":
        return "04"
    elif month == "травня":
        return "05"
    elif month == "червня":
        return "06"
    elif month == "липня":
        return "07"
    elif month == "серпня":
        return "08"
    elif month == "вересня":
        return "09"
    elif month == "жовтня":
        return "10"
    elif month == "листопада":
        return "11"
    elif month == "грудня":
        return "12"
    else:
        print("Unkown month "+month)

class Car_Structure():
    def __init__(self):
        self.brand = None                #маркамашины
        self.model = None  # модель
        self.price = 0  # цена
        self.release_year = 0  # год выпуска
        self.engine_capacity = 0  # обьем двигателя
        self.type_of_fuel = CC.FUEL_TYPE.NONE  # тип топлива
        self.mileage = 0  # пробег
        self.color = None  # цвет
        self.transmission = CC.TRANSMISSION_TYPE.NONE  # коробка передач
        self.type_of_drive = CC.DRIVE_TYPE.NONE  # тип привода
        self.body_type = CC.BODY_TYPE.NONE  # тип кузова
        self.came_from = None   #откуда приехала
        self.seats = 0 # количество мест
        self.door = 0 #количество дверей
        self.is_rastamozhena = None  # растоможена ли
        self.state = None #состояние
        self.creation_date = 0  # дата создания обьявления
        self.link = None  #ссылка на обьявление
        self.ad_region = None  # где выставлено обьявление, область
        self.ad_city = None  # где выставлено обьявление, область


    def GetBrandFromString(self, string):
        for iterator in CC.TAG_BRAND:
            for brand in iterator:
                for j in iterator[brand]:
                    if j in string.lower():
                        return brand

    def GetRegionFromString(self, string):
        for iterator in CC.UK_REGION:
            for location in iterator:
                for j in iterator[location]:
                    if j in string.lower():
                        return location

    def GetCityFromString(self, string, brand):
        if brand in string:
            string = string.replace(brand,'')
        string = string.replace(' ', '')
        string = string.replace('\'', '')
        string = string.replace('-', '')
        return string.lower()


    def NormilizingPrice(self, price):
        if price is not None:
            price = price.text.replace(' ', '')
            if "$" in price:
                price = int(float(price.replace('$', '')))
            elif "грн." in price:
                price = price.replace("грн.", '')
                price = int(float(int(price) / CC.EXCHANGE_RATE_HRYVNA_DOLLAR))
            elif "€" in price:
                price = int(float(price.replace('€', '')))
                price = int(float(int(price) * CC.EXCHANGE_RATE_EURO_DOLLAR)
                            )
            else:
                price = 0
        else:
            return 0
        return price

    def NormilizingEngineCapacity(self, capacity):
        capacity = capacity.replace(' ', '')
        capacity = float(capacity.replace('л.', ''))
        return capacity

    def NormilizingYearRelease(self, year):
        year = int(year.replace(' ', ''))
        return year

    def NormilizingMileage(self, mileage):
        mileage = mileage.replace(' ', '')
        if "тис.км." in mileage:
            mileage = mileage.replace('тис.км.', '')
            mileage = int(mileage) * 1000
        return mileage

    def NormilizingSeats(self, seats):
        seats = seats.replace(' ', '')
        if seats == '8ібільше':
            seats = 8
        else:
            seats = int(seats)
        return seats

    def NormilizingDoors(self, doors):
        doors = doors.replace(' ', '')
        doors = int(doors)
        return doors

    def NormilizingRozmutn(self, rozmutn):
        rozmutn = rozmutn.replace(' ', '')
        if rozmutn.lower() == 'так':
            rozmutn = 'так'
        else:
            rozmutn = 'ні'
        return rozmutn

    def NormilizingCreationDate(self, creation_date):
        if creation_date is not None:
            if "сьогодні" in creation_date.lower():
                creation_date = int(date.today().strftime('%Y%m%d'))
            elif "вчора" in creation_date.lower():
                creation_date = int((date.today() - 1).strftime('%Y%m%d'))
            else:
                split_date = creation_date.split()
                creation_date = int(split_date[2] + GetMonthNumFromString(split_date[1]) + split_date[0])
        else:
            print(GetCurrentLine() + "Creation date can't be None!")
            return 0
        return creation_date

    def ConvertToDatabaseRaw(self):
        return [self.creation_date, self.link, self.price, self.brand, self.model, self.release_year, self.engine_capacity,
         CC.FUEL[self.type_of_fuel],
         self.mileage, self.color, CC.TRANSMISSION[self.transmission], CC.DRIVE[self.type_of_drive], CC.BODY[self.body_type],
         self.came_from, self.seats, self.door, self.is_rastamozhena, self.state, self.ad_region, self.ad_city]

    def FillInfoByBeautifulSoup(self, soup, link):

        self.link = link

        try:
            temp_date = soup.find('span', class_='css-19yf5ek')
            if temp_date != None:
                self.creation_date = self.NormilizingCreationDate(temp_date.text)
            else:
                print(GetCurrentLine() + " error")
                print(self.link)
        except:
            print(GetCurrentLine()+" error")
            print(self.link)


        self.price = self.NormilizingPrice(soup.find('h3', class_='css-ddweki er34gjf0'))

        tags = soup.find_all('li', class_='css-1r0si1e')
        for tag in tags:
            tag = tag.text.replace('\'','')
            if CC.TAG_CAME_FROM.lower() in tag.lower():
                self.came_from = tag.lower().replace(CC.TAG_CAME_FROM.lower(),"")
            elif CC.TAG_DOOR.lower() in tag.lower():
                self.door = self.NormilizingDoors(tag.lower().replace(CC.TAG_DOOR.lower(),""))
            elif CC.TAG_COLOR.lower() in tag.lower():
                self.color = tag.lower().replace(CC.TAG_COLOR.lower(),"")
            elif CC.TAG_SEATS.lower() in tag.lower():
                self.seats = self.NormilizingSeats(tag.lower().replace(CC.TAG_SEATS.lower(),""))
            elif CC.TAG_BODY_TYPE.lower() in tag.lower():
                body_type = tag.lower().replace(CC.TAG_BODY_TYPE.lower(),"")
                for i in CC.BODY:
                    if CC.BODY[i].lower() in body_type.lower():
                        self.body_type = i
                        break

            elif CC.TAG_ENGINE_CAPACITY.lower() in tag.lower():
                self.engine_capacity = self.NormilizingEngineCapacity(tag.lower().replace(CC.TAG_ENGINE_CAPACITY.lower(),""))
            elif CC.TAG_IS_RASTAMOZHENA.lower() in tag.lower():
                self.is_rastamozhena = self.NormilizingRozmutn(tag.lower().replace(CC.TAG_IS_RASTAMOZHENA.lower(),""))
            elif CC.TAG_MILEAGE.lower() in tag.lower():
                self.mileage = self.NormilizingMileage(tag.lower().replace(CC.TAG_MILEAGE.lower(),""))
            elif CC.TAG_MODEl.lower() in tag.lower():
                self.model = tag.lower().replace(CC.TAG_MODEl.lower(),"")
            elif CC.TAG_RELEASE_YEAR.lower() in tag.lower():
                self.release_year = self.NormilizingYearRelease(tag.lower().replace(CC.TAG_RELEASE_YEAR.lower(),""))
            elif CC.TAG_TRANSMISSION.lower() in tag.lower():
                transmission = tag.lower().replace(CC.TAG_TRANSMISSION.lower(),"")
                for i in CC.TRANSMISSION:
                    if CC.TRANSMISSION[i].lower() in transmission.lower():
                        self.transmission = i
                        break
            elif CC.TAG_TYPE_OF_DRIVE.lower() in tag.lower():
                self.type_of_drive = tag.lower().replace(CC.TAG_TYPE_OF_DRIVE.lower(),"")
                type_of_drive = tag.lower().replace(CC.TAG_TYPE_OF_DRIVE.lower(),"")

                for i in CC.DRIVE:
                    if CC.DRIVE[i].lower() in type_of_drive.lower():
                        self.type_of_drive = i
                        break

            elif CC.TAG_TYPE_OF_FUEL.lower() in tag.lower():
                type_of_fuel = tag.lower().replace(CC.TAG_TYPE_OF_FUEL.lower(),"")
                for i in CC.FUEL:
                    if CC.FUEL[i].lower() in type_of_fuel.lower():
                        self.type_of_fuel = i
                        break

            elif CC.TAG_STATE.lower() in tag.lower():
                self.state = tag.lower().replace(CC.TAG_STATE.lower(),"")

        headers = soup.find_all('a', class_='css-tyi2d1')

        for element in headers:
            if self.ad_region is not None:
                break
            self.ad_region = self.GetRegionFromString(element.text)

        for element in headers:
            if self.brand is not None:
                break
            self.brand = self.GetBrandFromString(element.text)

        if self.brand is None:
            name = soup.find('h1', class_='css-1soizd2 er34gjf0')
            description = soup.find('div', class_='css-bgzo2k er34gjf0')

            if name is not None:
                self.brand = self.GetBrandFromString(name.text)

            if self.brand is None:
                if description is not None:
                    self.brand = self.GetBrandFromString(description.text)

                if self.brand is None:
                    if self.model is not None:
                        self.brand = self.GetBrandFromString(self.model)

                if self.brand is None:
                    print(GetCurrentLine() + "can't find a brand")

        if self.brand is not None and len(headers)>5:
            self.ad_city = self.GetCityFromString(headers[5].text.lower(), self.brand)

    def ShowFullInfo(self):
        if self.brand is not None:
            print("Марка: "+self.brand)
        if self.price is not None:
            print("Цена: "+str(self.price))
        if self.model is not None:
            print("Модель: "+self.model)
        if self.release_year is not None:
            print("Год выпуска: "+str(self.release_year))
        if self.state is not None:
            print("Техническое состояние: "+self.state)
        if self.engine_capacity is not None:
            print("Обьем двигателя: "+str(self.engine_capacity))
        if self.type_of_fuel is not None:
            print("Тип горючего: "+CC.FUEL[self.type_of_fuel])
        if self.mileage is not None:
            print("Пробег: "+str(self.mileage))
        if self.color is not None:
            print("Цвет: "+self.color)
        if self.transmission is not None:
            print("Коробка передач: "+CC.TRANSMISSION[self.transmission])
        if self.type_of_drive is not None:
            print("Привод: "+CC.DRIVE[self.type_of_drive])
        if self.body_type is not None:
            print("Кузов: "+CC.BODY[self.body_type])
        if self.seats is not None:
            print("Количество мест: "+str(self.seats))
        if self.door is not None:
            print("Количество дверей: "+str(self.door))
        if self.is_rastamozhena is not None:
            print("Растоможена: "+self.is_rastamozhena)
        if self.came_from is not None:
            print("Приехала из: "+self.came_from)
        if self.creation_date is not None:
            print("Дата создания: "+str(self.creation_date))
        if self.link is not None:
            print("Ссылка: "+str(self.link))
        if self.ad_region is not None:
            print("Область: "+str(self.ad_region))
        if self.ad_city is not None:
            print("Город: "+str(self.ad_city))

def CarSearching(searching_browser, searching_URL):
    global cars_list
    current_ad = 0
    quantity_existent_links = 0
    while True:
        UpdateLinksFromDatabase()

        searching_browser.get(searching_URL)
        page = searching_browser.page_source
        soup = BeautifulSoup(page, "html.parser")

        quantity_page = 0

        while quantity_page <20:
            quantity_page = quantity_page + 1
            print("Page:" + str(quantity_page))

            elements_list, result = GetAllPageElements(searching_browser, By.CLASS_NAME, 'css-rc5s2u',30)

            if result == False:
                print(GetCurrentLine() + "result = False")
                continue

            for i in range(len(elements_list)):
                elements_list, result = GetAllPageElements(searching_browser, By.CLASS_NAME, 'css-rc5s2u',30)

                if result == False:
                    print(GetCurrentLine() + "result = False")
                    continue

                link = elements_list[i].get_attribute('href')


                if "https://www.olx" not in link:
                    print(GetCurrentLine() + "link out of the olx scope")
                    continue

                current_ad = current_ad + 1
                print(current_ad)

                if cars_database.IsRawWithDataExist(CC.DB_TABLE_NAME, "link", link) == 1:
                    quantity_existent_links = quantity_existent_links + 1
                    print("Bad links percentage:" + str(float(quantity_existent_links / current_ad * 100)))
                    continue

                searching_browser.get(link)

                element, result = GetPageElement(searching_browser, By.CLASS_NAME, 'css-dcwlyx', 30 )
                if result == CC.TYPE_OPERATION_RESULT.TIMEOUT_EXCEPTION:
                    print(GetCurrentLine() + " timeout exception")
                    searching_browser.back()
                    time.sleep(3)
                elif result != CC.TYPE_OPERATION_RESULT.SUCCEED:
                    continue

                page = searching_browser.page_source
                soup = BeautifulSoup(page, "html.parser")
                currentCar = Car_Structure()


                currentCar.FillInfoByBeautifulSoup(soup, link)
                cars_list.append(currentCar.ConvertToDatabaseRaw())

                if current_ad%10 ==0:
                    cars_database.Insert(CC.DB_TABLE_NAME, cars_list)

                    if invalid_links:
                        print("LINKS REMOVED: ")
                        print(invalid_links)
                        cars_database.RemoveLinks(CC.DB_TABLE_NAME, invalid_links)
                        invalid_links.clear()

                    cars_list.clear()

                if current_ad % 1000 == 0:
                    UpdateLinksFromDatabase()

                #try:
                searching_browser.back()
                #except NoSuchElementException:
                 #   print(GetCurrentLine() + "no such element")
                #    continue
                #except TimeoutException:
                 #   print(GetCurrentLine() + "too long to open page")
                  #  searching_browser.back()
                  #  continue
                #except:
                 #   print(GetCurrentLine() + "unknown error")
                  #  continue
            element, result = GetPageElement(searching_browser,By.CSS_SELECTOR, '[data-testid="pagination-forward"]', 30)

            if result == CC.TYPE_OPERATION_RESULT.TIMEOUT_EXCEPTION:
                print(GetCurrentLine() + " timeout exception")
                searching_browser.back()
                time.sleep(2)

                searching_browser.execute_script('arguments[0].click()', element)
                #button_next = WebDriverWait(searching_browser, 30).until(
                #    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="pagination-forward"]')))

        time.sleep(3)


def TestingCertainCar(searching_browser, searching_URL):
    searching_browser.get(searching_URL)

    page = searching_browser.page_source
    soup = BeautifulSoup(page, "html.parser")

    try:
        WebDriverWait(searching_browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-dcwlyx')))
        page = searching_browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        currentCar = Car_Structure()
        currentCar.FillInfoByBeautifulSoup(soup, searching_URL)
        currentCar.ShowFullInfo()
    except NoSuchElementException:
        print(GetCurrentLine() + "no such element")
    except TimeoutException:
        print(GetCurrentLine() + "too long to open page")



def BrowserInitializing():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("--headless")
    return webdriver.Chrome(options=option)

def save_cookie(driver):
    with open("cookie", 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)
def load_cookie(driver):
     driver.get(URL)
     with open("cookie", 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             #print(cookie)
             try:
                driver.add_cookie(cookie)
             except:
                print("cookie error")


def SearchingForInvalidLinksInDatabse(searching_browser):
    global all_links_from_database
    while True:
        links_list = all_links_from_database
        for link in links_list:
            try:
                searching_browser.get(link[0])
                WebDriverWait(searching_browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'css-dcwlyx')))
            except NoSuchElementException:
                print(GetCurrentLine() + "no such element")
                continue
            except TimeoutException:
                print(GetCurrentLine() + "too long to open page")
                invalid_links.append(link[0])
                print("FIND NEW INVALID LINK "+ link[0])
                print(invalid_links)
                searching_browser.back()
                continue
            except:
                print(GetCurrentLine() + "unknown error")
                continue

browser = BrowserInitializing()
browserForInvalidLinks = BrowserInitializing()

t1 = threading.Thread(target=SearchingForInvalidLinksInDatabse, args=(browserForInvalidLinks,))
t1.start()

CarSearching(browser, URL)
t1.join()

print("Done!")

#TestingCertainCar(browser, URL)

