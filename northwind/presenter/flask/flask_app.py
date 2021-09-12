import sys
import os
import logging
import connexion
from waitress import serve
from flask_cors import CORS
from northwind.adapter.configuration import application

log=logging.getLogger(__name__)

def run():
    cwd = os.getcwd()
    log.info('Starting Product Details Data Service...')
    app_config=application.get_app_config()
    try:
        api_server=connexion.FlaskApp(__name__,specification_dir=app_config['api']['specdir'])
        api_server.add_api(app_config['api']['spec'])  
        CORS(api_server.app)
        serve(api_server,host='0.0.0.0',port=app_config['host']['port'])
    except Exception as ex:
        log.error(ex.args[0])
        sys.exit(-1)