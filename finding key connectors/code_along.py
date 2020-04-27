"""
p.3 — I.D. who the 'key connectors' are among a network.
"""

# data dump
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# friendship data
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# initialize the dict w/an empty list for each user id (looking things up in a dict is very fast):
friendships = {user["id"]: [] for user in users}

# loop over the friendship pairs to populate it:
