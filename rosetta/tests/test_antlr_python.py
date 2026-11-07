import sys
import os
from rosetta.babel.python.antlr_frontend import PythonAntlrFrontend

source = """
def hello(name):
    print("Hello " + name)

x = 10
if x > 5:
    hello("World")
"""

frontend = PythonAntlrFrontend()
ir = frontend.parse(source)

print("--- Rosetta IR (from ANTLR) ---")
print(ir)
