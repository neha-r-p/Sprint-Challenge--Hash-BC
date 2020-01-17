#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #source is key to hash, destination is value. create hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    #intiialize route with the source None ticket
    route[0] = hash_table_retrieve(hashtable, "NONE")
    #hash value of previous key to find next destination
    #replace index value in route array until last one (NONE)
    for i in range(1,length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
