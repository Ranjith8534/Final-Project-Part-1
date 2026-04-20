import time

def dictionary_access(n):
    data = {i: i for i in range(n)}
    total = 0
    start = time.perf_counter()
    for key in data:
        total += data[key]
    end = time.perf_counter()
    return total, end - start

def list_access(n):
    data = list(range(n))
    total = 0
    start = time.perf_counter()
    for value in data:
        total += value
    end = time.perf_counter()
    return total, end - start

def main():
    sizes = [100000, 500000, 1000000]

    print("Data Locality Optimization Experiment")
    print("-" * 45)

    for n in sizes:
        dict_total, dict_time = dictionary_access(n)
        list_total, list_time = list_access(n)

        print(f"\nDataset Size: {n}")
        print(f"Dictionary Access -> Sum: {dict_total}, Time: {dict_time:.6f} seconds")
        print(f"List Access       -> Sum: {list_total}, Time: {list_time:.6f} seconds")

        if list_time < dict_time:
            improvement = ((dict_time - list_time) / dict_time) * 100
            print(f"Performance Improvement: {improvement:.2f}% faster using list")
        else:
            print("No improvement observed in this run")

if __name__ == "__main__":
    main()