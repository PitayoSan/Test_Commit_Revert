from re import split


def add(raw_content):

  # Case 1: empty string
  if len(raw_content) == 0: return 0

  current_delimiter = ',|\n'
  content = raw_content

  # Custom delimeter detection
  if len(raw_content) >= 3 and raw_content[1] == '\n':
    current_delimiter = raw_content[0]
    content = raw_content[2:]

  # Case 2: one or more arguments
  split_content = split(current_delimiter, content)
  for element in split_content:
    if not element.isnumeric():
      if '-' in element:
        raise ValueError("negatives not allowed - {}".format(element))
      raise ValueError("only integers allowed - {}".format(element))

  numeric_contents = [int(number) for number in split_content]
  return sum(numeric_contents)