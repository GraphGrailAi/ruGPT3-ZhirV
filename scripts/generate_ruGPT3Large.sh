#! /bin/bash


python generate_transformers.py \
    --model_type=gpt2 \
    --model_name_or_path=sberbank-ai/rugpt3large_based_on_gpt2 \
    --k=100 \
    --p=0.9 \


# python generate_transformers.py --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3large_based_on_gpt2 --k=100 --p=0.9
# python generate_transformers.py --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3large_based_on_gpt2 --k=200 --p=0.9 --length=100 --num_return_sequences=2

# Модель эссе
# python generate_transformers.py --model_type=gpt2 --model_name_or_path=checkpoints_1 --k=500 --p=0.9 --length=100 --num_return_sequences=2


# Модель Жириновский
# python generate_transformers.py --model_type=gpt2 --model_name_or_path=checkpoint-1000 --k=100 --p=0.9 --length=200 --num_return_sequences=3

# python generate_transformers.py --model_type=gpt2 --model_name_or_path=checkpoint-1500 --k=100 --p=0.9 --length=200 --num_return_sequences=3

# python generate_transformers.py --model_type=gpt2 --model_name_or_path=checkpoint-3000 --k=100 --p=0.9 --length=200 --num_return_sequences=3

