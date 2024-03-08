class BubbleSort:
    def __init__(self, data):
        self.data = data
    
    def sort(self):
        n = len(self.data)
        # Traverse through all elements in the data
        for i in range(n):
            # Last i elements are already sorted
            for j in range(0, n-i-1):
                # Traverse the data from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
        return self.data

# Example usage:
# sorting = BubbleSort([64, 34, 25, 12, 22, 11, 90])
# sorted_data = sorting.sort()
# print(sorted_data)
