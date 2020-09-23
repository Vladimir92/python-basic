import configparser
import os

from aiohttp import ClientSession
from loguru import logger
import asyncio
from homeworks.homework3.models import *

USER_URL = "https://jsonplaceholder.typicode.com/users"


async def save_geo(geo_data: dict):
    geo = await Geo.create(lat=float(geo_data["lat"]), lng=float(geo_data["lng"]))
    logger.info(f"Geo object created in DB: {geo}")
    return geo


async def save_company(comp_data: dict):
    company = await Company.create(name=comp_data["name"], catchPhrase=comp_data["catchPhrase"], bs=comp_data["bs"])
    logger.info(f"Company object created in DB: {company}")
    return company


async def save_address(address_data: dict):
    geo = await save_geo(address_data["geo"])
    address = await Address.create(
        street=address_data["street"],
        suite=address_data["suite"],
        city=address_data["city"], 
        zipcode=address_data["zipcode"],
        geo_id=geo.id
    )
    logger.info(f"Address object created in DB: {address}")
    return address


async def save_user(user_data: dict):
    company = await save_company(user_data["company"])
    address = await save_address(user_data["address"])
    user = await User.create(
       name=user_data["name"],
       username=user_data["username"],
       email=user_data["email"],
       phone=user_data["phone"],
       website=user_data["website"],
       address_id=address.id,
       company_id=company.id
    )
    logger.info(f"User object created in DB: {user}")


async def fetch(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_user() -> dict:
    async with ClientSession() as session:
        result = await fetch(session, USER_URL)
        logger.info(f"Users dict returned: {result}")
        for user in result:
            await save_user(user)

        await session.close()
        return result


def parse_conf(filename: str):
    config = configparser.ConfigParser()
    config.read(filename)
    psql = config['postgresql']
    for key in psql:
        if key == 'user' or key == 'host' or key == 'database':
            if not psql[key]:
                raise ValueError("Config file must contain values for keys: user, host, database")
    if 'user' not in list(psql) or 'host' not in list(psql) or 'database' not in list(psql):
        raise ValueError("Config file must contain keys: user, host, database")
    return psql


async def main_proc():
    psql = parse_conf("config.ini")
    psw = os.environ.get("PG_PASS")

    conn_str = f"postgresql://{psql['user']}:{psw}@{psql['host']}:{psql.get('port', '5432')}/{psql['database']}"
    async with db.with_bind(conn_str):
        await db.gino.create_all()

        await fetch_user()
        users = await db.all(User.query)
        users_count = await db.func.count(User.id).gino.scalar()
        logger.info(f"{users_count} Users stored in DB: {users}")

    # await db.pop_bind().close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_proc())
