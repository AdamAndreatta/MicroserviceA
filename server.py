import zmq
import json
import time

context = zmq.Context()
rep_socket = context.socket(zmq.REP)
rep_socket.bind('tcp://*:5555')

print("your conversion is being processed")
message = rep_socket.recv_string()
data = json.loads(message)
vals = list(data.values())

key = vals[0]
conversion = vals[1]

f = open("inventory.json")
items = json.load(f)
f.close()
amount = items[key][0]
current_measure = items[key][1]

#metric conversions can be added to ass need converts the value then edits the json object
if current_measure == "kg" and conversion == "g":
    amount = amount * 1000
    items[key][0] = amount
    items[key][1] = "g"

elif current_measure == "L" and conversion == "ml":
    amount = amount * 1000
    items[key][0] = amount
    items[key][1] = "ml"

elif current_measure == "ml" and conversion == "L":
    amount = amount * .001
    items[key][0] = amount
    items[key][1] = "L"

elif current_measure == "g" and conversion == "kg":
    amount = amount * .001
    items[key][0] = amount
    items[key][1] = "kg"

elif current_measure == "g" and conversion == "mg":
    amount = amount * 1000
    items[key][0] = amount
    items[key][1] = "mg"

elif current_measure == "mg" and conversion == "g":
    amount = amount * .001
    items[key][0] = amount
    items[key][1] = "g"

#writes the values within the json object to the file updating with the new values of the conversion and what it was converted to
with open("inventory.json", "w") as inventory:
    json.dump(items, inventory)

rep_socket.send_string("conversion complete")




