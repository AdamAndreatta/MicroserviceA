import zmq
import subprocess
import time
import sys
import json

# You can use this to help test your microservice.
# This function will be called to pass arguments to your microservice.
def connect_to_conversion(ingredient: str, convert_to: str) -> str:
    subprocess.Popen([sys.executable, 'server.py'])
    # The above will auto open your program when called. Make sure to replace the name.
    time.sleep(1)

    # The below sets up the requester socket after the rep socket in your microprogram is setup.
    recipe_context = zmq.Context()
    recipe_req = recipe_context.socket(zmq.REQ)
    recipe_req.connect('tcp://localhost:5555')

    val1 = ingredient
    val2 = convert_to

    dict = {"ingredient": val1, "Convert to": val2}
    message = json.dumps(dict)

    # The below sends the above dictionary to your microservice.
    recipe_req.send_string(message)
    time.sleep(10)
    # For zeromq your microservice HAS to send a message back. Just send back a string that says success.
    response = recipe_req.recv_string()
    print(response)
    recipe_req.close()
    recipe_context.term()

connect_to_conversion("Flour","lbs")
