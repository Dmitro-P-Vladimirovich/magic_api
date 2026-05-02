import requests
from endpoints.status_code_endpoint import Endpoint

class CreateUrlEndpoint(Endpoint):
    lastname = None
    booking_id = None

    def create_url_for_booking(self):
        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            headers={'Content-Type': 'application/json'},
            json={
                'firstname': 'Dmitriy',
                'lastname': 'Ponomarev',
                'totalprice': 666,
                'depositpaid': True,
                'bookingdates': {
                    'checkin': '2018-01-01',
                    'checkout': '2019-01-01'
                },
                'additionalneeds': 'Breakfast'}
        )
        self.status = response.status_code
        self.lastname = response.json()['booking']['lastname']
        self.booking_id = response.json()['bookingid']
        return response


    def check_booking_id_is_not_empty(self):
        assert self.booking_id > 0




