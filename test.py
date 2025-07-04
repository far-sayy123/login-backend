import colorama # sabko import karne ke liye
from colorama import Fore, Back, Style
from tqdm import tqdm
import time



print(Fore.RED + Style.BRIGHT + "Hello")



for i in tqdm(range(1, 100)):
    time.sleep(0.2)