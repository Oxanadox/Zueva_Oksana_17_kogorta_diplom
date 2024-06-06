import sender_stand_request

# Зуева Оксана, 17 когорта - финальный проект. Инженер по тестированию плюс.

def test_take_order_with_track():
    track = sender_stand_request.post_new_order()
    response = sender_stand_request.get_order_with_track(track)
    assert response.status_code == 200

