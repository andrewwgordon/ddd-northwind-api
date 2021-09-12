import sys
import logging
import logging.config
import configparser
from datetime import datetime
from northwind.adapter.repository.sqlite_datastore_context import SQLiteDatastoreContext
from northwind.adapter.repository.sqlite_product_detail_repository import SQLiteProductDetailRepository
from northwind.service.service_manager import ServiceManager

try:
    logging.config.fileConfig('./northwind/resources/logging.conf',disable_existing_loggers=False)
except Exception as ex:
    sys.stderr.write(str(datetime.now())+' - __main__ - FATAL - Error loading logging.conf...\n')
    sys.exit(-1)

log=logging.getLogger(__name__)

app_config=configparser.RawConfigParser()
try:
    app_config.read('./northwind/resources/northwind.properties')
except Exception as ex:
    log.fatal(ex.args[0])
    sys.exit(-1)

datastore_context = SQLiteDatastoreContext(app_config)
product_detail_repository = SQLiteProductDetailRepository(datastore_context)
service_manager = ServiceManager(product_detail_repository)

def get_app_config():
    return app_config

def get_product_detail_repository():
    return product_detail_repository

def get_service_manager():
    return service_manager