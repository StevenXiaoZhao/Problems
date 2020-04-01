from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list1, list2 = list2, list1

        list_index = dict()
        count = len(list1)
        for i in range(count):
            list_index[list1[i]] = i

        count2 = len(list2)
        index_sum = count + count2
        index_restaurant = dict()
        for i in range(count2):
            if list2[i] in list_index:
                index = i+ list_index[list2[i]]
                if index < index_sum:
                    index_sum = index
                    index_restaurant.clear()
                    index_restaurant[index] = [list2[i]]
                elif index == index_sum:
                    index_restaurant[index].append(list2[i])

        if len(index_restaurant)>0:
            return index_restaurant[index_sum]

        return []

print(Solution().findRestaurant(["Shogun", "KFC", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
