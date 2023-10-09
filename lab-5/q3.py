class SubsetGenerator:
    def __init__(self, input_set):
        self.input_set = list(input_set)
        self.subsets = []

    def generate_subsets(self):
        self._generate([], 0)
        return self.subsets

    def _generate(self, current_subset, start_index):
        self.subsets.append(list(current_subset))

        for i in range(start_index, len(self.input_set)):
            current_subset.append(self.input_set[i])
            self._generate(current_subset, i + 1)
            current_subset.pop()


if __name__ == "__main__":
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)

generator = SubsetGenerator(lst)
subsets = generator.generate_subsets()

for subset in subsets:
    print(subset)
