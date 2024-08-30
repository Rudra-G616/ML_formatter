# Read the content of the file
def code_to_string(file_path):   
    
    with open(file_path, 'r') as file:
        rst_code = file.read()
    
    # Convert the multi-line string into a single-line string
    single_line_rst_code = rst_code.replace('\n', '\n')
    
    # Return the single-line string
    return single_line_rst_code
