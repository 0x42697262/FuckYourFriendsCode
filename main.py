import random, os, sys

WHITESPACE_CHARS = [
        '\u00A0',   # No-Break Space
        '\u1680',   # Ogham Space Mark
        '\u2000',   # En Quad
        '\u2001',   # Em Quad
        '\u2004',   # Three-Per-Em Space
        '\u2005',   # Four-Per-Em Space
        '\u2006',   # Six-Per-Em Space
        '\u2007',   # Figure Space
        '\u2008',   # Punctuation Space
        '\u2009',   # Thin Space
        '\u200A',   # Hair Space
        '\u202F',   # Narrow No-Break Space
        '\u205F',   # Medium Mathematical Space
        '\u3000',   # Ideographic Space   
        ]

ZERO_WIDTH_CHARS = [
        '\u17B4',   # Khmer Vowel Inherent AQ
        '\u17B5',   # Khmer Vowel Inherent AA
        '\u200B',   # Space
        '\u200C',   # Non-Joiner
        '\u200D',   # Joiner
        '\uFEFF',   # No-Break Space
        '\u034F',   # Joiner, Non-Spacing
        '\u2060',   # Word Joiner
        ]



def generate_random_zwsp() -> str:
    """This uses unicode q blocks"""

    start_range     = 0xe0000
    end_range       = 0xe00ff

    return chr(random.randint(start_range, end_range))

def get_file_size(filename) -> int:
    file_size   = os.path.getsize(filename)

    return file_size

def modify_file(filename, ratio: int = 25):
    with open(filename, 'r') as file:
        content = file.read()

    file_size           = get_file_size(filename)
    modified_content    = content
    
    ratio   = int((ratio/100) * file_size)
    for _ in range(ratio):
        position            = random.randint(0, file_size)
        zwsp                = generate_random_zwsp()
        modified_content    = modified_content[:position] + zwsp + modified_content[position:]

    with open(filename, 'w') as file:
        file.write(modified_content)

    return modified_content


def main(args):
    if len(args) == 1:
        filename    = args[0]

        print(f"File size: {get_file_size(filename)} bytes")
        modify_file(filename)

        print('New file size:', get_file_size(filename), 'bytes')

    elif len(args) > 1:
        filename    = args[0]
        ratio = int(args[1])

        print(f"File size: {get_file_size(filename)} bytes")
        modify_file(filename, ratio)

        print('New file size:', get_file_size(filename), 'bytes')

    else:
        print("Run: python main.py <filename> <ratio in percent>")




if __name__ == "__main__":
    main(sys.argv[1:])
