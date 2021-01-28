import os


name = os.getenv("INPUT_WHO_TO_GREET")

print("This has printed from a python script")
print(f"the input name was {name}")
print(os.environ)

