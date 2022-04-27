from loader import db, cursor
from data.config import a_id


def sql_start():
    if db:
        print('Database connected')

        cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_number BIGINT(50),
        job_name VARCHAR(255),
        job_description VARCHAR(255),
        status VARCHAR(255),
        client_id INT,
        order_date DATE
        )""")
        db.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id BIGINT(50) NOT NULL UNIQUE,
        f_name VARCHAR(255),
        l_name VARCHAR(255),
        user_status tinyint(4),
        date DATE,
        admin_status tinyint(4)
        )""")
        db.commit()

        cursor.execute(f"SELECT * FROM users WHERE user_id = {a_id}")
        if cursor.fetchone() is None:
            sql_user_reg = "INSERT INTO users (user_id, f_name, l_name, admin_status) VALUES (%s, %s, %s, %s)"
            val_user_reg = (a_id, 'B', 'K', '1',)
            cursor.execute(sql_user_reg, val_user_reg)
            db.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS mikrotik(
                id BIGINT(50) AUTO_INCREMENT PRIMARY KEY,
                model VARCHAR(255),
                description VARCHAR(255),
                qty BIGINT(50),
                price BIGINT(50)
                )""")
        db.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS ubiquiti(
                        id BIGINT(50) AUTO_INCREMENT PRIMARY KEY,
                        model VARCHAR(255),
                        description VARCHAR(255),
                        qty BIGINT(50),
                        price BIGINT(50)
                        )""")
        db.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS linksys(
                                id BIGINT(50) AUTO_INCREMENT PRIMARY KEY,
                                model VARCHAR(255),
                                description VARCHAR(255),
                                qty BIGINT(50),
                                price BIGINT(50)
                                )""")
        db.commit()
