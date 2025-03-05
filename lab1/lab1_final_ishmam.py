# -*- coding: utf-8 -*-


#@title Read Input File
data_list = []
file_path = "cities.txt"
with open(file_path, "r") as file:
    data_list = [line.strip() for line in file]

print(data_list)
for i in data_list:
  print(i)

#@title Heuristic and Nodes Dictionary
heuristic_value = {}
nodes_value = {}

#@title Update The Heuristic Dictionary
for hv in data_list:
  heuristic_list = []
  heuristic_list = hv.split(" ")
  heuristic_value[heuristic_list[0]] = int(heuristic_list[1]) # node ar tar heuristic value

heuristic_value

#@title Update the Keys of Nodes Values
# Format ==> Node : [[neighbour, value], [neighbour1, value1]]

for a in data_list:
  splitted = []
  splitted = a.split(" ")
  nodes_value[splitted[0]] = [] # shudhu amar current node ta ke key hisebe add korbo dictionary te
print(nodes_value)

#@title Update the Values of Node Dictionary

for a in data_list:
  splitted1 = []
  splitted1 = a.split(" ")

  # splitted 1 list e amader full text ache
  # ekhn amra 2 theke shuru korbo tarpor len porjonto update korbo
  for i in range(2, len(splitted1), 2):
    nodes_value[splitted1[0]].append([splitted1[i], int(splitted1[i+1])])

#@title Update the Values of Node Dictionary
# print(nodes_value)
# ekhane amar proti node er child value ache
for key, value in nodes_value.items():
  print(f"{key} : {value}")

def a_star(priorityQueue, visited, graph, heuristic_value, destination):
  # prothom kaj hocche check kora, jodi amar queue faka hoye jay tahole ami recursion venge dibo
  if not priorityQueue:
    print("No path found.")
    return None

  # jodi priority queue e kisu thake tahole:
  priorityQueue.sort(key=lambda x: x[1]) # sort according to value
  popped = priorityQueue.pop(0)
  # print(popped)
  # print(visited)
  # f(n)     =    g(n)    +     h(n)
  # total cost = actual cost + heuristic cost
  currentState, total_cost, actual_cost, path = popped
  # print(graph[currentState])

  if currentState == destination:
    print("Path found, path is: ")
    for i in range (0, len(path)):
      if i < len(path)-1:
        print(path[i], end=" -> ")
      else:
        print(path[i])
    print("Total cost is: ", total_cost)
    return

    # jodi amar currentcity already theke thake, tahole skipppppp
  if currentState in visited:
    # print("already there")
    return
  # jodi na theke thake, tahole push korbo
  visited.append(currentState)
  # print(visited)


  for neighbor, cost in graph[currentState]:
    # ami koi theke aschi, sei onujayi cost
    iterated_actual_cost = actual_cost + cost
    # total cost
    total_cost = iterated_actual_cost + heuristic_value[neighbor]
    # print(neighbor)
    # print(total_cost)

    if neighbor not in visited:
      # priority queue update hobe, basically abar notun kore recursion
      priorityQueue.append([neighbor, total_cost, iterated_actual_cost, path + [neighbor]])
  # recursion er loop
  return a_star(priorityQueue, visited, graph, heuristic_value, destination)

start = 'Arad'
destination = 'Bucharest'
priorityQueue = [[start, heuristic_value[start], 0, [start]]]
visited = []
# nodes value hoitese basically amar graph
a_star(priorityQueue, visited, nodes_value, heuristic_value, destination)
