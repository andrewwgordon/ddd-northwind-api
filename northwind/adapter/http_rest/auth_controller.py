import connexion
from typing import Dict
import logging

log=logging.getLogger(__name__)

def basic(username: str,password: str,required_scopes=None) -> Dict:
    return {'identitytype':'user','identity':username}