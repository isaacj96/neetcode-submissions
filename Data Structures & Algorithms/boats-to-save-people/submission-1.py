class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        count = 0
        people.sort()

        while l <= r:
            remainder = limit - people[r]
            r -= 1
            count += 1
            if remainder >= people[l]:
                l += 1

        return count