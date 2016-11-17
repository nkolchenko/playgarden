#!/usr/bin/python
import sys
import json

# 10494
def updateJsonFile():
    jsonFile = open('./10494.json', "r")
    data = json.load(jsonFile)  # it's a dictionaly that contains a list of settings per line_item somewhere inside
    jsonFile.close()

    line_item_params = data["line_items"]  # it's a comma separated list of all the line items with their settings
#    targetings = line_items_params[0]

    for line_item in line_item_params:
#        print line_item
        li_settings = line_item["targeting"]

        my_check = li_settings.get('inventory_type', "empty")  # checks is inventory_type exists
        if my_check == "empty":
            # here we should ADD missed targeting
            #print str("There is no such targenting for LI") # here we should ADD missed targeting
            li_settings['inventory_type']=[u"mobile_app"]
 #           print li_settings['inventory_type']
        else:
            # here we need to replace any content with mobile_app
            li_settings['inventory_type'] = [u"mobile_app"]
 #           print li_settings['inventory_type']


    jsonFile = open("./test10494.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

if __name__ == '__main__':
    sys.exit(updateJsonFile())
