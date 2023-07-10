#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    visited = set()

    def exploreBox(box_num):
        if box_num in visited:
            return

        visited.add(box_num)

        keys = boxes[box_num]
        for key in keys:
            if key < len(boxes):
                exploreBox(key)

    exploreBox(0)

    return len(visited) == len(boxes)


# Example usage
boxes = [
    [1],     # Box 0 has a key to Box 1
    [2],     # Box 1 has a key to Box 2
    [3, 4],  # Box 2 has keys to Box 3 and Box 4
    [],      # Box 3 has no keys
    [2],     # Box 4 has a key to Box 2
]

print(canUnlockAll(boxes))  # Output: True
