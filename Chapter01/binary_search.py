def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 3, 5, 8, 10]
    print(binary_search(my_list, 5))
    print(binary_search(my_list, -1))

# 假设有一个包含128个名字的有序列表，你要使用二分查找在其中查找一个名字，
# 请问最多需要几步才能找到？

...
# log2(128) =
...
