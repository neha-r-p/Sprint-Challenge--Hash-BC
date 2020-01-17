#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #inputting weights into ht
    for i in range(0,len(weights)):
        # print("weight index", i, weights[i])
        hash_table_insert(ht, weights[i], i)

    for i in range(0, len(weights)):
         #retrieve first weight
        weight1 = weights[i]
        print("weight1", weight1)
         #subtract weight from limit
        weight2 = limit - weight1
        print("weight2", weight2)
        weight2_in_table = hash_table_retrieve(ht, weight2)
        print("weight2 in table", weight2_in_table)
        #check to see if the other weight exists in table
        if weight2_in_table is not None:
            #return tuple, larger weight at index 0
            if i > weight2_in_table:
                print("return", i, weight2_in_table)
                return (i, weight2_in_table)
            else:
                print("return", weight2_in_table, i)
                return (weight2_in_table, i)
        #if not, move to next weight
        i+=1



        


    
        
    


    """
    YOUR CODE HERE
    """
    # hash_table_insert(ht, )

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
