#! /bin/bash
#
# run_parser.sh
# Copyright (C) 2019-02-11 Junxian <He>
#
# Distributed under terms of the MIT license.
#

python -u dmv_flow_train.py \
        --lang $1 \
        --mode unsupervised \
        --set_seed \
        --model nice \
        --prob_const 1. \
        --max_len 150 \
        --train_max_len 20 \
        --pos_emb_dim 300 \
        --proj_lr 0.001 \
        --prior_lr 0.01 \
        --freeze_pos_emb \
        --load_nice ./dump_models/dmv/en_supervised_wopos_nice_0_20.pt \
        --beta 0.1
