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
    print('--Start Project Julian--')
    configuration = get_config.main(standalone_mode=False)
    print('--Configuration: OK--') 
    farm = f.Farm(configuration)

