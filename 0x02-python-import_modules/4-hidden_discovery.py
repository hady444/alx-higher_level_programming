#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
filtered_names = sorted(name for name in names if not name.startswith("__"))
for name in filtered_names:
    print(name)
