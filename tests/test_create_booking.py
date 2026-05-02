import requests

def test_get_booking_by_id(new_booking_id):
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{new_booking_id}')
    assert response.status_code == 200
    assert response.json()['lastname'] == 'Ponomarev'


def test_create_booking(url_creator_endp):
    url_creator_endp.create_url_for_booking()
    url_creator_endp.check_response_status_is_ok()
    url_creator_endp.check_booking_id_is_not_empty()


