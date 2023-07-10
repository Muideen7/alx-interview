#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
 and each box may contain keys to the other boxes.
"""
def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened_boxes = set([0])

    # List to store the keys obtained
    keys = boxes[0]

    # Iterate over the keys until no new keys are found
    while keys:
        new_keys = []

        # Check each key obtained
        for key in keys:
            # If the key corresponds to a box that hasn't been opened yet
            if key < len(boxes) and key not in opened_boxes:
                # Mark the box as opened and add its keys to the list of new keys
                opened_boxes.add(key)
                new_keys.extend(boxes[key])

        # Update the keys list with the new keys
        keys = new_keys

    # If all boxes have been opened, return True
    if len(opened_boxes) == len(boxes):
        return True

    # If there are still unopened boxes, return False
    return False
