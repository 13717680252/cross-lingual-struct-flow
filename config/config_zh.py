
params_markov={
    "couple_layers": 8,
    "cell_layers": 1,
    "valid_nepoch": 1,
    "epochs": 50,
    "batch_size": 32,
    "emb_dir": "fastText_data",
    "train_file": "ud-treebanks-v2.2/UD_Chinese-GSD/zh_gsd-ud-train.conllu",
    "val_file": "ud-treebanks-v2.2/UD_Chinese-GSD/zh_gsd-ud-dev.conllu",
    "test_file": "ud-treebanks-v2.2/UD_Chinese-GSD/zh_gsd-ud-test.conllu",
    "vec_file": "fastText_data/wiki.zh.gsd.vec",
    "align_file": "multilingual_trans/alignment_matrices/zh.txt"
}

params_dmv={
    "couple_layers": 8,
    "cell_layers": 1,
    "valid_nepoch": 1,
    "epochs": 50,
    "batch_size": 32,
    "emb_dir": "fastText_data",
    "train_file": "ud-treebanks-v2.2/UD_Chinese-GSD/zh_gsd-ud-train.conllu",
    "val_file": "ud-treebanks-v2.2/UD_Chinese-GSD/zh_gsd-ud-dev.conllu",
    "test_file": "ud-treebanks-v2.2/UD_Chinese-GSD/zh_gsd-ud-test.conllu",
    "vec_file": "fastText_data/wiki.zh.gsd.vec",
    "align_file": "multilingual_trans/alignment_matrices/zh.txt"
}