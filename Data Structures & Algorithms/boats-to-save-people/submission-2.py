class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        people.sort()
        boats = 0
        while l <= r:
            remainder = limit - people[r]
            boats += 1
            r -= 1
            if remainder >= people[l]:
                l += 1
        return boats