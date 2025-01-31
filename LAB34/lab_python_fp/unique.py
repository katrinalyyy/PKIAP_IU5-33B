class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(items)

    def __next__(self):
        while True:
            item = next(self.iterator)
            comparison_value = item.lower() if self.ignore_case and isinstance(item, str) else item
            
            if comparison_value not in self.seen:
                self.seen.add(comparison_value)
                return item

    def __iter__(self):
        return self
