import os


name = os.getenv("INPUT_WHOTOGREET")

print("This has printed from a python script")
print(f"the input name was {name}")
print(os.environ)

