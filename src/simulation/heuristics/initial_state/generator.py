"""
Initial State Generator
"""

from models.establishment import Establishment
from ...graph import Graph


class Generator:  # pylint: disable=too-few-public-methods
    """
    Generator class that has a method **generate**
    that takes a list of establishments and the desired number of carriers
    and generates a sample from the same list to be used
    in the initial state of the simulation
    """

    @staticmethod
    def next(
        establishments: dict[int, Establishment],
        previous: Establishment,
        graph: Graph,
    ) -> Establishment:
        """
        Generates a sample of establishments
        to be used in the applications initial state.

        The return value takes the form (<sample>, <rest>).

        The default implementation takes no sample and returns its parameter
        """

        return establishments.popitem()[1]
