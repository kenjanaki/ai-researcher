import re

def split_thoughts(text):
    think_match = re.search(r"<think>(.*?)</think>", text, re.DOTALL)
    thinking = think_match.group(1).strip() if think_match else None
    answer = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    return thinking, answer
