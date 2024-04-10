from copy import deepcopy

def run_tests(questions: list, answers: list, Solution: object, method_name: str, copy: bool=True):
    """Run test cases to validate the correctness of a given solution method.

    Parameters
    ----------
    questions : list
        A list of input questions, each question represented as a dictionary.
    answers : list
        A list of expected answers corresponding to each question.
    Solution : object
        The class containing the solution methods.
    method_name : str
        The name of the method to be tested.
    copy : bool, optional
        Whether to create a deep copy of input objects to prevent modification.
        Defaults to True.

    Notes
    -----
    Date: 2024/04/10
        Some solutions may modify the input objects. To prevent this, we provide
        the option to make copies. For complex objects like nested lists, a
        shallow copy may not be sufficient, so we use deepcopy.
    """
    if copy:
        questions, answers = deepcopy([questions, answers])

    for i, (question, answer) in enumerate(zip(questions, answers)):
        solution_instance  = Solution()
        method = getattr(solution_instance , method_name)
        result = method(**question)
        if result != answer:
            print(f'Test Case {i}: Failed! Expected {answer}, Got {result}')
        else:
            print(f'Test Case {i}: Passed!')