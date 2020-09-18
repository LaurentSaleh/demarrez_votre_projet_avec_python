# -*- coding: utf8 -*-

import json

def read_values_from_json():
    # Create a new empty list
    values = []# open a json file with my objects
    with open("charac_slh.json")as f:
        # load all the data contained in this file data = entries
        for entry in data:
            values.append(entry["character"])
    return values
    # return my completed list
