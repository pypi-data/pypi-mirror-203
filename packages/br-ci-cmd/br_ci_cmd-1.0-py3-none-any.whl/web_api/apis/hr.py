from config import Conf

from ..schemas import hr as hrSchema
from .client import Client

cClient = Client(baseUrl=Conf.hrServer.baseUrl)

Headers = Conf.hrServer.headers


def user_info(userCard: str):
    url = "/External/GetLineManagerInfoList"
    body = hrSchema.GetLineManagerInfoList(EmployeeNo=[userCard])
    resp = cClient.post(url, headers=Headers, json=body.dict())
    data = resp.json()
    if "code" in data and data["StatusCode"] == 200:
        if data["Data"]:
            return data["Data"][0]
        else:
            return {}
    else:
        raise ValueError("http respone err")
