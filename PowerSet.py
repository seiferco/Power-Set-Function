def print_set(inputSet):
    for subset in inputSet:
        print(subset)

def powerset(inputSet):
    
    answer_set = [] # will contain all subsets to be returned (powerset)                                                                [1,2,3]
    subset = [] #the current recursive subset                                                                                             /    \ 
                                                                                                                        #              [1]      []    idx = 0 (element: 1)
    def choices(idx):                                                                                                   #             /  \     /  \ 
        if idx >= len(inputSet):                                                                                        #        [1][2]   [1] [2] [] 
            answer_set.append(subset.copy())                                                                            #        /\        .   .   .    choice 1 is left subtree (do pick element at inputSet[idx])
        else:                                                                                                           #         .        .   .   .    choice 2 is right subtree (do not pick element at inputSet[idx])
            # Choice 1 (include the number at current idx of inputSet)                                                  #         .        .   .   .
            subset.append(inputSet[idx])                                                                                #           At ith layer, all subsets will be given (2^N) solutions (8 in this case)
            choices(idx + 1)

            # Choice 2 (do not include the number at current idx of inputSet)
            subset.pop()
            choices(idx + 1)

    choices(0)
    return answer_set

def main():
    set1 = [1,2,3]
    powerSet1 = powerset(set1)
    print_set(powerSet1)

    # set2 = []
    # powerSet2 = powerset(set2)
    # print_set(powerSet2)
    
    # set3 = [1,2,3]
    # powerSet3 = powerset(set3)
    # print_set(powerSet3)
main()