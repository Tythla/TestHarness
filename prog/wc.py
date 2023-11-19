import argparse

def word_count(filenames, flags=None):
    results = {}

    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

            result = {}
            if not flags or 'l' in flags:
                result['lines'] = num_lines
            if not flags or 'w' in flags:
                result['words'] = num_words
            if not flags or 'c' in flags:
                result['chars'] = num_chars

            results[filename] = result

        except FileNotFoundError:
            results[filename] = "File not found."

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
    print(f"Results for {filename}:")
    for key, value in result.items():
        print(f"  {key}: {value}")
