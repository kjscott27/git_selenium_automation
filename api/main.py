import getopt
import sys
from helpers import print_help
from github import Github


def main():
  value = get_script_options()


def get_script_options():
  # -----------
  # long arg  short arg   value?
  # --help        -h        NO
  # --password    -p        YES
  # --save        -s        NO
  # --token       -t        YES
  # --username    -u        YES
  # -----------
  short_options = "hu:p:t:s"
  long_options = ["help", "username=", "password=", "token=", "save"]

  # argv is an array of arguments passed including the script i.e.
  # python test.py arg1 arg2 arg3 = python test.py arg1 arg2 arg3
  full_args = sys.argv

  # get rid of the first element
  args_excl_script = full_args[1:]  # get rid of the first element

  try:
    arguments, values = getopt.getopt(
      args_excl_script, short_options, long_options)
  except getopt.error as err:
    # output error and then close web driver
    print(str(err))
    sys.exit(2)
  return map_over_options(arguments)


def map_over_options(arguments):
  print(arguments)
  token = ""
  username = ""
  password = ""
  persistToken = False
  for current_arg, current_val in arguments:
      if current_arg in ("-h", "--help"):
        print_help()
        sys.exit(2)
      elif current_arg in ("-u", "--username"):
        print("Passed URL is: ", current_val)
        value = current_val
      elif current_arg in ("-p", "--password"):
        print("")
      elif current_arg in ("-t", "--username"):
        print("")
      elif current_arg in ("-s", "--save"):
        print("")
  return value


if __name__ == "__main__":
    main()
