class Sort:
    bubble_O = 'O(n^2)'
    merge_O = 'O(n log n)'
    quick_O = 'O(n log n)'

    @classmethod
    def bubble(self, array):
        for i in range(len(array) - 1):
            for j in range(len(array) - 1):
                if j < len(array) - 1:
                    if array[j + 1] < array[j]:
                        array[j + 1], array[j] = array[j], array[j + 1]

        return array

    @classmethod
    def merge(self, array):
        length = len(array)

        if length > 1:
            middle = length // 2
            left = self.merge(array[:middle])
            right = self.merge(array[middle:])
            return self.__merge_two_list(left, right)

        elif length == 1:
            return array

    @classmethod
    def __merge_two_list(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    @classmethod
    def quick(self, array):
        if len(array) <= 1:
            return array
            
        elem = array[0]

        less = []
        equal = []
        more = []

        for i in array:
            if i < elem:
                less.append(i)
            elif i == elem:
                equal.append(i)
            elif i > elem:
                more.append(i)

        return self.quick(less) + equal + self.quick(more)