# -*- encoding: utf-8 -*-
# Author: li_colin

import yaml
from loguru import logger
from typing import Dict, Text
from base_exceptions import *


def _load_yaml_file(yaml_file: Text) -> Dict:
    """load yaml file and check file content format"""
    with open(yaml_file, mode="rb") as stream:
        try:
            yaml_content = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as ex:
            err_msg = f"YAMLError:\nfile: {yaml_file}\nerror: {ex}"
            logger.error(err_msg)
            raise FileFormatError

        return yaml_content
