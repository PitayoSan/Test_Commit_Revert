


def add(raw_content):
  # Case 1: empty string
  if len(raw_content) == 0: return 0

  # Case 2: one or more arguments
  contents = raw_content.split(',')
  for element in contents:
    if not element.isnumeric():
      raise ValueError("only integers allowed - {}".format(element))

  numeric_contents = [int(number) for number in contents]
  return sum(numeric_contents)