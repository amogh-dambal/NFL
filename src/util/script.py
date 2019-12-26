# utility functions
# to call bash scripts
from subprocess import call


def run(script, path='../scripts/'):
	call(path + script, shell=True)