#!/usr/bin/env python
import click
import random

VERSION = '1.0.0-442'

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

def _welcome_message():
    print('ChangeTimeToNow(tm) v{0}'.format(VERSION))
    print('')

def _prompt_confirm(force):
    print('ChangeTimeToNow will change time to NOW!')
    if force:
	print('forced...')
	return

    click.confirm('are you sure you want to continue?', abort=True)

@click.command()
@click.option('--force', is_flag=True, help='force time change to now')
def main(force):
    _welcome_message()
    _prompt_confirm(force)
    funcs = (_success, _failure, _warning)

    random.choice(funcs)()

if __name__ == '__main__':
    main()
