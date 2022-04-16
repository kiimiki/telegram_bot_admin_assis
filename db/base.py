from loader import db, cursor


def sql_start():
    if db:
        print('Database connected')

        cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_number INT,
        job_name VARCHAR(255),
        job_description VARCHAR(255),
        status VARCHAR(255),
        client_id INT,
        order_date DATE
        )""")
        db.commit()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL UNIQUE,
        f_name VARCHAR(255),
        l_name VARCHAR(255),
        user_status tinyint(4),
        date DATE,
        admin_status tinyint(4)
        )""")
        db.commit()
