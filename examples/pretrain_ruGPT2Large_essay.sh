#! /bin/bash

NUM_GPUS_PER_WORKER=1

now=$(date +"%Y_%m_%d_%H_%I_%S")
host=$(hostname)

mpirun --np ${NUM_GPUS_PER_WORKER} python pretrain_transformers.py \
    --output_dir=/home/jovyan/gpt2_large_bbpe_v50/essays/checkpoints_"${now}"_"${host}" \
    --model_type=gpt2 \
    --model_name_or_path=/home/jovyan/gpt2_large_bbpe_v50 \
    --do_train \
    --train_data_file=/home/jovyan/data/all_essays.txt \
    --do_eval \
    --eval_data_file=/home/jovyan/data/valid_essays.txt \
    --fp16 \
    --num_train_epochs 10 \
    --overwrite_cache \
    --block_size=1024 \
    --per_gpu_train_batch_size 1 \
    --gradient_accumulation_steps 8 \

# sberbank-ai/rugpt3large_based_on_gpt2
# --np 1 python pretrain_transformers.py --output_dir=data/gpt3_large_hf/checkpoints_1 --model_type=gpt2 --model_name_or_path=data/gpt3_large_hf --do_train --train_data_file=data/all_essays.jsonl --do_eval --eval_data_file=data/valid_essays.jsonl --fp16 --num_train_epochs 10 --overwrite_cache --block_size=1024 --per_gpu_train_batch_size 1 --gradient_accumulation_steps 8

# no --fp16
# python pretrain_transformers.py --output_dir=data/gpt3_large_hf/checkpoints_1 --model_type=gpt2 --model_name_or_path=data/gpt3_large_hf --do_train --train_data_file=data/all_essays.jsonl --do_eval --eval_data_file=data/valid_essays.jsonl --num_train_epochs 10 --overwrite_cache --block_size=1024 --per_gpu_train_batch_size 1 --gradient_accumulation_steps 8


# for Google Colab https://colab.research.google.com/drive/1ze0fKjQN3JbGMlW3QdlAXTq-HlZwmyyw#scrollTo=G35UxKXEn6dM
# !python pretrain_transformers.py --output_dir=/content/ru-gpts/checkpoints_1 --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3large_based_on_gpt2 --do_train --train_data_file=data/all_essays.jsonl --do_eval --eval_data_file=data/valid_essays.jsonl --num_train_epochs 10 --overwrite_cache --block_size=1024 --per_gpu_train_batch_size 1 --gradient_accumulation_steps 8