def print_help():
  print('''\
  -----------
  long arg  short arg   value?
  --help        -h        NO
  --password    -p        YES
  --save        -s        NO
  --token       -t        YES
  --username    -u        YES
  -----------
   
  Options:
  -----------
  -h (--help): prints this message and ends the program
  -u (--username): your GitHub USERNAME (this will not be saved locally)
  -p (--password): your GitHub PASSWORD (this will not be saved locally)
  -t (--token): a GitHub personal token (this can be saved locally optionally)
  -----------

  Usage:
  -----------
  main.py --username \"yourGithubUSERNAME\" --password \"yourGithubPASSWORD\"
  main.py --token \"yourGithubPERSONALTOKEN\" --password \"someUrlGoesHere\"
  -----------
  END
   ''')