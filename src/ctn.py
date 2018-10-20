import sys
import random

def _success():
    print('INFO: change time to now completed successfully!')
    print('INFO: time IS now')

def _failure():
    print('ERR: change time to now failed')
    print('ERR: time is NOT now!!')

def _warning():
    import traceback

    try:
        raise Exception('Unknown exception caught')
    except:
        traceback.print_exc()
        print('ERR: change time to now failed unexpectedly')
        print('ERR: Warning: Time might not be now!!')

def main():
    funcs = (_success, _failure, _warning)

    random.choice(funcs)()

if __name__ == '__main__':
    sys.exit(main())
