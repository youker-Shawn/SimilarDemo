# -*- coding: utf-8 -*-
'''
@Time    :   2022-11-23 23:31:08
@File    :   utils.py
@author  :   youker-Shawn
@Desc    :   demo views.py 用到工具函数

'''

import logging
from typing import Tuple, Optional
from geopy import distance


def distance_between_2_locations(
    first_location: Tuple[float], second_location: Tuple[float]
) -> Optional[float]:
    try:
        dist = distance.distance(first_location, second_location)
    except Exception as e:
        logging.warning(f"Locations: {first_location} {second_location} .Error: {e}")
        return None
    else:
        return dist.km
