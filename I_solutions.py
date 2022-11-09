from abc import ABC, abstractmethod

class SolutionInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

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


        