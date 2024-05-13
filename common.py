from copy import deepcopy
from typing import Union


def run_tests(
    questions: list[dict],
    answers: list,
    Solution: object,
    inplace_modification: Union[list[dict], None] = None,
    method_name: Union[str, None] = None,
    copy: bool = True,
):
    """Run test cases to validate the correctness of a given solution method.

    Parameters
    ----------
    questions : list[dict]
        A list of input questions, each question represented as a dictionary.
    answers : list
        A list of expected answers corresponding to each question.
    Solution : object
        The class containing the solution methods.
    method_name : Union[str, None], optional
        The name of the method to be tested. If not provided, the function
        automatically finds callable method names in the Solution class. If
        there are more than two, an error will be raised. Default is None.
    copy : bool, optional
        Whether to create a deep copy of input objects to prevent modification.
        Default is True.

    Raises
    ------
    ValueError
        If method_name is not provided and there are more than two callable
        method names in the Solution class.

    Notes
    -----
    Date: 2024/04/10
        Some solutions may modify the input objects. To prevent this, we provide
        the option to make copies. For complex objects like nested lists, a
        shallow copy may not be sufficient, so we use deepcopy.
    """
    if method_name is None:
        callable_method = [x for x, y in Solution.__dict__.items() if callable(y)]
        if len(callable_method) != 1:
            raise ValueError(
                "Method name not provided, and multiple callable "
                "methods found in the Solution class. "
                "Please specify the method_name parameter."
            )
        method_name = callable_method[0]

    if copy:
        questions, answers = deepcopy([questions, answers])

    for i, (question, answer) in enumerate(zip(questions, answers)):
        solution_instance = Solution()
        method = getattr(solution_instance, method_name)
        result = method(**question)
        if result != answer:
            print(f"Test Case {i}: Failed! Expected {answer}, Got {result}")
        elif inplace_modification is not None and question != inplace_modification[i]:
            print(
                f"Test Case {i}: In-place modification failed! Expected {inplace_modification[i]}, Got {question}"
            )
        else:
            print(f"Test Case {i}: Passed!")
