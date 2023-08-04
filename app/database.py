import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tg_id INTEGER,"
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "description TEXT,"
                "price TEXT,"
                "photo TEXT,"
                "brand TEXT)")
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM  accounts WHERE tg_id == {kay}".format(kay=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()

async def add_item(state):
    async with state.proxy() as data:
        cur.execute("INSERT INTO items (name, description, price, photo , brand) VALUES (?,?,?,?,?)",
                    (data['name'], data['description'], data['price'], data['photo'], data['type']))
        db.commit()