"""
Script to demonstrate the import functionality of python code
"""


Greetings = "Good Morning"

def hello_world():
    """ Hello world function"""
    print("Hello world")


if __name__ == "__main__":
    hello_world()
else:
    print(
        f"""
        {__name__    =}
        {__package__ =}
    """
    )

