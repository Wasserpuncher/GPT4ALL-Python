import gpt4all

gpt = gpt4all.GPT4All("ggml-v3-13b-hermes-q5_1")

msgs = [{"role": "user", "content": "Program me a website"}] 

gpt.chat.completion(msgs)
