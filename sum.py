#sum of first n natural numbers
def add_first_n_numbers(n):
    return n * (n + 1) // 2  

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = add_first_n_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {result}")
