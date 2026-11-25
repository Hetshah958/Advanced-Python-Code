import threading

numbers = list(range(1, 11))

def count_numbers():
    for number in numbers:
        print(f"[Counting] {number}")

def calculate_squares():
    for number in numbers:
        print(f"[Square] {number}² = {number ** 2}")

def calculate_cubes():
    for number in numbers:
        print(f"[Cube] {number}³ = {number ** 3}")

def main():
    tasks = [
        threading.Thread(target=count_numbers, name="Counter"),
        threading.Thread(target=calculate_squares, name="Squares"),
        threading.Thread(target=calculate_cubes, name="Cubes"),
    ]
    for thread in tasks:
        thread.start()
    for thread in tasks:
        thread.join()
    print("All three tasks have completed.")

if __name__ == "__main__":
    main()
