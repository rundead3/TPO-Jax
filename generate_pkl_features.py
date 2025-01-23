# Copyright 2021 Beijing DP Technology Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Get preprocessed features (features.pkl) from input fasta files."""

import os
import pathlib
import pickle
import random
import sys
import time

from absl import app
from absl import flags
from absl import logging
from multiprocessing import Pool
from functools import partial

from unifold.data import pipeline
from unifold.data import templates
from unifold.inference.inference_pipeline import generate_pkl_features_from_fasta

#### USER CONFIGURATION ####

# Note: If your databases and toolkits were configured directly using the scripts 
# provided by Uni-Fold, the following code is directly useful. If not, you need 
# to customize your own paths of the downloaded databases and toolkits. 
# See README.md for more details.

# Define flags.
flags.DEFINE_string('fasta_dir', None, 
                    'Paths to FASTA files, each containing one sequence. '
                    'Paths should be separated by commas. All FASTA paths '
                    'must have a unique basename as the basename is used to '
                    'name the output directories for each prediction.')
flags.DEFINE_string('output_dir', None,
                    'Path to a directory that will store the results.')
flags.DEFINE_string('data_dir', None,
                    'Path to directory of supporting data.')
# External tools paths.
flags.DEFINE_string('jackhmmer_binary_path', 'jackhmmer',
                    'Path to the JackHMMER executable.')
flags.DEFINE_string('hhblits_binary_path', 'hhblits',
                    'Path to the HHblits executable.')
flags.DEFINE_string('hhsearch_binary_path', 'hhsearch',
                    'Path to the HHsearch executable.')
flags.DEFINE_string('kalign_binary_path', 'kalign',
                    'Path to the Kalign executable.')
# Databases paths.
flags.DEFINE_string('uniref90_database_path', None,
                    'Path to the Uniref90 database for use by JackHMMER.')
flags.DEFINE_string('mgnify_database_path', None,
                    'Path to the MGnify database for use by JackHMMER.')
flags.DEFINE_string('bfd_database_path', None, 
                    'Path to the BFD database for use by HHblits.')
flags.DEFINE_string('uniclust30_database_path', None,
                    'Path to the Uniclust30 database for use by HHblits.')
flags.DEFINE_string('pdb70_database_path', None,
                    'Path to the PDB70 database for use by HHsearch.')
flags.DEFINE_string('template_mmcif_dir', None,
                    'Path to a directory with template mmCIF structures, '
                    'each named <pdb_id>.cif')
flags.DEFINE_string('obsolete_pdbs_path', None,
                    'Path to file containing a mapping from obsolete PDB IDs '
                    'to the PDB IDs of their replacements.')
# Other configs.
flags.DEFINE_string('max_template_date', '2020-4-30',
                    'Maximum template release date to consider. Important '
                    'if folding historical test sets.')
flags.DEFINE_integer('random_seed', None,
                     'The random seed for the data pipeline. By default, this '
                     'is randomly generated. Note that even if this is set, '
                     'Uni-Fold may still not be deterministic, because '
                     'processes like GPU inference are nondeterministic.')
flags.DEFINE_integer('num_workers', 1, 'Number of parallel workers.')

flags.DEFINE_string('small_bfd_database_path', None,
                   'Path to the Small BFD database for use by HHblits.')
FLAGS = flags.FLAGS

MAX_TEMPLATE_HITS = 20


def get_fasta_paths(fasta_dir: str):
  fasta_paths = []
  for root, dirs, files in os.walk(fasta_dir):
    for fname in files:
      # consider .fasta / .fas / .fa files
      if fname.endswith(".fasta") or fname.endswith(".fas") or fname.endswith(".fa"):
        fasta_paths.append(os.path.join(root, fname))
  return fasta_paths


def main(argv):
    if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')

    # Only load the two databases we need
    uniclust30_database_path = os.path.join(
        FLAGS.data_dir, 'uniclust30', 'UniRef30_2020_06/UniRef30_2020_06') \
        if FLAGS.uniclust30_database_path is None \
        else FLAGS.uniclust30_database_path

    small_bfd_database_path = os.path.join(
        FLAGS.data_dir, 'small_bfd', 'bfd-first_non_consensus_sequences.fasta') \
        if FLAGS.small_bfd_database_path is None \
        else FLAGS.small_bfd_database_path

    # get fasta paths and check for duplicated names
    fasta_paths = get_fasta_paths(FLAGS.fasta_dir)
    fasta_names = [pathlib.Path(p).stem for p in fasta_paths]
    if len(fasta_names) != len(set(fasta_names)):
        raise ValueError('All FASTA paths must have a unique basename.')

    # Set up minimal data pipeline
    data_pipeline = pipeline.DataPipeline(
        jackhmmer_binary_path=FLAGS.jackhmmer_binary_path,
        hhblits_binary_path=FLAGS.hhblits_binary_path,
        hhsearch_binary_path=FLAGS.hhsearch_binary_path,
        uniclust30_database_path=uniclust30_database_path,
        use_small_bfd=True,
        small_bfd_database_path=small_bfd_database_path,
        uniref90_database_path=None,
        mgnify_database_path=None,
        bfd_database_path=None,
        pdb70_database_path=None,
        template_featurizer=None)

    # Predict structure by pool
    par = partial(generate_pkl_features_from_fasta,
                 output_dir=FLAGS.output_dir,
                 data_pipeline=data_pipeline)
    pool = Pool(FLAGS.num_workers)
    pool.starmap(par, list(zip(fasta_paths, fasta_names)))
    pool.close()
    pool.join()


if __name__ == '__main__':
  flags.mark_flags_as_required([
      'fasta_dir',
      'output_dir',
      'data_dir'
  ])

  app.run(main)
