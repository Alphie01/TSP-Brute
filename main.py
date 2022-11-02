import itertools
import sys



def main():
    #nodes and instanceSize are passed into main() using another program
    #I just gave them default values for this example

    #The Node lookup table. 200 124 90 78
    try_data=  [[0, 5, 2, 1]
    , [5, 0, 4, 7]
    , [2, 4, 0, 3]
    , [1, 7, 3, 0]]
    try_data1= [[0, 118, 200, 167, 207, 211, 199, 119],
        [118, 0, 124, 90, 129, 98, 86, 88],
        [200, 124, 0, 40, 10, 72, 44, 208],
        [167, 90, 40, 0, 48, 78, 78, 180],
        [207, 129, 10, 48, 0, 67, 39, 165],
        [211, 98, 72, 78, 67, 0, 34, 181],
        [199, 86, 44, 78, 39, 34, 0, 168],
        [119, 88, 208, 180, 165, 181, 168, 0]]

    cities = ["London","Birmingham","Leeds","Sheffield","Bradford","Liverpool","Manchester","Bristol"]

    minCosts = minFunc(try_data1)
    print("Minumum cost : ", minCosts[0])
    print("Route that has minimum cost : ",Searchcities(cities,  minCosts[1]))
    selectedCities = 4
    selectedRoute = selectedOnes(try_data1, selectedCities)
    print("Minumum cost that start from selected city : ", selectedRoute[0])
    print("selected city Route that has minimum cost : ", Searchcities(cities, selectedRoute[1]))




def Searchcities(cities, listedCities):
    names = []
    for i in listedCities:
        names.append(cities[i])
    
    return names





def minFunc(arrays):
    s = 0
    count = len(arrays)
    optimal = []
    v = []
    for i in range(0,count):
        v.append(i)

    minimum_node = 9223372036854775807
    calculate_perm =itertools.permutations(v)
    for i in calculate_perm:



        cost_of_the_current_path = 0

        # compute current path weight
        z = s
        for j in i:
            cost_of_the_current_path += arrays[z][j]
            z = j
        cost_of_the_current_path += arrays[z][s]

        # update minimum
        if cost_of_the_current_path<minimum_node:

            minimum_node= min(minimum_node, cost_of_the_current_path)
            optimal = i
            optimal = optimal + (optimal[0],)


    return (minimum_node, optimal)




def selectedOnes(arrays, selected):
    s = 0
    count = len(arrays)
    optimal = []
    v = []
    for i in range(0,count):
        v.append(i)

    minimum_node = 9223372036854775807
    calculate_perm =itertools.permutations(v)
    for i in calculate_perm:


        if i[0] == selected:

            cost_of_the_current_path = 0

            # compute current path weight
            z = s
            for j in i:
                cost_of_the_current_path += arrays[z][j]
                z = j
            cost_of_the_current_path += arrays[z][s]

            # update minimum
            if cost_of_the_current_path<minimum_node:

                minimum_node= min(minimum_node, cost_of_the_current_path)
                optimal = i
                optimal = optimal + (optimal[0],)

    return (minimum_node, optimal)


if __name__ == '__main__':
    main()




