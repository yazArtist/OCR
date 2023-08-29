from enum import Enum

class DataTypes:
    PHONE_NUMBER = "phone_number"
    ID_NUMBER = "id_number"
    CREDIT_CARD_NUMBER = "credit_card_number"
    PLATE = "plate"
    DATE = "date"
    EMAIL = "email"
    DOMAIN = "domain"
    URL = "url"
    HASH = "hash"
    COMBOLIST = "combolist"

class Countries(Enum):
    TURKEY = "turkey"
    GERMANY = "germany"
    FRANCE = "france"
    UK = "uk"
    ITALY = "italy"
    SPAIN = "spain"
