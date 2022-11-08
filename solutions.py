
class Solution:

    def convert_number_to_reversed_array(self, num):
        """
        Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
        Example(Input => Output):
        35231 => [1,3,2,5,3]
        0 => [0]
        """
        return [int(x) for x in reversed(str(num))]

    def testing123(self, lines):
        """
        Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
        Write a function which takes a list of strings and returns each line prepended by the correct number.
        The numbering starts at 1. The format is n: string. Notice the colon and space in between.
        Examples: (Input --> Output)
        [] --> []
        ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
        """
        return [f"{i}: {v}" for i, v in enumerate(lines, start=1)]

    if __name__ == '__main__':
        algo = AlgoDs()


# class Person:
#     name = []

#     def set_name(self, user_name):
#         self.name.append(user_name)
#         return len(self.name) - 1

#     def get_name(self, user_id):
#         if user_id >= len(self.name):
#             return 'There is no such user'
#         else:
#             return self.name[user_id]


# if __name__ == '__main__':
#     person = Person()
#     print('User Abbas has been added with id ', person.set_name('Abbas'))
#     print('User associated with id 0 is ', person.get_name(0))