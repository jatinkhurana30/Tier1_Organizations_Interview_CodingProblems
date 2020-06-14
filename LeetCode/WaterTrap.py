class Solution:
    def trap(self, height) -> int:
        trapped_water = 0
        trapped_water = self.find_water(trapped_water, height)
        return trapped_water

    def find_water(self, trapped_water, height):
        if height is None:
            return 0
        elif len(height) < 2:
            return 0

        trapped_water = self.find_trapped_water(height)
        start = min(height[0],height[-1])
        i = 0
        flag = True
        # Remove leading blocks
        while i < len(height):
            if (height[i] == start or height[i] == 0) and flag:
                height.pop(i)
                i -= 1
            else:
                flag = False
                break
            i += 1
        # Remove trailing blocks
        i = len(height) - 1
        flag = True
        while i >= 0:
            if (height[i] == start or height[i] == 0) and flag:
                height.pop(i)
            else:
                flag = False
                break
            i -= 1

        trapped_water += self.find_water(trapped_water, height)
        return trapped_water

    def find_trapped_water(self, block):
        distance_between_walls = len(block) - 2
        wall1 = block[0]
        wall2 = block[-1]
        if wall1 == 0 or wall2 == 0:
            return 0
        smaller_wall = min(wall1, wall2)
        water_retained = smaller_wall * distance_between_walls

        for k in block[1:len(block) - 1]:
            if k > smaller_wall:
                water_retained -= smaller_wall
            else:
                water_retained -= k

        j = 0
        while j < len(block):
            if block[j] < smaller_wall:
                block[j] = smaller_wall
            j += 1

        return water_retained


tower = [5,5,1,7,1,1,5,2,7,6]
print(Solution().trap(tower))

# print(Solution().find_block([2, 1]))
