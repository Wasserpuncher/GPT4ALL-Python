import gpt4all

gpt = gpt4all.GPT4All("ggml-v3-13b-hermes-q5_1")

msgs = [{"role": "user", "content": "Create a recipe for banana frappunchino"}] 

gpt.chat.completion(msgs)