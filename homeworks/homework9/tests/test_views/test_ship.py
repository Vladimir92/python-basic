from pytest import fixture
from collections import OrderedDict
from homework9.app import app

from homework9.views.product import read_csv_ships


@fixture
def client():
    with app.test_client() as client:
        yield client


def test_read_ships():
    res = read_csv_ships()
    assert isinstance(res, list)
    assert isinstance(res.pop(), OrderedDict)


def test_recover_products(client):
    resp = client.get("/ships/")
    assert resp.status_code == 200
    del_req = client.delete("/ships/1/")
    data = del_req.json
    assert data == {"ok": True}