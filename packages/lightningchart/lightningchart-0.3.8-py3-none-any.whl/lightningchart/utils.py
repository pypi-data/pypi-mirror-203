from __future__ import annotations
import requests
import csv
import json
import random
import openpyxl
import xml.etree.ElementTree as ET

from .globals import *


def read_csv(csv_input: str,
             delimiter: str,
             fields_to_include: list[str],
             new_keys: list[str] = None,
             field_types_row: bool = False
             ) -> list[dict[str, int | float]]:
    """UNDER DEVELOPMENT, MAY NOT WORK!
    Read data from a CSV file.

    Args:
        csv_input (str): Either a path to the CSV file or the CSV content in a string.
        delimiter (str): The delimiter of the CSV data, typically either "," or ";".
        fields_to_include (list[str]): The fields of the CSV data that you want to use, e.g. ['a','b']
        new_keys (list of str): Assign new names for the fields_to_include you have chosen, e.g. ['x','y']
        field_types_row (bool): Whether the CSV data contains field types in the second row. If true,
            the second row will be interpreted as types instead of data to be used.

    Returns:
        Python list of dictionaries containing included fields formatted as new keys.
    """

    def parse(reader_):
        headers = next(reader_)
        types = next(reader_) if field_types_row is True else None
        indexes = [headers.index(field) for field in fields_to_include]
        result = []
        for row in reader_:
            dict_item = {}
            for i, index in enumerate(indexes):
                field_type = types[i] if types is not None and i < len(types) else None
                if index < len(row):
                    value = row[index]
                    if str(field_type).lower().startswith('int'):
                        value = int(value)
                    elif str(field_type).lower().startswith('float') or str(field_type).lower().startswith('double'):
                        if ',' in value and '.' not in value:
                            value = value.replace(',', '.')
                        value = float(value)
                    key = new_keys[i] if new_keys is not None and i < len(new_keys) else fields_to_include[i]
                    dict_item[key] = value
            result.append(dict_item)
        return result

    if csv_input.endswith('.csv'):
        with open(csv_input, 'r') as f:
            reader = csv.reader(f, delimiter=delimiter)
            return parse(reader)
    else:
        reader = csv.reader(csv_input.splitlines(), delimiter=delimiter)
        return parse(reader)


def read_json(json_input: str,
              fields_to_include: list[str],
              new_keys: list[str] = None,
              json_key: str = None
              ) -> list[dict[str, int | float]]:
    """UNDER DEVELOPMENT, MAY NOT WORK!
    Read data from a JSON file.

    Args:
        json_input (str): Either a path to the JSON file or the JSON content in a string.
        fields_to_include (list[str]): The fields of the JSON objects that you want to use, e.g. ['a','b']
        new_keys (list[str]): Assign new names for the fields_to_include you have chosen, e.g. ['x','y']
        json_key (str): The key of the JSON object to read

    Returns:
        Python list of dictionaries containing included fields formatted as new keys.
    """
    if json_input.endswith('.json'):
        with open(json_input, 'r') as f:
            data = json.load(f)
    else:
        data = json.loads(json_input)

    if json_key:
        data = data[json_key]
        if data is None:
            raise Exception(f'No "{json_key}" found in the JSON data.')

    result = []
    for item in data:
        dict_item = {}
        for i, field in enumerate(fields_to_include):
            if field in item:
                key = field
                if new_keys and len(new_keys) > i:
                    key = new_keys[i]
                dict_item[key] = item[field]
        result.append(dict_item)
    return result


def read_xml(xml_input: str,
             fields_to_include: list[str],
             new_keys: list[str] = None,
             node_name: str = None
             ) -> list[dict[str, int | float]]:
    """UNDER DEVELOPMENT, MAY NOT WORK!
    Read data from an XML file.

    Args:
        xml_input (str): Either a path to the XML file or the XML content in a string.
        fields_to_include (list[str]): The fields of the XML nodes that you want to use, e.g. ['a','b']
        new_keys (list[str]): Assign new names for the fields_to_include you have chosen, e.g. ['x','y']
        node_name (str): The name of the XML node to extract data from

    Returns:
        Python list of dictionaries containing included fields formatted as new keys.
    """
    if xml_input.endswith('.xml'):
        tree = ET.parse(xml_input)
        root = tree.getroot()
    else:
        root = ET.fromstring(xml_input)

    if node_name is not None:
        root = root.find(node_name)
        if root is None:
            raise Exception(f'No "{node_name}" found in the XML data.')

    result = []
    for item in root:
        dict_item = {}
        for i, field in enumerate(fields_to_include):
            if item.find(field) is not None:
                key = field
                if new_keys and len(new_keys) > i:
                    key = new_keys[i]
                value = item.find(field).text
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                dict_item[key] = value
        result.append(dict_item)
    return result


