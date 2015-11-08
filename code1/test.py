import os

print os.path.split(__file__)

print os.path.join(
    os.path.split(__file__)[0],
    "..",
    "data",
    "abc"
)
print os.path.isfile("../test.py")
