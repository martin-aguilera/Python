"""
SE EJECUTA EN TERMINAL UTILIZA
python request.py -t [URL]
"""

import requests, argparse, os
from time import sleep

os.system("cls")
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="objetivo")
parser = parser.parse_args()


def main():
    if parser.target:
        try:
            objetivo = requests.get(url=parser.target)
            header = dict(objetivo.headers)
            for x in header:
                print("\n", x + " : " + header[x], "\n")
                sleep(0.5)
        except:
            print("\n~ERROR: --no se puede conectar--\n")
    else:
        print("\n~ERROR: --objetivo mal escrito--\n")


if __name__ == "__main__":
    main()
