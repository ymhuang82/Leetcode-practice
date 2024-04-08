def run_tests(questions, answers, Solution, method_name):
    for i, (question, answer) in enumerate(zip(questions, answers)):
        sol = Solution()
        method = getattr(sol, method_name)
        result = method(**question)
        if result != answer:
            print(f'Test Case {i}: Failed! Expected {answer}, Got {result}')
        else:
            print(f'Test Case {i}: Passed!')