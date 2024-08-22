from handlers.handler import Handler


class AlgorithmHandlers(Handler):
    def add_algorithm(self, user_id: int, name: str, description: str) -> None:
        """
        Add a new algorithm. (just for admin user)

        Flow:
        - create algorithm object
        - convert to dict
        - save in DB

        :param user_id: user id to validate admin user.
        :param name: algorithm name.
        :param description: algorithm description.(needs to find specific template)
        :return: None
        """
        pass

    def get_algorithms(self, user_id: int):
        """
        Return the list of algorithms

        Flow:
        - get algorithms from DB

        :param user_id: user id to get algorithms by permissions
        :return: the list of dicts algorithms
        """
        pass
