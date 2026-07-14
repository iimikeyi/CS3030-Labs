import os
import psutil

# Memory Peak observed during testing: 204.52 MB 

def get_memory_mb(process):
    """Return current memory usage in MB."""
    return process.memory_info().rss / (1024 * 1024)

def main():
    process = psutil.Process(os.getpid())

    starting_memory = get_memory_mb(process)
    print(f"Starting memory footprint: {starting_memory:.2f} MB")

    print("Generating 5,000,000 numbers...")
    big_list = [i for i in range(5_000_000)]

    ending_memory = get_memory_mb(process)
    print(f"Memory after task: {ending_memory:.2f} MB")

    consumed = ending_memory - starting_memory
    print(f"Memory consumed by task: {consumed:.2f} MB")

    cpu_time = process.cpu_times()
    print(f"CPU time - user: {cpu_time.user:.4f}s, system: {cpu_time.system:.4f}s")

if __name__ == "__main__":
    main()
