#!/usr/bin/env python3

import argparse
import json
import os

DEFAULT_CONFIG_FILE = 'configs/base.json'
DEFAULT_DATA_DIRECTORY = '/home/ubuntu/data/'

def read_json(filename):
  contents = None
  with open(filename) as f:
    contents = f.read()
  return json.loads(contents)

def write_json(filename, config_dict):
  serialized = json.dumps(config_dict, indent=2)
  with open(filename, 'w') as f:
    f.write(serialized)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--speaker_dir', type=str, required=True,
                      help='Directory name for speaker training data (dirname or absolute)')
  args = parser.parse_args()

  print('Speaker directory: {}'.format(args.speaker_dir))

  configs = read_json(DEFAULT_CONFIG_FILE)

  speaker_dir = os.path.join(DEFAULT_DATA_DIRECTORY, args.speaker_dir)
  training_filename = os.path.join(speaker_dir, 'training.csv')
  validation_filename = os.path.join(speaker_dir, 'validation.csv')

  print('Training filename: {}'.format(training_filename))
  print('Validation filename: {}'.format(validation_filename))

  configs['data']['training_files'] = training_filename
  configs['data']['validation_files'] = validation_filename

  write_json(DEFAULT_CONFIG_FILE, configs)


if __name__ == '__main__':
  main()

