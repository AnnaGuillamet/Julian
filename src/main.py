''' Julian

Usage:
    Julian control
    Julian --help
Julian is a sowfware for xxxxxxx
'''

from email.policy import default
import enclosure as e  #e.blablabla. Sempre agafara el arxiu __init__.py
from farm import Farm 

import click

@click.command()  ##Decorador
@click.option("-c","--configuration", default = "farm.cfg", type = click.Path("rb"), help="Configuration")
def main(configuration):
    print("Hello from Julian")
    sensor = e.Sensor()


if __name__=="__main__":
    main()