def read_xlsx(xlsx_file: str,
              sheet_name: str,
              fields_to_include: list[str],
              new_keys: list[str] = None
              ) -> list[dict[str, int | float]]:
    """UNDER DEVELOPMENT, MAY NOT WORK!
    Read data from a XLSX file, i.e., an Excel sheet.

    Args:
        xlsx_file (str): The path to the XLSX file.
        sheet_name (str): The name of the Excel sheet, e.g. "Sheet1".
        fields_to_include (list[str]): The fields of the JSON objects that you want to use, e.g. ['a','b']
        new_keys (list[str]): Assign new names for the fields_to_include you have chosen, e.g. ['x','y']

    Returns:
        Python list of dictionaries containing included fields formatted as new keys.
    """
    workbook = openpyxl.load_workbook(xlsx_file)
    sheet = workbook[sheet_name]
    header = [cell.value for cell in sheet[1]]
    result = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        dict_item = {}
        for i, field in enumerate(fields_to_include):
            if field in header:
                key = field
                if new_keys and len(new_keys) > i:
                    key = new_keys[i]
                value = row[header.index(field)]
                dict_item[key] = value
        result.append(dict_item)
    return result


def generate_random_xy_data(amount: int = 100,
                            min_value: int | float = 0,
                            max_value: int | float = 10
                            ) -> list[dict[str, int | float]]:
    """Generate n amount of random XY datapoints in a specific value range.

    Args:
        amount (int): The size of the generated dataset.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.

    Returns:
        List of dictionaries containing x and y values.
    """
    data = []
    for i in range(amount):
        data.append({
            'x': random.uniform(min_value, max_value),
            'y': random.uniform(min_value, max_value),
        })
    return data


def generate_random_xyz_data(amount: int = 100,
                             min_value: int | float = 0,
                             max_value: int | float = 10
                             ) -> list[dict[str, int | float]]:
    """Generate n amount of random XYZ datapoints in a specific value range.

        Args:
            amount (int): The size of the generated dataset.
            min_value (int | float): Minimum value of any given datapoint.
            max_value (int | float): Maximum value of any given datapoint.

        Returns:
            List of dictionaries containing x, y, and z values.
    """
    data = []
    for i in range(amount):
        data.append({
            'x': random.uniform(min_value, max_value),
            'y': random.uniform(min_value, max_value),
            'z': random.uniform(min_value, max_value),
        })
    return data


def generate_progressive_xy_data(amount: int = 100,
                                 min_value: int | float = 0,
                                 max_value: int | float = 10,
                                 progressive_axis: str = 'x'
                                 ) -> list[dict[str, int | float]]:
    """Generate n amount of XY datapoints that are progressive with respect to one axis.

    Args:
        amount (int): The size of the generated dataset.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.
        progressive_axis (str): "x" or "y"

    Returns:
        List of dictionaries containing x and y values.
    """
    data = []
    if progressive_axis == 'x':
        for i in range(amount):
            data.append({
                'x': i,
                'y': random.uniform(min_value, max_value),
                'z': random.uniform(min_value, max_value),
            })
    elif progressive_axis == 'y':
        for i in range(amount):
            data.append({
                'x': random.uniform(min_value, max_value),
                'y': i,
                'z': random.uniform(min_value, max_value),
            })
    return data


def generate_progressive_xyz_data(amount: int = 100,
                                  min_value: int | float = 0,
                                  max_value: int | float = 10,
                                  progressive_axis: str = 'x'
                                  ) -> list[dict[str, int | float]]:
    """Generate n amount of XYZ datapoints that are progressive with respect to one axis.

    Args:
        amount (int): The size of the generated dataset.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.
        progressive_axis (str): "x", "y", or "z"

    Returns:
        List of dictionaries containing x, y, and z values.
    """
    data = []
    if progressive_axis == 'x':
        for i in range(amount):
            data.append({
                'x': i,
                'y': random.uniform(min_value, max_value),
                'z': random.uniform(min_value, max_value),
            })
    elif progressive_axis == 'y':
        for i in range(amount):
            data.append({
                'x': random.uniform(min_value, max_value),
                'y': i,
                'z': random.uniform(min_value, max_value),
            })
    elif progressive_axis == 'z':
        for i in range(amount):
            data.append({
                'x': random.uniform(min_value, max_value),
                'y': random.uniform(min_value, max_value),
                'z': i,
            })
    return data


def generate_random_matrix_data(columns: int,
                                rows: int,
                                min_value: int | float = 0,
                                max_value: int | float = 10
                                ) -> list[list[int | float]]:
    """Generate a (2D) matrix dataset with random values between a specific range.

    Args:
        columns (int): The amount of columns in the matrix.
        rows (int): The amount of rows in the matrix.
        min_value (int | float): Minimum value of any given point in the matrix.
        max_value (int | float): Maximum value of any given point in the matrix.

    Returns:
        List of lists containing values.
    """
    data = [
        [random.uniform(min_value, max_value) for j in range(columns)]
        for i in range(rows)
    ]
    return data
