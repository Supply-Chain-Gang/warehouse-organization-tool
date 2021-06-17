class UserInput:
  """this class contains funcitonality to validate user input.
  """
  def __init__(self):
    pass

  @staticmethod
  def get_and_validate_input():
    """this class gets user input and returns valid input.

    Returns:
        [string]: returns valid user input, which will be one letter.
    """
    valid_responses = ['S','R','I','A','O','E','Y','N','H']
    response = input("> ").upper()
    while True:
      if not response in valid_responses:
        print("Response not valid")
        response = input("> ").upper()
        continue
      break
    return response

