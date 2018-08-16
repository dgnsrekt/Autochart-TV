import socket
from contextlib import closing

class ValidationError(Exception):
    pass


def validate(kwarg, validator, validator_string):
    try:
        if isinstance(validator, dict):
            validator = list(validator.keys())
        assert kwarg in validator
    except AssertionError:
        raise ValidationError(
            f'{kwarg} is an invalid {validator_string} keyword. Use the following. {validator}')


#TODO IDEA: FUTURE FEATURE to run multiple instances.
#Will add a port section to model, client, and server.
#IDEA: ability to change port within a single client.
def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is in use.")
        else:
            print("Port is available.")
