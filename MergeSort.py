class MergeSort:
    def __init__(self, data):
        self.data = data
    
    def sort(self):
        if len(self.data) > 1:
            mid = len(self.data) // 2
            L = self.data[:mid]
            R = self.data[mid:]

            # Sorting the first half
            left_sort = MergeSort(L)
            L = left_sort.sort()

            # Sorting the second half
            right_sort = MergeSort(R)
            R = right_sort.sort()

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    self.data[k] = L[i]
                    i += 1
                else:
                    self.data[k] = R[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                self.data[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                self.data[k] = R[j]
                j += 1
                k += 1

        return self.data

# Example usage:
# sorting = MergeSort([38, 27, 43, 3, 9, 82, 10])
# sorted_data = sorting.sort()
# print(sorted_data)
