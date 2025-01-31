def sort(items: list) -> list:
    return list(sorted(items))


lambda_sort = lambda items: sorted(items)


if __name__ == "__main__":
    print(sort(["amanda", "zuck", "bob"]))
    print(lambda_sort([5, 3, 7]))
