import requests
import json
import logging
from datetime import datetime

logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level  = logging.INFO, # Nivel de los eventos que se registran en el logger
)
class sendNewRelic():
    def __init__(self, url, license_key, app_name, app_id):
        """
        Metodo constuctor que recibe:
            url: para el envio de logs (verificar la documentacion de new relic),
            license_key: de proyecto new relic
            app_name: nombre de la aplicacion
            app_id: id de la aplicacion
        Args:
            url: string
            license_key: string
            app_name: string
            app_id: string
        """
        self.url = url
        self.app_name = app_name
        self.app_id = app_id
        self.headers = {'Content-Type': "application/json", 'X-License-Key': license_key}

    def send_message(self, message, logtype, print_log=True):
        """
        Funcion que se encarga de enviar mensajes a new relic, recibe:
            message: mensaje a enviar a new relic
            logtype: puede ser info, error, etc para poder diferenciar de que tipo son los mensajes
            print_log: para saber si muestro los mensajes de logs o no
        Args:
            message: string requerido
            logtype: string requerido
            print_log: boolean opcional

        Returns:

        """
        data = {"appId": self.app_id, "message": message, "logtype": logtype, "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "labels": { "app": self.app_name } }
        response = requests.post(self.url, data = json.dumps(data), headers = self.headers )
        if print_log:
            logging.info('Send message to new relic: {}'.format(response))