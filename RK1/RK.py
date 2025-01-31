from operator import itemgetter


class Browser:
    def __init__(self, id, name, time_count, comp_id):
        self.id = id
        self.name = name
        self.time_count = time_count
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BrowserComputer:
    def __init__(self, browser_id, comp_id):
        self.browser_id = browser_id
        self.comp_id = comp_id


comps = [
    Computer(1, "Компьютер 1"),
    Computer(2, "Компьютер 2"),
    Computer(3, "Компьютер 3")
]
brows = [
    Browser(1, "Chrome", 120, 1),
    Browser(2, "Firefox", 100, 1),
    Browser(3, "Safari", 200, 2),
    Browser(4, "Opera", 150, 3),
    Browser(5, "Edge", 80, 3)
]
browser_pc_link = [
    BrowserComputer(1, 1),
    BrowserComputer(2, 1),
    BrowserComputer(3, 2),
    BrowserComputer(4, 3),
    BrowserComputer(5, 3)
]


def main():
    one_to_many = [(b.name, b.time_count, comp.name)
                   for comp in comps
                   for b in brows
                   if b.comp_id == comp.id]

    many_to_many_temp = [(comp.name, bc.comp_id, bc.browser_id)
                         for comp in comps
                         for bc in browser_pc_link
                         if comp.id == bc.comp_id]

    many_to_many = [(b.name, b.time_count, comp_name)
                    for comp_name, comp_id, browser_id in many_to_many_temp
                    for b in brows if b.id == browser_id]

    # Запрос 1
    print("Запрос 1")
    res_1 = [(b.name, comp.name) for b in brows if b.name.startswith("A") for comp in comps if b.comp_id == comp.id]
    print(*res_1)

    # Запрос 2
    print("\nЗапрос 2")
    res_2_unsorted = []
    for comp in comps:
        comp_brows = list(filter(lambda record: record[2] == comp.name, one_to_many))
        if comp_brows:
            min_time = min([time for browser_name, time, computer_name in comp_brows])
            res_2_unsorted.append((comp.name, min_time))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(*res_2)

    # Запрос 3
    print("\nЗапрос 3")
    res_3 = sorted(many_to_many, key=itemgetter(0))
    print(*res_3)


if __name__ == "__main__":
    main()
