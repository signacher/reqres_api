import allure
import pytest
from model.utils.helper import reqres_session, reqres_responce


@allure.label('owner', 'Telnov')
@allure.epic('Delete')
@allure.feature('Delete user')
@allure.story('Delete user success')
def test_user_delete_success():
    user_id = 2
    response = reqres_session.delete(f'api/users/{user_id}')

    status = response.status_code
    response_json = reqres_responce.responce_json_get(response)

    reqres_responce.responce_status_chek(status, 204)

    with allure.step('Ответ пустой'):
        assert response_json == ''