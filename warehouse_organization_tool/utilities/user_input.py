class UserInput:
  def __init__(self):
    pass

  @staticmethod
  def get_and_validate_input():
    valid_initial_response = ['S','R','I','A','O','E']
    response = input("> ").upper()
    while True:
      if not response in valid_initial_response:
        print("Response not valid")
        response = input("> ").upper()
        continue
      break
    return response

