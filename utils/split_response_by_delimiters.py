import re

def split_response_by_delimiters(text, delimiters):
    """
    Extracts substrings from 'text' that are enclosed within each pair of delimiters in 'delimiters'.

    :param text: The text to extract substrings from.
    :param delimiters: A list of tuples, each containing a pair of delimiters.
    :return: A list of extracted substrings.
    """
    extracted_strings = []

    for start_delim, end_delim in delimiters:
        # Create a regular expression pattern for each pair of delimiters
        pattern = re.escape(start_delim) + '(.*?)' + re.escape(end_delim)
        # Find all occurrences of the pattern
        matches = re.findall(pattern, text, re.DOTALL)
        extracted_strings.extend(matches)

    return extracted_strings

# Example usage
# text = "Hello $$$extract this$$$ and ```also this```"
# delimiters = [('$$$', '$$$'), ('```', '```')]
# extracted_strings = extract_strings(text, delimiters)
# extracted_strings
