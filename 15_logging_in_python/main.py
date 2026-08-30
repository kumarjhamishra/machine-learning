import logging

import database
import auth

logging.basicConfig(
    filename='application.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

database.fetch_data()
auth.login()