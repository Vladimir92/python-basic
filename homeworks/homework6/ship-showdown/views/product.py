import csv
import pathlib
from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

from models import db, Ship

product_app = Blueprint("product_app", __name__)


@product_app.route("/")
def ship_list():
    ships = Ship.query.filter_by(deleted=False).order_by(Ship.id).all()
    return render_template("ships/index.html", items=ships)


@product_app.route("/add", methods=['POST', 'GET'])
def add_ship():
    msg=''
    # Insert ship into DB
    if request.method == 'POST':
        try: 
            name = request.form.get('name')
            mass = int(request.form.get('mass'))
            speed = int(request.form.get('speed'))
            jump = int(request.form.get('jump'))
            img_id = int(request.form.get('img_id'))
            s = Ship(name=name, mass=mass, speed=speed, jump=jump, img_id=img_id)
            db.session.add(s)
            db.session.commit()
            msg = "Ship successfully inserted"
        except ValueError as ex:
            msg = ex.__str__
    return render_template("ships/add.html", message=msg)


@product_app.route("/<int:identifier>/", methods=['GET', 'DELETE'])
def ship_detail(identifier: int):
    ship = Ship.query.filter_by(id=identifier).one_or_none()
    if ship is None:
        raise BadRequest("No such ship")

    if request.method == 'DELETE':
        ship.deleted = True
        db.session.commit()
        return jsonify(ok=True)

    return render_template(
        "ships/detail.html",
        ship=ship,
    )
