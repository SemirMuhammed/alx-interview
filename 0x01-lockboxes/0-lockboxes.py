#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        False: not all boxes can be opened
        True: all boxes can be opened
    '''
    box_length = len(boxes)
    box_keys = set()
    opened_boxes = []
    i = 0

    while i < box_length:
        previous_iteration = i
        opened_boxes.append(i)
        box_keys.update(boxes[i])
        for key in box_keys:
            if key != 0 and key < box_length and key not in opened_boxes:
                i = key
                break
        if previous_iteration != i:
            continue
        else:
            break

    for i in range(box_length):
        if i not in opened_boxes and i != 0:
            return False
    return True
