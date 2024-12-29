import pytest
import logging
import json
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = 'http://127.0.0.1:8080'

class TestFlaskApp:

    @pytest.fixture(scope='class')
    def auth(self):
        url_auth = BASE_URL + '/auth'

        with requests.Session() as s:
            request_ = s.post(url_auth, auth=HTTPBasicAuth('test_user', 'test_pass'))
            stat_code = request_.status_code
            access_token = json.loads(request_.text)['access_token']
            s.headers.update({'Authorization': 'Bearer ' + access_token})
            print('status_code: ', stat_code)
            print('access_token: ', access_token)

        yield stat_code, access_token

    @pytest.fixture()
    def logger(self):

        # Створення та налаштування логера
        logging.basicConfig(filename='test_path.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG,
                            force=True)
        logger = logging.getLogger()
        yield logger

    def test_auth(self, logger, auth):
        if auth[0] == 200:
            logging.info('Successful authentication')
        elif auth[0] != 200:
            logging.error('Wrong authentication!')
        assert auth[0] == 200

    @pytest.fixture(params=
                    [('price', 2),
                     ('engine_volume', 3),
                     ('year', 4)])
    def input_data(self, request):
        return request.param

    def test_get_cars(self, logger, auth, input_data):
        url_get = BASE_URL + '/cars'
        token = auth[1]
        headers = {'Authorization': f'Bearer {token}'}
        params = {'sort_by': input_data[0], 'limit': input_data[1]}

        response_get = requests.request("GET", url_get, headers=headers, params=params)

        sts_code = response_get.status_code

        print(response_get.text)

        if sts_code == 200:
            logging.info('Successful Get request')
        elif auth[0] != 200:
            logging.error('Wrong Get request!')

        content_length = len(json.loads(response_get.text))

        assert sts_code == 200
        assert content_length == input_data[1]

# PARAMETRIZE
    @pytest.mark.parametrize('sort_by, limit',
                     [
                         ('brand', 3),
                         ('price', 5)
                     ])
    def test_get_cars_mark_params(self, logger, auth, sort_by, limit):
        url_get = BASE_URL + '/cars'
        token = auth[1]
        headers = {'Authorization': f'Bearer {token}'}
        params = {'sort_by': {sort_by}, 'limit': {limit}}

        response_get = requests.request("GET", url_get, headers=headers, params=params)

        logger.status_code = response_get.status_code
        logger.status_code_to_compare = 200
        print(response_get.text)

        sts_code = response_get.status_code

        if sts_code == 200:
            logging.info('Successful Get request')
        elif auth[0] != 200:
            logging.error('Wrong Get request!')

        content_length = len(json.loads(response_get.text))

        assert sts_code == 200
        assert content_length == limit

