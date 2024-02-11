import json
import logging
import os.path

import allure
from allure_commons.types import AttachmentType
from requests import Session, Response
from curlify import to_curl
from jsonschema import validate
from datetime import datetime
from pathlib import Path

def load_json_schema(file_name):
    schema_path = os.path.join(Path(__file__).parents[1], 'schemas', file_name)
    with open(schema_path) as schema:
        return json.loads(schema.read())


class ReqresResponce():

    def responce_status_chek(self, status_code, expected_status):
        with allure.step(f'Статус ответа: {status_code}'):
            assert status_code == expected_status, f'Статус ответа {status_code}'


    def responce_schema_validate(self, response_json, schema):
        with allure.step('Валидация схемы ответа'):
            validate(instance=response_json, schema=schema)

    def responce_json_get(self, responce_content):
        response_json = ''
        try:
            response_json = responce_content.json()
        except json.JSONDecodeError:
            print('Ответ не в json формате или пустой')
        return response_json


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method = method, url = self.base_url + url, *args, **kwargs)
        status = response.status_code
        curl = to_curl(response.request)
        date_time = datetime.now()

        logging.info(date_time)
        logging.info(f'Код ответа: {status}')
        logging.info(curl)

        with allure.step(f'{method} {url}'):
            allure.attach(body=f'Время запроса: {date_time}. Код ответа: {status} {curl}. Переданы параметры *args, **kwargs: {args} {kwargs}',
                          name='info',
                          attachment_type=AttachmentType.TEXT,
                          extension='txt')
            try:
                allure.attach(body=json.dumps(response.json(), ensure_ascii=False, indent=2),
                              name='response json',
                              attachment_type=AttachmentType.JSON,
                              extension='json')
            except json.JSONDecodeError:
                allure.attach(body=response.text,
                              name='response text',
                              attachment_type=AttachmentType.TEXT,
                              extension='txt')

            return response

reqres_session = CustomSession('https://reqres.in/')
reqres_responce = ReqresResponce()

