# Extract staticstics from rtc-worker log file
# Usage: python worker-log.py rtc-worker.log user_id

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'))
parser.add_argument('user_id', nargs='?')

def find_recv_remb(line):
  start  = line.find('report: ')
  end = line.find(',', start)
  return int(line[start + 8:end])

def find_send_remb(line):
  start  = line.find('sending REMB: ')
  end = line.find(',', start)
  return int(line[start + 14:end])
    
def find_bitrate(line):
  start  = line.find('bitrate: ')
  end = line.find(',', start)
  return int(line[start + 9:end])
    
args = parser.parse_args()

if args.input_file == None:
  print 'Please specify input file'
  sys.exit(0)

if args.user_id == None:
  print 'Please specify user id'
  sys.exit(0)

out_file = open(args.user_id + '.csv', 'w')

file = args.input_file.readlines()
recv_remb_count = 0
recv_remb_sum = 0
send_remb_count = 0
send_remb_sum = 0
bitrate_sum = 0
bitrate_count = 0
nack_count = 0
for line in file:
  if args.user_id in line and 'report' in line:
    remb = find_recv_remb(line)
    if remb > -1:
      out_file.write(str(remb))
      out_file.write(',\n')
      recv_remb_count += 1
      recv_remb_sum += remb
    bitrate = find_bitrate(line)
    if bitrate > 0:
      bitrate_count += 1
      bitrate_sum += bitrate
  elif args.user_id in line and 'sending REMB:' in line:
    remb = find_send_remb(line)
    send_remb_count += 1
    send_remb_sum += remb
  elif args.user_id in line and 'NACK ssrc:' in line:
    nack_count += 1
  elif args.user_id in line and (('connect' in line) or ('Disabling' in line)):
    print line.rstrip()

out_file.close()
args.input_file.close()

print 'Received REMB messages:', recv_remb_count
if recv_remb_count > 0:
  print 'Average received REMB:', recv_remb_sum/recv_remb_count, '[bps]'

print 'Sent REMB messages:', send_remb_count
if send_remb_count > 0:
  print 'Average sent REMB:', send_remb_sum/send_remb_count, '[bps]'

print 'Recv bitrate count:', bitrate_count
if bitrate_count > 0:
  print 'Average received bitrate:', bitrate_sum/bitrate_count, '[bps]'

print 'NACK mesages:', nack_count
