import argparse
import os
import shutil


FILE_DIR = os.path.dirname(__file__)
ARGS = None
HOME = os.environ['HOME']

FILES = ['.bashrc','.vimrc', '.bash_aliases']


def setup():
    for fil in FILES:
        source =        os.path.join(FILE_DIR,fil)
        destination =   os.path.join(HOME,fil)
        shutil.copyfile(source, destination)
    print("Make sure to source .bashrc")
    print(f"command to run: source {os.path.join(HOME,'.bashrc')}")

    


def fetch():
    for fil in FILES:
        source =        os.path.join(HOME,fil)
        destination =   os.path.join(FILE_DIR,fil)
        shutil.copyfile(source, destination)
    print("files successfully updated")





if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Manager for setupNdots repo')
    parser.add_argument('action', nargs='?', choices=('setup','fetch'))
    # parser.add_argument('server',action='store_true') # possible argument to use when on a server though not sure exactly what should differ

    ARGS=parser.parse_args() # Parse commandline args by default
    if ARGS.action == None:
        print('An action needs to be specified')
    # Perform specified action
    elif ARGS.action == 'setup': setup()
    elif ARGS.action == 'fetch': fetch()

