#!/usr/bin/python3
import hidden_4
if __name__ != "__main__":
    exit()
names = dir(hidden_4)
filtered_names = sorted(name for name in names if not name.startswith("__"))
for name in filtered_names:
    print(name)
