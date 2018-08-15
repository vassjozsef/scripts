import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'))
parser.add_argument('user_id', nargs='?')

def find_report(line):
  start  = line.find('report: ')
  end = line.find(',', start)
  return line[start + 8:end]
    
args = parser.parse_args()

if args.input_file == None:
  print 'Please specify input file'
  sys.exit(0)

if args.user_id == None:
  print 'Please specify user id'
  sys.exit(0)

out_file = open(args.user_id + '.csv', 'w')

file = args.input_file.readlines()
count = 0
for line in file:
  if args.user_id in line and 'report' in line:
    report = find_report(line)
    out_file.write(report)
    out_file.write(',')
    count = count + 1

out_file.close()
args.input_file.close()

print count

