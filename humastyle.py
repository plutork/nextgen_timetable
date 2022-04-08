from os import system, name

def tittle():
    if name == 'nt': # windows
        system('cls')
    else:            # mac & linux
        system('clear')
    print("\n   -=| nextgen coffeetime |=-\n")

if name == 'nt': #windows
  import colorama
  from colorama import Fore, Back, Style
  colorama.init()
  def gprint(text):
      print(Fore.GREEN + str(text))
      print(Style.RESET_ALL, end = "")
  
  def rprint(text):
      print(Fore.RED + str(text))
      print(Style.RESET_ALL, end = "")
  
  def yprint(text):
      print(Fore.YELLOW + str(text))
      print(Style.RESET_ALL, end = "")
  
  def cprint(text):
      print(Fore.CYAN + str(text))
      print(Style.RESET_ALL, end = "")
  
  def mprint(text):
      print(Fore.MAGENTA + str(text))
      print(Style.RESET_ALL, end = "")    

else: # mac & linux
  def gprint(text):
    print("\033[32m {}\033[0m" .format(text))

  def rprint(text):
    print("\033[31m {}\033[0m" .format(text))
  
  def yprint(text):
    print("\033[33m {}\033[0m" .format(text))

  def cprint(text):
    print("\033[34m {}\033[0m" .format(text))

  def mprint(text):
    print("\033[35m {}\033[0m" .format(text))

def view_schedule():
  wday = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
  print("".ljust(10), 
        wday[0].ljust(6), 
        wday[1].ljust(6), 
        wday[2].ljust(6), 
        wday[3].ljust(6), 
        wday[4].ljust(6), 
        wday[5].ljust(6), 
        wday[6].ljust(6))
  print("Officer")
  print("Cook")
  print("Barista")
  print("Support")
  print("Support2")
  print("Officer")
  print("Cook")
  print("Barista")

 
if __name__ == "__main__":
  print('humanstyle test funtions:')
  gprint("COMPLETE")
  rprint("ERROR")
  yprint("WARNING")
  cprint("INFO")
  mprint("SYSTEM")

  view_schedule()
  