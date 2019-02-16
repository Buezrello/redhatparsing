# redhatparsing
Project "Parsing" for RedHat interview

## Short testing
For your convenience, the project contains two text files, testfile1.txt and testfile2.txt

They can be used for searching a regular expression:
'[\w\.-]+@[\w\.-]+'

(email address)

Same regular expression can be used for searching pattern in command line string.

## Limitation
1. The script must be run with Python 2 only, because it used Python 2 specific methods, like raw_input
2. Text file(s) must contains ASCII text, the script does not understand non-ASCII characters or binary
3. Regular expression must be enclosed in double or single quotes:

-r 'regular expression'

--regex "regular expression"

Without quotes the script will not recognized the regex

## Using
Unzip directory with subdirectories

From the directory that contains myparsing.py file run

python myparsing.py -r REGEX -f list of files


For help and list of allowed flags run

python myparsing.py --help

### Comments for RedHat interviewer 
1. In order encapsulate difference in output formates OOP used
2. I used "composition" design pattern here
