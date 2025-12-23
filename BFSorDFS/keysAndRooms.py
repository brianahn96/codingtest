# https://leetcode.com/problems/keys-and-rooms/description/

def canVisitAllRooms(rooms: list[list[int]]) -> bool:

    stack = rooms[0]
    visited = {0}

    while stack:
        key = stack.pop()

        if key in visited:      
            continue

        visited.add(key)

        for next_key in rooms[key]:
            stack.append(next_key)

    return len(visited) == len(rooms)