import enum

EXCHANGE_RATE_HRYVNA_DOLLAR = 37
EXCHANGE_RATE_EURO_DOLLAR = 1.08

DB_NAME = "cars_ad.db"
DB_TABLE_NAME = "cars_table"

#CSV_HEADER = ["дата створення","посилання","ціна","бренд","модель","рік випуску","об'єм двигуна","вид палива","пробіг","колір","коробка передач","тип приводу",
#              "кузов","пригнано з","кількість місць","кількість дверей","розмитнена","технічний стан"]
CSV_HEADER_DATABASE = ["data_creation","link","price","brand","model","year_release","engine_capacity","fuel_type","mileage","color","transmission","drive_type",
              "body","from_country","quantity_places","quantity_doors","rozmutnena","tech_state","region","city"]

CSV_HEADER_DATABASETE = ["data_creation","link","price","brand",10,"year_release","engine_capacity","fuel_type","mileage","color","transmission","drive_type",
              "body","from_country","quantity_places","quantity_doors","rozmutnena","tech_state","region"]

TAG_MODEl = "Модель: "  # модель
TAG_RELEASE_YEAR = "Рік випуску: "  # год выпуска
TAG_ENGINE_CAPACITY = "Обєм двигуна: "  # обьем двигателя
TAG_TYPE_OF_FUEL = "Вид палива: "  # тип топлива
TAG_MILEAGE = "Пробіг: "  # пробег
TAG_COLOR = "Kолір: "  # цвет
TAG_TRANSMISSION = "Коробка передач: "  # коробка передач
TAG_TYPE_OF_DRIVE = "Тип приводу: "  # тип привода
TAG_BODY_TYPE = "Тип кузова: "  # тип кузова
TAG_CAME_FROM = "Авто пригнано з: "   #откуда приехала
TAG_SEATS = "Кількість місць: " # количество мест
TAG_DOOR = "Кількість дверей: " #количество дверей
TAG_IS_RASTAMOZHENA = "Розмитнена: "  # растоможена ли
TAG_STATE = "Технічний стан: "

class TRANSMISSION_TYPE(enum.Enum):
    MECHANIC = 0
    AUTOMATIC = 1
    VARIATOR = 2
    ADAPTIVE = 3
    TIPTRONIK = 4
    NONE = 5

class FUEL_TYPE(enum.Enum):
    PETROL = 0
    DIESEL = 1
    GAS = 2
    ELECTRO = 3
    HYBRID = 4
    NONE = 5

class BODY_TYPE(enum.Enum):
    CABRIOLET = 0
    PICKUP = 1
    COUPE = 2
    UNIVERSAL = 3
    HATCHBACK = 4
    MINIVAN = 5
    CROSSOVER = 6
    SEDAN = 7
    NONE = 8

class DRIVE_TYPE(enum.Enum):
    FULL = 0
    FRONT = 1
    REAR = 2
    NONE = 3

TRANSMISSION_TYPE_STRING_MECHANIG ="механічна"
TRANSMISSION_TYPE_STRING_AUTOMATIC ="автоматична"
TRANSMISSION_TYPE_STRING_VARIATOR ="варіатор"
TRANSMISSION_TYPE_STRING_ADAPTIVE ="адаптивна"
TRANSMISSION_TYPE_STRING_TIPTRONIK ="типтронік"

FUEL_TYPE_STRING_PETROL ="бензин"
FUEL_TYPE_STRING_DIESEL ="дизель"
FUEL_TYPE_STRING_GAS ="газ"
FUEL_TYPE_STRING_ELECTRO ="електро"
FUEL_TYPE_STRING_HYBRID ="гібрид"

BODY_TYPE_STRING_CABRIOLET ="кабріолет"
BODY_TYPE_STRING_PICKUP ="пікап"
BODY_TYPE_STRING_COUPE ="купе"
BODY_TYPE_STRING_UNIVERSAL ="унiверсал"
BODY_TYPE_STRING_HATCHBACK ="хетчбек"
BODY_TYPE_STRING_MINIVAN ="мінівен"
BODY_TYPE_STRING_CROSSOVER ="кроссовер"
BODY_TYPE_STRING_SEDAN ="седан"

DRIVE_TYPE_STRING_FULL ="повний"
DRIVE_TYPE_STRING_FRONT ="передній"
DRIVE_TYPE_STRING_REAR ="задній"

TRANSMISSION = {TRANSMISSION_TYPE.MECHANIC:TRANSMISSION_TYPE_STRING_MECHANIG,
                TRANSMISSION_TYPE.TIPTRONIK:TRANSMISSION_TYPE_STRING_TIPTRONIK,
                TRANSMISSION_TYPE.ADAPTIVE:TRANSMISSION_TYPE_STRING_ADAPTIVE,
                TRANSMISSION_TYPE.VARIATOR:TRANSMISSION_TYPE_STRING_VARIATOR,
                TRANSMISSION_TYPE.AUTOMATIC:TRANSMISSION_TYPE_STRING_AUTOMATIC,
                TRANSMISSION_TYPE.NONE:""}

FUEL =         {FUEL_TYPE.GAS:FUEL_TYPE_STRING_GAS,
                FUEL_TYPE.DIESEL:FUEL_TYPE_STRING_DIESEL,
                FUEL_TYPE.HYBRID:FUEL_TYPE_STRING_HYBRID,
                FUEL_TYPE.PETROL:FUEL_TYPE_STRING_PETROL,
                FUEL_TYPE.ELECTRO:FUEL_TYPE_STRING_ELECTRO,
                FUEL_TYPE.NONE:""}

DRIVE =        {DRIVE_TYPE.FULL:DRIVE_TYPE_STRING_FULL,
                DRIVE_TYPE.REAR:DRIVE_TYPE_STRING_REAR,
                DRIVE_TYPE.FRONT:DRIVE_TYPE_STRING_FRONT,
                DRIVE_TYPE.NONE:""}

