import requests

from pass_my_requests import request_and_responses


for elem in request_and_responses:
    r = requests.post('http://127.0.0.1:5000/predict', data=elem["Request"])
    try:
        r.raise_for_status()
        response = r.json()

        assert int(response.get('FlowerID', -1)) == elem['ExpectedResponse']['FlowerID']
        assert response.get('Species') == elem['ExpectedResponse']['Species:']
        print('Success')

    except requests.exceptions.HTTPError as err:
        print(err)
        print('Going to keep trying through the remainder of the requests')

    except AssertionError as err:
        print(err)
        print('Something fishy with the response. Continuing with the remainder of the requests.')
        print('expected: ', elem['ExpectedResponse'])
        print('actual: ', r.json())
