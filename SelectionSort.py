class SelectionSort:
    def __init__(self, data):
        self.data = data
        
    def sort(self):
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
        return self.data

# Example usage:
# selection_sort = SelectionSort([64, 25, 12, 22, 11])
# sorted_data = selection_sort.sort()
# print(sorted_data)
