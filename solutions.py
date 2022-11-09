from I_solutions import SolutionInterface

class Solution(SolutionInterface):
    def __init__(self) -> None:
        super().__init__()

    def convert_number_to_reversed_array(self, num):
        return [int(x) for x in reversed(str(num))]

    def testing123(self, lines):
        return [f"{i}: {v}" for i, v in enumerate(lines, start=1)]

if __name__ == '__main__':
    print("python solution")
    s = Solution()
    print(s.testing123(["a", "b", "c"]))
