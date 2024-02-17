#!/usr/bin/python3
import py_compile
import os
n = os.getenv('PYFILE')
py_compile.compile(file=n,cfile=n+'c')
