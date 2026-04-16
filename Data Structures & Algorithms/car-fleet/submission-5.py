class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = []
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            value = (target - p)/s
            if len(result) == 0 or result[-1] < value:
                result.append(value)
                
        return len(set(result))
        