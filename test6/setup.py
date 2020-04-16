"""
setup.py file for SWIG C\+\+/Python example
"""
from distutils.core import setup, Extension
datagen_module = Extension('_DataGen',
                           sources=['DataGen.cpp', 'DataGen_wrap.cxx',],
                           )
setup (name = 'DataGen',
       version = '0.1',
       author      = "wxh",
       description = """Simple swig C\+\+/Python example""",
       ext_modules = [datagen_module],
       py_modules = ["DataGen"],
       )
