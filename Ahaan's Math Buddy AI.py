import time

def solve_problem(problem):
    try:
        result = eval(problem)
        steps = [
        f'Solving your problem: {problem}',
        f'The answer is: {result}'
        ]
        for step in steps:
            print(step)
            time.sleep(1)
    except Exception as e:
        error_msg = f'Error solving the problem: {e}'
        print(error_msg)

if __name__ == '__main__':
    print('Welcome to Ahaan’s Math Buddy AI!')
    user_input = input('Enter a simple math problem (e.g., 4 + 5 * 2):')
    solve_problem(user_input)
