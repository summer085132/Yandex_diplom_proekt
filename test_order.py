from create_order_api import create_order, get_order_by_track
import data

def test_create_and_get_order_by_track():
    # Создание заказа
    order_response = create_order(data.order_body)
    assert order_response.status_code == 201  # Проверка успешного создания заказа

    # Получить трек-номер заказа
    order_track_number = order_response.json().get("track")
    assert order_track_number is not None  # Проверка, что трек-номер получен

    # Получаем данные заказа
    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200  # Проверка успешного получения заказа по треку

# Мария Денисенко, 25 когорта, Финальный проект, инженер по тестированию плюс