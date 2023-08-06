from __future__ import annotations
import requests
import socket

from .globals import *
from .utils import *
from .server import start_thread
from .instance import Instance
from .charts import ChartXY, Chart3D, Dashboard, \
    PieChart, GaugeChart, PyramidChart, FunnelChart, LineChart, ScatterPlot


def init():
    pass


def port_is_in_use(port: int) -> bool:
    """INTERNAL FUNCTION, NOT INTENDED FOR END-USER USE.

    Checks if the specified port is being used by another application.

    Args:
        port (int): The port number to check.

    Returns:
        (bool): True, if port is in use.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def server_is_running(port: int) -> bool:
    """INTERNAL FUNCTION, NOT INTENDED FOR END-USER USE.

    Checks if the local server is running on the specified port.

    Args:
        port (int): The port number to check.

    Returns:
        (bool): True, if server is running on the port.
    """
    try:
        response = requests.get(f'{LOCALHOST}{port}/test_connection')
        if response.status_code == 222:
            return True
        else:
            return False
    except:
        return False


if not server_is_running(server_port):
    try:
        server_thread = start_thread(server_port)
    except:
        while True:
            server_port += 1
            if server_is_running(server_port):
                break
            if not port_is_in_use(server_port):
                server_thread = start_thread(server_port)
                break
