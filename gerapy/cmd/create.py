import os

from gerapy.libs.get_content import get_content


def create(args):
    try:
        os.mkdir(args)
        os.chdir(args)
        with open('gerapy.cfg', 'w') as f:
            f.write(get_content('/gerapy.cfg'))
            f.close()
    except Exception:
        print('create project failed')
        return False
    print('create', args, 'successfully')
    return True