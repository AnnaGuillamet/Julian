''' Julian
Usage:
    Julian control
    Julian --help
Julian is a sowfware for xxxxx
'''
import yaml, json
import time
import click
import farm as f


@click.command()
@click.option("-c","--configuration", default="julian.yaml", type = click.Path("rb"), help="Configuration")
def get_config(configuration):        
    with open(configuration) as f:
        cfg = yaml.load(f, Loader = yaml.FullLoader)
        api = cfg["telegram"]["token"]
        chatid = cfg["telegram"]["chat_id"]
        f.close()
    #print(cfg)
    return cfg

if __name__ == '__main__':
    configuration = get_config.main(standalone_mode=False)
    print('Configuration OK')
    farm = f.Farm(configuration)
    print ('Execució Programa OK')

    while 1:
       time.sleep(5)