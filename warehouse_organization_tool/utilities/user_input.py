class UserInput:
  def __init__(self):
    pass

  @staticmethod
  def get_and_validate_input():
    valid_responses = ['S','R','I','A','O','E','Y','N']
    response = input("> ").upper()
    while True:
      if not response in valid_responses:
        print("Response not valid")
        response = input("> ").upper()
        continue
      break
    return response

