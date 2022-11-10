from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def nb_year(self, p0: int, percent: float, aug: int, p: int) -> int:
        """
        In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases 
        by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years 
        does the town need to see its population greater or equal to p = 1200 inhabitants?

        At the end of the first year there will be: 
        1000 + 1000 * 0.02 + 50 => 1070 inhabitants

        At the end of the 2nd year there will be: 
        1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

        At the end of the 3rd year there will be:
        1141 + 1141 * 0.02 + 50 => 1213

        It will need 3 entire years.
        More generally given parameters:

        p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

        the function nb_year should return n number of entire years needed to get a population greater or equal to p.

        aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

        Examples:
        nb_year(1500, 5, 100, 5000) -> 15
        nb_year(1500000, 2.5, 10000, 2000000) -> 10
        Note:
        Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.
        """
        raise NotImplementedError

    @abstractmethod
    def convert_number_to_reversed_array(self, num: int) -> list[int]:
        """
        Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
        Example(Input => Output):
        35231 => [1,3,2,5,3]
        0 => [0]
        """
        raise NotImplementedError

    @abstractmethod
    def testing123(self, lines: list[str]) -> list[str]:
        """
        Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
        Write a function which takes a list of strings and returns each line prepended by the correct number.
        The numbering starts at 1. The format is n: string. Notice the colon and space in between.
        Examples: (Input --> Output)
        [] --> []
        ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
        """
        raise NotImplementedError


        