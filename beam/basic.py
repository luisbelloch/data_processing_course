#!/usr/bin/env python

from __future__ import absolute_import

import argparse
import logging

import apache_beam as beam
from apache_beam.utils.pipeline_options import PipelineOptions
from apache_beam.utils.pipeline_options import SetupOptions

def run(argv=None):
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', dest='input') 
  parser.add_argument('--output', dest='output')

  known_args, pipeline_args = parser.parse_known_args(argv)
  pipeline_args.extend(['--runner=DirectRunner'])
  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = True
  p = beam.Pipeline(options=pipeline_options)

  print("Input:", known_args.input)
  print("Output:", known_args.output)

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.DEBUG)
  run()
