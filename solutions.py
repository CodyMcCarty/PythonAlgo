from I_solutions import SolutionInterface

class Solution(SolutionInterface):
    def __init__(self) -> None:
        super().__init__()

    def nb_year(self, p0, percent, aug, p):
        percent, pop, year = percent / 100, p0, 0
        while pop < p:
            pop += pop * percent + aug
            year += 1
        return year

    def testing123(self, lines):
        return [f"{index}: {line}" for index, line in enumerate(lines, start=1)]

    # keeps ^

    def min_max(lst):
        return [min(list), max(lst)]

    def convert_number_to_reversed_array(self, num):
        return [int(x) for x in reversed(str(num))]



if __name__ == '__main__':
    print("python solution")
    s = Solution()
    print(s.nb_year(1500000, 2.5, 10000, 2000000))

