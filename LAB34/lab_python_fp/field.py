def field(items: list, *args) -> None:
    for item in items:
        for key in args:
            if item[key]:
                print(item[key])


def main():
     goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
        ]
     field(goods, 'title')
     field(goods, 'title', 'price')


if __name__ == "__main__":
    main()