BODY =         {BODY_TYPE.COUPE:BODY_TYPE_STRING_COUPE,
                BODY_TYPE.SEDAN:BODY_TYPE_STRING_SEDAN,
                BODY_TYPE.MINIVAN:BODY_TYPE_STRING_MINIVAN,
                BODY_TYPE.PICKUP:BODY_TYPE_STRING_PICKUP,
                BODY_TYPE.CABRIOLET:BODY_TYPE_STRING_CABRIOLET,
                BODY_TYPE.CROSSOVER: BODY_TYPE_STRING_CROSSOVER,
                BODY_TYPE.HATCHBACK: BODY_TYPE_STRING_HATCHBACK,
                BODY_TYPE.UNIVERSAL: BODY_TYPE_STRING_UNIVERSAL,
                BODY_TYPE.NONE:""}

UK_REGION = [{"дніпропетровська область":{"дніпропетровська область"}},
             {"сумська область":{"сумська область"}},
             {"івано-франківська область":{"івано-франківська область"}},
             {"вінницька область":{"вінницька область"}},
             {"волинська область":{"волинська область"}},
             {"донецька область":{"донецька область"}},
             {"житомирська область":{"житомирська область"}},
             {"закарпатська область":{"закарпатська область"}},
             {"запорізька область":{"запорізька область"}},
             {"кіровоградська область":{"кіровоградська область"}},
             {"київська область":{"київська область"}},
             {"крим":{"крим"}},
             {"луганська область":{"луганська область"}},
             {"львівська область":{"львівська область"}},
             {"миколаївська область":{"миколаївська область"}},
             {"одеська область":{"одеська область"}},
             {"полтавська область":{"полтавська область"}},
             {"рівненська область":{"рівненська область"}},
             {"тернопільська область":{"тернопільська область"}},
             {"харківська область":{"харківська область"}},
             {"херсонська область":{"херсонська область"}},
             {"хмельницька область":{"хмельницька область"}},
             {"черкаська область":{"черкаська область"}},
             {"чернівецька область":{"чернівецька область"}},
             {"чернігівська область":{"чернігівська область"}},
             ]

TAG_BRAND = [{"bmw":{"bmw","беха","бээмвэшка","бэха","бумер","бмв"}},
             {"audi":{"audi","ауди","ауді"}},
            {"volkswagen":{"volkswagen","вольсксваген","passat","пасат","фольксваген","пассат","фольсваген","джетта","jetta"}},
            {"daewoo":{"daewoo","ланос","део"}},
            {"opel":{"opel","опель","вектра"}},
            {"hyundai":{"hyundai","santa fe","tucson","хюндай","sonata","соната"}},
            {"chevrolet ":{"chevrolet ","lacetti"}},
            {"ford":{"ford","форд","мондео","mondeo"}},
            {"tesla":{"tesla","тесла"}},
            {"kia":{"kia","киа","рио","rio"}},
            {"nissan":{"nissan","нисан","ниссан","rogue"}},
            {"mercedes-benz":{"mercedes-benz","мерс","мерседес","mercedes-bens","mercedes","mersedes"}},
            {"chrysler":{"chrysler"}},
            {"subaru":{"subaru","субару"}},
            {"skoda":{"skoda","шкода","octavia","октавиа","октавія"}},
            {"renault":{"renault","reno"}},
            {"mazda":{"mazda","мазда"}},
            {"honda":{"honda","хонда"}},
            {"citroen":{"citroen","ситроен","сітроен","berlingo"}},
            {"geely":{"geely","gelly","джили","джилли","джилі"}},
            {"peugeot":{"peugeot","пежо","пижо","піжо"}},
            {"fiat":{"fiat","фиат","фіат"}},
            {"toyota":{"toyota","тайота","сorolla","корола","королла"}},
            {"infinity":{"infinity","инфинити","інфініті","lnfiniti"}},
            {"jeep":{"jeep"}},
            {"chery":{"chery","cheri","чері","чери"}},
            {"gazel":{"gazel","газель"}},
            {"lexus":{"lexus","лексус"}},
            {"ваз": {"vaz", "ваз", "2112", "21013", "2114", "lada", "лада", "копейка", "копейку","2110","заз","таврия","таврія","москвич","уаз","уазик","2172"}},
            {"ssangyong":{"ssangyong","сангйонг"}},
            {"mitsubishi":{"mitsubishi","митсубиси","мітсубісі"}},
            {"gaz":{"gaz","газ","волга","volga"}},
            {"dodge":{"dodge","додж"}},
            {"volvo":{"volvo","вольво"}},
            {"byd":{"byd"}},
            {"smart":{"smart","смарт"}},
            {"seat":{"seat","сиат","сіат"}},
            {"porsche":{"porsche","порше","порш"}},
            {"great wall":{"great wall","greatwall"}},
            {"faw":{"faw","фав"}},
            {"maserati":{"maserati","мазерати","мазераті"}},
            {"buick":{"buick"}},
            {"dacia":{"dacia"}},
            {"cadillac":{"cadillac","кадилак"}},
            {"jac":{"jac"}},
            {"alfa romeo":{"alfa romeo"}},
            {"mini":{"mini"}},
            {"suzuki":{"suzuki","сузуки"}},
            {"ravon":{"ravon"}},
            {"samand":{"samand"}},
            {"land rover":{"land rover"}},
            {"range rover":{"range rover"}},
            {"lancia":{"lancia"}},
            {"lincoln":{"lincoln"}},
            {"saab":{"saab"}},
            {"jaguar":{"jaguar"}},
            {"acura":{"acura"}}

             ]                #маркамашины