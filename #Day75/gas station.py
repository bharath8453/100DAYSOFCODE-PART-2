class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            # If at any point we run out of gas, we can't start from previous stations
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        # If total gas is less than total cost, journey is impossible
        return start_station if total_tank >= 0 else -1


obj = Solution()
print(obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  
print(obj.canCompleteCircuit([2,3,4], [3,4,3]))  