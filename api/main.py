import getopt
import sys
from helpers import print_help
from github import Github


def main():
  token, username, password = get_script_options()
  print(token, username, password)


def get_script_options():
  short_options = "hu:p:t:s"
  long_options = ["help", "username=", "password=", "token=", "save"]

  # argv is an array of arguments passed including the script i.e.
  # python test.py arg1 arg2 arg3 = python test.py arg1 arg2 arg3
  full_args = sys.argv

  # get rid of the first element
  # (it isn't useful in this scenario because we dont need the script itself)
  args_excl_script = full_args[1:]

  try:
    arguments, _ = getopt.getopt(
      args_excl_script, short_options, long_options)
  except getopt.error as err:
    # output error and then close web driver
    print(str(err))
    sys.exit(2)
  return map_over_options(arguments)


def map_over_options(arguments):
  token = ""
  username = ""
  password = ""
  if len(arguments) > 0:  # if we have arguments available
    for current_arg, current_val in arguments:
        if current_arg in ("-h", "--help"):
          print_help()
          sys.exit(2)
        elif current_arg in ("-u", "--username"):
          print(current_val)
        elif current_arg in ("-p", "--password"):
          print(current_val)
        elif current_arg in ("-t", "--username"):
          print(current_val)
        elif current_arg in ("-s", "--save"):
          print("Token saved")
  else:  # if the user didn't provide arguments
    # we'll do the journey here for checking if we have a stored token locally
    # if so use that and continue, else print a helpful message like the help message
    print('no args')
  return token, username, password


if __name__ == "__main__":
    main()
