import os
from dotenv import load_dotenv


load_dotenv()
token = str(os.getenv("token"))
a_id = str(os.getenv("a_id"))

admins_id = [
    f'{a_id}'
]

mysql_user = str(os.getenv("mysql_u"))
mysql_password = str(os.getenv("mysql_p"))
mysql_db = str(os.getenv('db'))
