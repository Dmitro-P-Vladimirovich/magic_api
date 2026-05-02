import pytest
import requests

from endpoints.create_url_endpoint import CreateUrlEndpoint

@pytest.fixture()
def url_creator_endp():
    return CreateUrlEndpoint()


@pytest.fixture()
def new_booking_id():
    body = {
            'firstname': 'Dmitro',
            'lastname': 'Ponomarev',
            'totalprice': 666,
            'depositpaid': True,
            'bookingdates': {
                'checkin': '2018-01-01',
                'checkout': '2019-01-01'
            },
            'additionalneeds': 'Breakfast'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://restful-booker.herokuapp.com/booking',
        headers=headers,
        json=body
    )
    booking_id = response.json()['bookingid']
    print(booking_id)
    print(response.json())
    return booking_id