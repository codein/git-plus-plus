from optparse import OptionParser
import subprocess
import os


def exporter (option, opt_str, value, parser):
	cmd = subprocess.Popen('git status --porcelain', shell=True, stdout=subprocess.PIPE)
	i = 0
	exports = 'export'
	for line in cmd.stdout:
		i += 1
		status = line.split(' ')
		filename = status.pop()
		export = ' e%d=%s' % (i,filename.strip())
		exports += export

	print exports

def printer (option, opt_str, value, parser):
	cmd = subprocess.Popen('git status --porcelain', shell=True, stdout=subprocess.PIPE)
	i = 0
	for line in cmd.stdout:
		i += 1
		status = line.split(' ')
		filename = status.pop()
		export = ' e%d=%s' % (i,filename.strip())
		print export



parser = OptionParser()
parser.add_option("-p", "--print",
                  action="callback", callback=printer,
                  help="don't print status messages to stdout")
parser.add_option("-e", "--export",
                  action="callback", callback=exporter,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()