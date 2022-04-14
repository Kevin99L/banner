import pyfiglet
from random import choice
import subprocess as sp

def banner(bannerName):
    fonts = sp.getoutput("pyfiglet -l").split("\n")
    goodFonts = [1,4,5,8,9,11,17,19,24,26,27,29,31,36,37,38,41,42,46,49,52,
    64,72,73,74,75,76,78,80,81,83,86,87,89,90,91,93,96,102,103,105,106,118,
    120,122,123,127,128,137,149,166,172,202,206,210,237,238,239,240,252,267,268,269,270,273,284,290,293,308,310,316,320,325,329,330,332,334,339,352,
    354,362,364,385,386,414]
    index = choice(goodFonts)
    result = pyfiglet.figlet_format(bannerName,font=fonts[index])
    result2 = pyfiglet.figlet_format("Author  :  Kevin.L",font="term")
    print(result, " "*50+"[version 1.0]", "instagram : @kevindotl\n", result2,sep="\n")

if __name__ == "__main__":
    banner("ALI")