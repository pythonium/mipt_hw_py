try:
    int("asdf")
except ValueError:
    print("не интуится(((")
finally:
    print("дошел до \"finally\"")
