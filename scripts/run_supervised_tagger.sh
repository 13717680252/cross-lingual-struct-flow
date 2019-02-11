#! /bin/bash
#
# run_tagger.sh
# Copyright (C) 2019-02-11 Junxian <He>
#
# Distributed under terms of the MIT license.
#


python -u markov_flow_train.py \
        --lang en \
        --model nice \
        --mode supervised \
        --set_seed \
        --taskid $1