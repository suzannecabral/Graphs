import random
import time
class Queue():
    def __init(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range (0, num_users):
            self.add_user(f"User {i + 1}")

            # generate all possible friendships
            # create a list of possible friendships
            # Create friendships
        possible_friendships = []

            # will give you a long list, pick the first X many friends so you don't have convoluted steps
            
        # to avoid duplicates 
        # make sure that first number is smaller than second number
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
            # end of range is not inclusive

        # shuffle all possible friendships (randomize order)
        random.shuffle(possible_friendships)

        # create friendships for the first n pairs of the list of friends
        # X determined by the formula; num_users * avg_friendships // 2
        # // floor divide gives a whole number
        # add friendship creates 2 friendships, a to b and b to a
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create an empty queue
        # enqueue the first path
        # while the queue is not empty
            # dequeue the path
            # set a newuser_id to the last element of the path 
            # last item = arr[-1]
            # if the newuser_id is not in visited:
                # set the visited at the key of newuser_id to the path
                # for every friend_id in the friendships at the key of newuser_id
                    # make a copy of the path caalled new_path (not a reference back)
                    # append the friend_id to the new_path
                    # enqueue the new path
        # return the populated visited dictionary to the caller
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)

