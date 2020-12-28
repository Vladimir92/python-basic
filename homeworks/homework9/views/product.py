import csv
import pathlib
from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

product_app = Blueprint("product_app", __name__)

fieldnames = [
    "id", "name", "mass", "speed", "jump", "img_id"
]
filename = "views/ships.csv"


def read_csv_ships():
    SHIPS = []
    path = pathlib.Path(filename).resolve()
    with open(path) as f:
        csv_reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in csv_reader:
            SHIPS.append(row)
        print(SHIPS)
    return SHIPS


SHIP_LIST = read_csv_ships()


@product_app.route("/")
def ship_list():
    return render_template("ships/index.html", items=SHIP_LIST)


@product_app.route("/<string:identifier>/", methods=['GET', 'DELETE'])
def ship_detail(identifier: str):
    product = None
    num = 0
    for ship in SHIP_LIST:
        if ship["id"] == identifier:
            product = ship
            break
        num += 1
    if product is None:
        raise BadRequest("No such ship")

    if request.method == 'DELETE':
        SHIP_LIST.pop(num)
        return jsonify(ok=True)

    return render_template(
        "ships/detail.html",
        ship=SHIP_LIST[num],
    )
