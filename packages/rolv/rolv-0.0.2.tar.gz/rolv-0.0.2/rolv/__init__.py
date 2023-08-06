from . import bashrc

def version():
    print("0.0.1")

def install():
    bashrc.set_bashrc()

