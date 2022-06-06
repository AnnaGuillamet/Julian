import yaml
import click
import farm as f
import time

@click.command()
@click.option("-c","--configuration", default="julian.yaml", type = click.Path("rb"), help="Configuration")
def get_config(configuration):        
    with open(configuration) as f:
        cfg = yaml.load(f, Loader = yaml.FullLoader)
        api = cfg["telegram"]["token"]
        chatid = cfg["telegram"]["chat_id"]
        f.close()
    return cfg
bool = 0

if __name__ == '__main__':
    if bool == 0:
        print('--Start Sensors--')
        configuration = get_config.main(standalone_mode=False)
        print('--Configuration: OK--') 
        bool = 1
            
    farm = f.Farm(configuration)
    print ('Execució Programa OK')
    
    while 1:
        time.sleep(5)
