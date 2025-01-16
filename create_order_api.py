import configuration
import requests

def create_order(order_body):  #Функция для создания нового заказа
    response = requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=order_body)
    response.raise_for_status()
    return response

def get_order_by_track(order_track_number):  #Функция для получения информации о заказе по его трек-номеру
    response = requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + str(order_track_number))
    response.raise_for_status()
    return response