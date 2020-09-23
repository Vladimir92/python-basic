from gino import Gino

db = Gino()


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    catchPhrase = db.Column(db.String(), nullable=False)
    bs = db.Column(db.String(), nullable=False)


class Geo(db.Model):
    __tablename__ = 'geo'
    id = db.Column(db.Integer(), primary_key=True)
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer(), primary_key=True)
    street = db.Column(db.String(), nullable=False)
    suite = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    zipcode = db.Column(db.String(), nullable=False)
    geo_id = db.Column(db.Integer, db.ForeignKey('geo.id'))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    website = db.Column(db.String(), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))

    def __str__(self):
        values = [f"{n}={getattr(self, n)}" for n in ("id", "name", "username", "email", "phone", "website")]
        extra = [f"{val}={getattr(self, val)}" for val in ("address_id", "company_id")]
        return f"{self.__class__.__name__}({','.join(values)})({','.join(extra)})"