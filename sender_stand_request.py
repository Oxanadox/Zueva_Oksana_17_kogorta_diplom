import requests
import configuration
import data


def post_new_order():
    current_body = data.order_body.copy()
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                             json=current_body,
                             )
    return response.json()["track"]


def get_order_with_track(track):
    params = {
        't': track,
    }
    response = requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER,
                             params=params
                             )
    return response


