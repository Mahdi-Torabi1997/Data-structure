class InsertionSort:
    def __init__(self, data):
        self.data = data
        
    def sort(self):
        # Traverse through 1 to len(data)
        for i in range(1, len(self.data)):
            key = self.data[i]
            # Move elements of data[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >=0 and key < self.data[j]:
                self.data[j+1] = self.data[j]
                j -= 1
            self.data[j+1] = key
        return self.data

# Example usage:
# sorting = InsertionSort([12, 11, 13, 5, 6])
# sorted_data = sorting.sort()
# print(sorted_data)
