"""
Both Alice & Bob have friends. Create a Java/Python/JS/Typescript console application to find all the friends of Alice and all the friends of Bob & common friends of Alice and Bob.
Your algorithm should be able to do the following:
Take any 2 friends and find the common friends between the 2 friends
Take any 2 friends find the nth connection - for example: connection(Alice, Janice) => 2
Alice has friend Bob and Bob has friend Janice, if the input given is Alice and Janice the output should be 2, meaning 2nd connection, that means Janice is the second connection of Alice and Bob being the 1st connection of Alice.
Likewise if input given is Alice and Bob, the output should be 1, for 1st connection
If there is no connection at all, it should return -1

"""

from collections import defaultdict, deque

def find_friends_and_connections(friends):
    def bfs(start, end):
        queue = deque([(start, 0)])
        visited = set()
        while queue:
            current, depth = queue.popleft()
            if current == end:
                return depth
            if current not in visited:
                visited.add(current)
                queue.extend((neighbor, depth + 1) for neighbor in friends[current] if neighbor not in visited)
        return -1

    def common_friends(f1, f2):
        return friends[f1].intersection(friends[f2])

    return bfs, common_friends

def main():
    friends = defaultdict(set)
    friends['Alice'] = {'Bob', 'Carol'}
    friends['Bob'] = {'Alice', 'Dave', 'Janice'}
    friends['Carol'] = {'Alice', 'Eve'}
    friends['Dave'] = {'Bob'}
    friends['Janice'] = {'Bob'}
    friends['Eve'] = {'Carol'}

    bfs, common_friends = find_friends_and_connections(friends)

    print("Friends of Alice:", friends['Alice'])
    print("Friends of Bob:", friends['Bob'])
    print("Common friends of Alice and Bob:", common_friends('Alice', 'Bob'))
    print("Connection between Alice and Janice:", bfs('Alice', 'Janice'))
    print("Connection between Alice and Dave:", bfs('Alice', 'Dave'))
    print("Connection between Alice and Eve:", bfs('Alice', 'Eve'))

if __name__ == "__main__":
    main()

"""
Time Complexity:

1. Building the Graph: Building the graph from input data involves adding each
friend and their connections. If there are V friends and E connections, this 
step takes O(V + E) time.

2. Breadth-First Search (BFS) for Connections: In the worst case, BFS will visit
each friend and each connection once. Therefore, finding the nth connection takes
O(V + E) time.

3. Finding Common Friends: Finding common friends involves intersecting two sets.
If each set has an average size of F, the intersection operation takes O(F) time.
In the worst case, F could be V (if every friend is connected to every other friend),
leading to O(V) time.

Overall, the time complexity for the BFS operation is O(V + E), and for finding 
common friends, it is O(V) in the worst case.

Space Complexity:

1. Storing the Graph: The graph is stored using adjacency lists or sets, requiring
O(V + E) space.

2. Queue for BFS: The maximum size of the queue in BFS is O(V).

Overall, the space complexity is O(V + E) for storing the graph and O(V) for the BFS queue.

Summary:

Time Complexity:
BFS for nth connection: O(V + E)
Finding common friends: O(V) in the worst case

Space Complexity: O(V + E)

"""