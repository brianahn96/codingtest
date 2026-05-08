# Overall Time Complexity: O(N + K), where N is the number of rooms and K is the total number of keys across all rooms
# Overall Space Complexity: O(N), for storing the visited set and the exploration stack

# Define a function to determine if every room in the building can be accessed starting from room 0
def canVisitAllRooms(rooms: list[list[int]]) -> bool:

    # Initialize a stack using the initial set of keys available in the first room (index 0)
    stack = rooms[0]
    # Create a set to keep track of room indices that have been visited, starting with room 0
    visited = {0}

    # Continue the exploration process as long as there are keys remaining in the stack
    while stack:
        # Retrieve the next available key by popping it from the stack
        key = stack.pop()

        # Check if the room corresponding to this key has already been visited
        if key in visited:      
            # If already visited, skip processing this key to avoid redundant work
            continue

        # Add the current room index to the set of visited rooms
        visited.add(key)

        # Retrieve the list of keys found inside the room we just entered
        for next_key in rooms[key]:
            # Push each new key found onto the stack for later room exploration
            stack.append(next_key)

    # Compare the total number of unique rooms visited to the total number of rooms in the input list
    return len(visited) == len(rooms)
