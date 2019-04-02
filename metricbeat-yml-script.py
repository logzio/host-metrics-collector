import logging
import os
from ruamel.yaml import YAML
import socket

# set vars and consts

logzio_url = os.environ["LOGZIO_URL"]
logzio_url_arr = logzio_url.split(":")
logzio_token = os.environ["LOGZIO_TOKEN"]

HOST = logzio_url_arr[0]
PORT = int(logzio_url_arr[1])
SOCKET_TIMEOUT = 3
METRICBEAT_CONF_PATH = "/etc/metricbeat/metricbeat.yml"

logging.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s', level=logging.DEBUG)


def _is_open():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(SOCKET_TIMEOUT)

    result = sock.connect_ex((HOST, PORT))
    if result == 0:
        logging.info("Connection Established")
    else:
        logging.error("Can't connect to the listener, "
                      "please remove any firewall settings to host:{} port:{}".format(HOST, str(PORT)))
        raise ConnectionError


def _add_shipping_data():
    yaml = YAML()
    with open("default_metricbeat.yml") as default_metricbeat_yml:
        config_dic = yaml.load(default_metricbeat_yml)

    config_dic["output.logstash"]["hosts"].append(logzio_url)
    config_dic["fields"]["token"] = logzio_token

    with open(METRICBEAT_CONF_PATH, "w+") as metricbeat_yml:
        yaml.dump(config_dic, metricbeat_yml)


_is_open()
_add_shipping_data()

os.system("metricbeat -e")
