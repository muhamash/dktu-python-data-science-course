def last_bug():
    print("-" * 30)
    print("| I have written my last bug |")
    print("-" * 30)


def nice_sign(msg):
    dashes = "-" * (len(msg) + 4)
    print(dashes)
    print(f"| {msg} |")
    print(dashes)


# Testing last_bug() function
last_bug()

# Testing nice_sign() function
nice_sign("Hello World!")
nice_sign("This is a longer message")
nice_sign("Short")
