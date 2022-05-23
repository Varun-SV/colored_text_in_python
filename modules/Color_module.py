class COLOR:

  BOLD='\033[1m'
  ITALICS='\033[3m'
  UNDERLINE='\033[4m'

  DARK_GRAY='\033[30m'
  DARK_RED = '\033[31m'
  DARK_GREEN='\033[32m'
  DARK_YELLOW='\033[33m'
  DARK_BLUE='\033[34m'
  DARK_PURPLE='\033[35m'
  DARK_CYAN='\033[36m'
  DARK_WHITE='\033[37m'
  
  GRAY='\033[90m'
  RED = '\033[91m'
  GREEN='\033[92m'
  YELLOW='\033[93m'
  BLUE='\033[94m'
  PURPLE='\033[95m'
  CYAN='\033[96m'
  WHITE='\033[97m'
  
  LIGHT_GREY_HIGHLIGHT='\033[40m'
  LIGHT_RED_HIGHLIGHT='\033[41m'
  LIGHT_GREEN_HIGHLIGHT='\033[42m'
  LIGHT_YELLOW_HIGHLIGHT='\033[43m'
  LIGHT_BLUE_HIGHLIGHT='\033[44m'
  LIGHT_PURPLE_HIGHLIGHT='\033[45m'
  LIGHT_CYAN_HIGHLIGHT='\033[46m'
  LIGHT_WHITE_HIGHLIGHT='\033[47m'

  GREY_HIGHLIGHT='\033[100m'
  RED_HIGHLIGHT='\033[101m'
  GREEN_HIGHLIGHT='\033[102m'
  YELLOW_HIGHLIGHT='\033[103m'
  BLUE_HIGHLIGHT ='\033[104m'
  PURPLE_HIGHLIGHT='\033[105m'
  CYAN_HIGHLIGHT='\033[106m'
  WHITE_HIGHLIGHT='\033[107m'

  END ='\033[0m'

col={0:COLOR.END,
     1:COLOR.BOLD,
     2:COLOR.ITALICS,
     3:COLOR.UNDERLINE,
     4:COLOR.DARK_GRAY,
     5:COLOR.DARK_RED,
     6:COLOR.DARK_GREEN,
     7:COLOR.DARK_YELLOW,
     8:COLOR.DARK_BLUE,
     9:COLOR.DARK_PURPLE,
     10:COLOR.DARK_CYAN,
     11:COLOR.DARK_WHITE,
     12:COLOR.GRAY,
     13:COLOR.RED,
     14:COLOR.GREEN,
     15:COLOR.YELLOW,
     16:COLOR.BLUE,
     17:COLOR.PURPLE,
     18:COLOR.CYAN,
     19:COLOR.WHITE,
     20:COLOR.LIGHT_GREY_HIGHLIGHT,
     21:COLOR.LIGHT_RED_HIGHLIGHT,
     22:COLOR.LIGHT_GREEN_HIGHLIGHT,
     23:COLOR.LIGHT_YELLOW_HIGHLIGHT,
     24:COLOR.LIGHT_BLUE_HIGHLIGHT,
     25:COLOR.LIGHT_PURPLE_HIGHLIGHT,
     26:COLOR.LIGHT_CYAN_HIGHLIGHT,
     27:COLOR.LIGHT_WHITE_HIGHLIGHT,
     28:COLOR.GREY_HIGHLIGHT,
     29:COLOR.RED_HIGHLIGHT,
     30:COLOR.GREEN_HIGHLIGHT,
     31:COLOR.YELLOW_HIGHLIGHT,
     32:COLOR.BLUE_HIGHLIGHT,
     33:COLOR.PURPLE_HIGHLIGHT,
     34:COLOR.CYAN_HIGHLIGHT,
     35:COLOR.WHITE_HIGHLIGHT
     }
#function to make printing each stuff easy...
def prints(string,opt,ends):###Takes a string, a list of all the combination and the end delimiter and prints the combinations
  temp=""
  for i in opt:
    temp+=col[i%35]
  temp+=string
  print(temp+col[0],end=ends)
  
def text_return(string,opt,ends):###Takes a string, a list of all the combination and the end delimiter and prints the combinations
  temp=""
  for i in opt:
    temp+=col[i%35]
  temp+=string
  new_temp = str(temp+col[0]+ends)
  return new_temp
