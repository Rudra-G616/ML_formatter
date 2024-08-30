import random
import re
# n_mistakes = random.randint(0,100)

# def introduce_rst_syntax_mistakes(rst_string, num_mistakes=n_mistakes):
#     # Split the string into lines for processing
#     lines = rst_string.split('\n')
#     cnt_mistakes = 0
    
#     def add_syntax_mistake(line):
#         # Introduce various types of syntax mistakes
#         if random.choice([True, False]) and re.match(r'^\s*[-*]\s', line):
#             # Misformat a bullet list item (remove the bullet)
#             cnt_mistakes += 1
#             return line.lstrip('-*').lstrip()
        
#         if random.choice([True, False]) and re.match(r'^\s*\d+\.\s', line):
#             # Misformat a numbered list item (remove the number)
#             cnt_mistakes += 1
#             return line.lstrip('0123456789.').lstrip()
        
#         if random.choice([True, False]) and line.strip().endswith(':'):
#             # Remove a colon from a directive
#             cnt_mistakes += 1
#             return line.rstrip(':')
        
#         if random.choice([True, False]) and line.strip().startswith('.. '):
#             # Misformat a directive by changing it to lowercase
#             cnt_mistakes += 1
#             return line.lower()
        
#         if random.choice([True, False]) and '::' in line:
#             # Remove one of the colons in literal block markers
#             cnt_mistakes += 1
#             return line.replace('::', ':', 1)
        
#         if random.choice([True, False]) and line.strip().endswith('_.'):
#             # Remove the underscore from a link
#             cnt_mistakes += 1
#             return line.rstrip('_') + '.'
        
#         if random.choice([True, False]) and re.match(r'^\s*[*]', line):
#             # Misformat a strong emphasis
#             cnt_mistakes += 1
#             return line.replace('**', '*', 1)  # Change bold to italic
        
#         return line  # Return line unchanged if no mistakes applied

#     # Introduce mistakes
#     for _ in range(num_mistakes):
#         line_number = random.randint(0, len(lines) - 1)
#         lines[line_number] = add_syntax_mistake(lines[line_number])

#     # Rejoin the lines into a single string
#     if cnt_mistakes != 0:
#         print(cnt_mistakes)
#     return '\n'.join(lines)

n_mistakes =100

def introduce_rst_syntax_mistakes(rst_string, num_mistakes=n_mistakes):
    # Split the string into lines for processing
    lines = rst_string.split('\n')
    cnt_mistakes = 0
    
    def add_syntax_mistake(line):
        nonlocal cnt_mistakes  # Declare cnt_mistakes as nonlocal
        # Introduce various types of syntax mistakes
        if random.choice([True, False]) and re.match(r'^\s*[-*]\s', line):
            # Misformat a bullet list item (remove the bullet)
            cnt_mistakes += 1
            return line.lstrip('-*').lstrip()
        
        if random.choice([True, False]) and re.match(r'^\s*\d+\.\s', line):
            # Misformat a numbered list item (remove the number)
            cnt_mistakes += 1
            return line.lstrip('0123456789.').lstrip()
        
        if random.choice([True, False]) and line.strip().endswith(':'):
            # Remove a colon from a directive
            cnt_mistakes += 1
            return line.rstrip(':')
        
        if random.choice([True, False]) and line.strip().startswith('.. '):
            # Misformat a directive by changing it to lowercase
            cnt_mistakes += 1
            return line.lower()
        
        if random.choice([True, False]) and '::' in line:
            # Remove one of the colons in literal block markers
            cnt_mistakes += 1
            return line.replace('::', ':', 1)
        
        if random.choice([True, False]) and line.strip().endswith('_.'):
            # Remove the underscore from a link
            cnt_mistakes += 1
            return line.rstrip('_') + '.'
        
        if random.choice([True, False]) and re.match(r'^\s*[*]', line):
            # Misformat a strong emphasis
            cnt_mistakes += 1
            return line.replace('**', '*', 1)  # Change bold to italic
        
        return line

    # Introduce mistakes
    for _ in range(num_mistakes):
        line_number = random.randint(0, len(lines) - 1)
        lines[line_number] = add_syntax_mistake(lines[line_number])

    # Rejoin the lines into a single string
    
    
    return '\n'.join(lines), cnt_mistakes

