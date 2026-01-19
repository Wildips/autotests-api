from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class PublicUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание УЗ.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users не авторизованным пользователем.
    """

    def create_user_api(self, request: PublicUserRequestDict) -> Response:
        """
        Метод создает УЗ.

        :param request: Словарь с email, password, lastName, firstName и middleName создаваемо УЗ.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
