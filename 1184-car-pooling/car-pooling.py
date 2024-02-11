class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        #https://www.youtube.com/watch?v=nO95uYKB-lo
        # lastDropPoint=0
        # for route in trips:
        #     if route[2]>lastDropPoint:
        #         lastDropPoint=route[2]
        # Person_count_arr=[0]*(lastDropPoint+1)

        # for pick_drop in trips:
        #     Person_count_arr[pick_drop[1]]=Person_count_arr[pick_drop[1]]+pick_drop[0]
        #     Person_count_arr[pick_drop[2]]=Person_count_arr[pick_drop[2]]-pick_drop[0]
        # current_capacity=0
        # for setted_passanger in Person_count_arr:
        #     current_capacity+=setted_passanger
        #     if current_capacity>capacity:
        #         return False
        # return True

        #or 

        timeline = [0] * 1001
        for numPassengers, start, end in trips:
            timeline[start] += numPassengers
            timeline[end] -= numPassengers
        
        passengers = 0
        for change in timeline:
            passengers += change
            if passengers > capacity:
                return False
        return True
