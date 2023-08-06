from __future__ import annotations

import sys
import time
import math
import uuid
import json
import msgpack
import requests
import webbrowser
from IPython.lib.display import IFrame
from IPython import get_ipython

from .globals import *
from .charts import ChartXY, Chart3D, Dashboard, PieChart, GaugeChart, FunnelChart, PyramidChart


class Instance:

    def __init__(self, instance_id: str = None):
        """Legacy feature"""
        if not instance_id:
            instance_id = uuid.uuid4()
        self.id = str(instance_id)

    def set_id(self, instance_id: str) -> Instance:
        """Legacy feature"""
        self.id = instance_id
        return self

    def clear(self) -> Instance:
        """Legacy feature"""
        binary_data = json.dumps({
            'id': str(self.id),
            'command': 'clearInstance',
            'param': {}
        }).encode('utf-8')

        start_time = time.time()
        while (time.time() - start_time) < 10:
            try:
                response = requests.post(f'{LOCALHOST}{server_port}/clear?id={self.id}', data=binary_data)
                if response.ok:
                    return self
            except requests.exceptions.ConnectionError as e:
                print(e)

    def open(self, method: str = None, width: int = 800, height: int = 600):
        """Open the rendering view, either in a new browser tab or an IFrame component for Jupyter Notebook.

        Args:
            method (str): "browser" | "notebook", default value depends on your runtime environment.
            width (int): The width of the IFrame component in pixels.
            height (int): The height of the IFrame component in pixels.

        Returns:
            Either opens a new tab on your browser or returns an IFrame component for Jupyter Notebook.
        """
        if str(method).lower() == 'browser':
            return self.open_in_browser()
        elif get_ipython().__class__.__name__ == 'ZMQInteractiveShell' or 'notebook' in str(method).lower():
            return self.open_in_notebook(width, height)
        else:
            return self.open_in_browser()

    show = open

    def open_in_browser(self) -> Instance:
        """Open the rendering view in a new browser tab.

        Returns:
            Reference to self.
        """
        webbrowser.open(f'{LOCALHOST}{server_port}/?id={self.id}')
        start_time = time.time()
        while (time.time() - start_time) < 10:
            try:
                response = requests.get(f'{LOCALHOST}{server_port}/room_response?id={self.id}')
                if response.ok:
                    return self
            except requests.exceptions.ConnectionError as e:
                print(e)
        raise Exception('Client did not connect within 10 seconds, please try again')

    def open_in_notebook(self, width: int = 800, height: int = 600) -> IFrame:
        """Open the rendering view in an IFrame component.

        Args:
            width (int): The width of the IFrame component in pixels.
            height (int): The height of the IFrame component in pixels.

        Returns:
            An IFrame component containing the current render view.
        """
        return IFrame(src=f'{LOCALHOST}{server_port}/?id={self.id}', width=width, height=height)

    def send_command(self, id: str, command: str, parameters: dict = {}):
        """INTERNAL FUNCTION, DO NOT USE!"""
        payload = {
            'id': str(id),
            'command': command,
            'param': parameters
        }
        binary_data = msgpack.packb(payload)

        start_time = time.time()
        while (time.time() - start_time) < 10:
            try:
                response = requests.post(
                    f'{LOCALHOST}{server_port}/item?id={self.id}',
                    data=binary_data,
                    headers={'Content-Type': 'application/msgpack'}
                )
                if response.ok:
                    return True
            except requests.exceptions.ConnectionError as e:
                print(e)

    def send_data(
            self,
            id: str,
            data: dict[str, int | float] | list[dict[str, int | float]],
            clear_previous: bool
    ):
        """INTERNAL FUNCTION, DO NOT USE!"""
        payload = {
            'id': str(id),
            'command': 'addData',
            'param': {'data': data, 'clear': int(clear_previous)}
        }
        binary_data = msgpack.packb(payload)

        start_time = time.time()
        while (time.time() - start_time) < 10:
            try:
                response = requests.post(
                    f'{LOCALHOST}{server_port}/item?id={self.id}',
                    data=binary_data,
                    headers={'Content-Type': 'application/msgpack'}
                )
                if response.ok:
                    return True
            except requests.exceptions.ConnectionError as e:
                print(e)
