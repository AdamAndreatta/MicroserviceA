#Kitchen Converter

recipe_context = zmq.Context() #set up environment
recipe_req = recipe_context.socket(zmq.REQ) #create socket for making requests
recipe_req.connect('tcp://localhost:5555')  #connect to the port where the service is listening for your request

#Turn values taken from function parameter turn them into values to be passed
val1 = ingredient
val2 = convert_to

#Store values in a dictionary which will be dumped to a json string which will be sent to the service. Indicates to the service which values will be changed and how they will be changed.

dict = {"ingredient": val1, "Convert to": val2}
message = json.dumps(dict)

#Message is recived by the service and the string will be converted back into a python object to obtain the values needing to be changed

message = rep_socket.recv_string()
data = json.loads(message)
vals = list(data.values())

#Values are stored to variables for function use

key = vals[0]
conversion = vals[1]

#Load json dictionary so that converted values can be stored to the json and then passed back to client program.

f = open("inventory.json")
items = json.load(f)
f.close()
amount = items[key][0]
current_measure = items[key][1]

#Sends message of process completion

rep_socket.send_string("conversion complete")

#Service exits after completion 

recipe_req.close()
recipe_context.term()

UML Diagram
![UML](https://github.com/user-attachments/assets/57b6abb7-b2a1-4abe-913a-288e07873b08)
