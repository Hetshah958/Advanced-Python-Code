import gc
import tracemalloc

class Node:
    """A small object used to demonstrate reference cycles."""
    def __init__(self, value):
        self.value = value
        self.reference = None

def memory_usage(label):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{label}: current={current:,} bytes, peak={peak:,} bytes")

def create_reference_cycles(count=1000):
    for index in range(count):
        first = Node(index)
        second = Node(index + 1)
        first.reference = second
        second.reference = first
        # The local references disappear after each iteration; the cycle remains.

def main():
    tracemalloc.start()
    print("Garbage collection thresholds:", gc.get_threshold())
    print("Garbage collector enabled:", gc.isenabled())
    memory_usage("Initial memory")

    create_reference_cycles()
    memory_usage("After creating reference cycles")

    collected = gc.collect()
    print(f"Garbage collector collected {collected} objects.")
    memory_usage("After manual collection")

    print("Updated collection counts:", gc.get_count())
    tracemalloc.stop()

if __name__ == "__main__":
    main()
