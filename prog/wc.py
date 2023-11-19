import argparse

def word_count(filenames, flags=None):
    results = {}
    total_lines = total_words = total_chars = 0

    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

            results[filename] = (num_lines, num_words, num_chars)

            total_lines += num_lines
            total_words += num_words
            total_chars += num_chars

        except FileNotFoundError:
            results[filename] = "File not found."

    # Add totals if there iscmore than one file
    if len(filenames) > 1:
        results['total'] = (total_lines, total_words, total_chars)

    return results


parser = argparse.ArgumentParser(description="Word Count Tool")
parser.add_argument('filenames', nargs='+',
                    help="List of files to be processed")
parser.add_argument('-l', '--lines', action='store_true', help="Count lines")
parser.add_argument('-w', '--words', action='store_true', help="Count words")
parser.add_argument('-c', '--chars', action='store_true',
                    help="Count characters")

args = parser.parse_args()

flags = set()
if args.lines:
    flags.add('l')
if args.words:
    flags.add('w')
if args.chars:
    flags.add('c')


results = word_count(args.filenames, flags)

for filename, result in results.items():
    if isinstance(result, tuple):
        line_count, word_count, char_count = result
        output = []
        if not flags or 'l' in flags:
            output.append(f"{line_count:8}")
        if not flags or 'w' in flags:
            output.append(f"{word_count:8}")
        if not flags or 'c' in flags:
            output.append(f"{char_count:8}")
        output.append(f"{filename}")
        print(' '.join(output))
    else:
        print(f"{filename}: {result}")