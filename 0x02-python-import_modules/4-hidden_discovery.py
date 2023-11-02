#!/usr/bin/python3
import py_compile
import dis
if __name__ != "__main__":
    exit()
py_compile.compile('hidden_4.pyc')
import hidden_4
names = dir(hidden_4)
filtered_names = sorted(name for name in names if not name.startswith("__"))
for name in filtered_names:
    print(name)
