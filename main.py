def greet(name:str = "John Doe") -> str:
    return f"Hello {name}"

if __name__ == "__main__":
    message = greet("Rajesh Joshi")
    print(message)
