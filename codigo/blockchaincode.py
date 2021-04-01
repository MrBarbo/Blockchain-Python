import json
from datetime import datetime


class Block:
    def __init__(self, email, motiv, arch):
        self.email = email
        self.motive = motiv 
        self.archivo = arch
        self.timestamp = datetime.now()


