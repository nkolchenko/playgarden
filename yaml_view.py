#!/usr/bin/python3

import yaml

if __name__ == '__main__':

    stream = open("yaml_cheat_sheet.yaml", 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)  # https://msg.pyyaml.org/load 
    for key, value in dictionary.items():
        print(key + " : " + str(value))
