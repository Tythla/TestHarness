import subprocess
import os
import sys


def run_test(prog, test_name):
    input_file = f"test/{prog}.{test_name}.in"
    expected_output_file = f"test/{prog}.{test_name}.out"

    with open(input_file, 'r') as f:
        input_data = f.read()

    result = subprocess.run(
        ['python3', f'prog/{prog}.py', input_file], capture_output=True, text=True)
    output = result.stdout.strip()

    with open(expected_output_file, 'r') as f:
        expected_output = f.read().strip()
        
    if output != expected_output:
        print(f"Failed Test: {prog}.{test_name}")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(output)
        if result.stderr.strip():
            print("Error Output, if any:")
            print(result.stderr.strip())
    return output == expected_output


def main():
    tests = [
        ('gron', 'test'),
        ('ungron', 'test'),
        ('wc', 'test1')
    ]

    all_passed = True
    for prog, test_name in tests:
        if run_test(prog, test_name):
            print(f"Test {prog}.{test_name}: PASSED")
        else:
            print(f"Test {prog}.{test_name}: FAILED")
            all_passed = False

    if not all_passed:
        exit(1)


if __name__ == "__main__":
    main()
