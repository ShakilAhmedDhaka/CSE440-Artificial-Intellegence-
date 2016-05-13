# Name: Shakil Ahmed
# NSU ID: 121 0499 042
# assignment no: 1


import heapq as pq

__author__ = 'Shakil'

# first Input is taken
input_file = raw_input("Enter Input: ")  # "input1.txt"

input_info = input_file.split()
input_file = input_info[0]
origin_city = input_info[1]
destination_city = input_info[2]

# Now a graph will generated
my_file = open(input_file, "r")
edge = {}
cost = {}
info = my_file.readline()
while info != "END OF INPUT":
    my_list = info.split(" ")
    dist = my_list[2].split("/n")
    x = my_list[0]
    y = my_list[1]
    c = int(dist[0])
    # Initialize the dictionary key if that key is not present. If already present do nothing.
    edge.setdefault(x, [])
    edge.setdefault(y, [])
    cost.setdefault(x, [])
    cost.setdefault(y, [])

    edge[x].append(y)
    edge[y].append(x)
    cost[x].append(c)
    cost[y].append(c)
    info = my_file.readline()
my_file.close()

# print edge
# print cost

# Calculation for shortest path starts

final_cost = {}
parent = {}
parent_cost = {}
q = []
pq.heappush(q, (0, origin_city))


def uniform_search():
    # print "in function"
    while len(q) != 0:
        # print "loop1"
        # u = parent node
        (dest, u) = pq.heappop(q)
        edges = edge[u]
        costs = cost[u]
        for i in range(len(edges)):
            # print "loop2"
            # v = child node
            v = edges[i]
            final_cost.setdefault(v, float("inf"))
            if dest+costs[i] < final_cost[v]:
                final_cost[v] = dest+costs[i]
                pq.heappush(q, (final_cost[v], v))
                parent[v] = u
                parent_cost[v] = costs[i]
                # print (final_cost[v], v)

# Calculation for shortest path ends

uniform_search()

# Now the result will bw printed following the given format
final_cost.setdefault(destination_city, float("inf"))
if final_cost[destination_city] < float("inf"):
    print "distance: " + str(final_cost[destination_city]) + " km"
    node = destination_city
    stack = []
    while node != origin_city:
        x = parent[node]+" to "+node+", "+str(parent_cost[node])+" km"
        stack.append(x)
        node = parent[node]
    print "route:"
    for i in range(len(stack)):
        routes = stack.pop()
        print routes
else:
    print "distance: infinity"
    print "route:"
    print "none"

# input1.txt Bremen Frankfurt
