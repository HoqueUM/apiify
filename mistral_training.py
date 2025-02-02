# import pandas as pd

# df = pd.read_json("hf://datasets/MBZUAI/Web2Code/Web2Code_samples.json")

# df_train=df.sample(frac=0.995,random_state=200)
# df_eval=df.drop(df_train.index)

# df_train.to_json("ultrachat_chunk_train.jsonl", orient="records", lines=True)
# df_eval.to_json("ultrachat_chunk_eval.jsonl", orient="records", lines=True)

from mistralai import Mistral
import os

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

ultrachat_chunk_train = client.files.upload(file={
    "file_name": "ultrachat_chunk_train.jsonl",
    "content": open("ultrachat_chunk_train.jsonl", "rb"),
})
ultrachat_chunk_eval = client.files.upload(file={
    "file_name": "ultrachat_chunk_eval.jsonl",
    "content": open("ultrachat_chunk_eval.jsonl", "rb"),
})