#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in sorted(names):
        if name[0:2] != "__":
            print(name)
