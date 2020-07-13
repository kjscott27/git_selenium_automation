import getopt
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    input_url = get_script_options()
    browser = get_web_driver(input_url)


def get_web_driver(url):
    driver = webdriver.Firefox()
    driver.get(url)
    return driver


def get_element_with_wait(by, element, driver):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, element)))


def get_script_options():
    # -----------
    # long arg  short arg   value?
    # --help        -h        NO
    # --url         -u        YES
    # -----------
    short_options = "hu:"
    long_options = ["help", "url="]

    # argv is an array of arguments passed including the script i.e.
    # python test.py arg1 arg2 arg3 = python test.py arg1 arg2 arg3
    full_args = sys.argv

    # get rid of the first element
    args_excl_script = full_args[1:]  # get rid of the first element

    try:
        arguments, values = getopt.getopt(args_excl_script, short_options, long_options)
    except getopt.error as err:
        # output error and then close web driver
        print(str(err))
        sys.exit(2)
    return map_over_options(arguments)


def map_over_options(arguments):
    value = ""
    for current_arg, current_val in arguments:
        if current_arg in ("-h", "--help"):
            print("Options:")
            print("-h (--help): prints this message")
            print("-u (--url): passes a URL to the script for the web driver (this should be a github PR diff page)")
            print("Usage:")
            print("main.py --url \"someUrlGoesHere\"")
            sys.exit(2)
        elif current_arg in ("-u", "--url"):
            print("Passed URL is: ", current_val)
            value = current_val
    return value


if __name__ == "__main__":
    main()
