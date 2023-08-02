#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    unlocked_boxes = set([0])
    keys = boxes[0]

    while keys:
        new_keys = []
        for key in keys:
            if 0 <= key < n and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                new_keys.extend(boxes[key])
        keys = new_keys

    return len(unlocked_boxes) == n

