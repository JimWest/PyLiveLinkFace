import socket
import time
import random

from pylivelinkface import PyLiveLinkFace, FaceBlendShape

UDP_IP = "127.0.0.1"
UDP_PORT = 11111

py_face = PyLiveLinkFace()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.connect((UDP_IP, UDP_PORT))
    while True: 

        # set the head rotation to random values             
        py_face.set_value(FaceBlendShape.HeadPitch, random.uniform(-1, 1))
        py_face.set_value(FaceBlendShape.HeadRoll,random.uniform(-1, 1))
        py_face.set_value(FaceBlendShape.HeadYaw, random.uniform(-1, 1))
        s.sendall(py_face.encode())
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
        
finally: 
    s.close()

