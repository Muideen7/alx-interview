#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    Check if all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the locked boxes.

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise.
    """
    totalBoxes = len(boxes)
    checkBox = [False] * total_boxes
    checkBox[0] = True
    stack = [0]

    while stack:
        currentBox = stack.pop()
        keys = boxes[currentBox]

        for key in keys:
            if key < total_boxes and not check_box[key]:
                checkBox[key] = True
                stack.append(key)

    return all(checkBox)
