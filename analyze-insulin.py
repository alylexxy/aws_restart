import re


def clean_file_with_regex(pattern, input_file, output_file):
    with open(input_file, 'r') as inp:
        with open(output_file, 'w') as outp:
            content = inp.read()
            mod_content = re.sub(pattern, '', content)
            outp.write(mod_content)
    print(f'I wrote the resulting string in the file: {output_file}')
    print(f'Length of modified content is: {len(mod_content)}')


def cut_part_of_string(input_file, output_file, start, finish):
    with open(input_file, 'r') as inp:
        with open(output_file, 'w') as outp:
            string = inp.read()
            string_part = string[start-1:finish]
            outp.write(string_part)
    print(f'Length of cut string is : {len(string_part)}')


patterns_list = [r'[A-Z]', r'//', r'\d+', r'\n', r'\s']

# join the patterns in the list with or operand (|) in regex and save them in a string
combined_pattern = '|'.join(patterns_list)

clean_file_with_regex(combined_pattern, 'preproinsulin-seq.txt', 'preproinsulin-clean.txt')

cut_part_of_string('preproinsulin-clean.txt', 'lsinsulin-seq-clean.txt', 1, 24)
cut_part_of_string('preproinsulin-clean.txt', 'binsulin-seq-clean.txt', 25, 54)
cut_part_of_string('preproinsulin-clean.txt', 'cinsulin-seq-clean.txt', 55, 89)
cut_part_of_string('preproinsulin-clean.txt', 'ainsulin-seq-clean.txt', 90, 110)
