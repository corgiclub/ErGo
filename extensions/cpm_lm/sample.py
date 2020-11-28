import tensorflow_hub as hub
import tensorflow as tf
import os

from gpt2_tokenizer import GPT2Tokenizer

BASE_PATH = "/ErGo/extensions/cpm_lm"
def process_relpath(relpath): return os.path.join(BASE_PATH, relpath)


tokenizer = GPT2Tokenizer(
    process_relpath('CPM-Generate/bpe_3w_new/vocab.json'),
    process_relpath('CPM-Generate/bpe_3w_new/merges.txt'),
    model_file=process_relpath('CPM-Generate/bpe_3w_new/chinese_vocab.model')
)

gpt = hub.load(process_relpath('cpm-lm-tf2_v2/'))


def sample(sentence, tokenizer=tokenizer, gpt=gpt, number=1, length=20, top_p=0.9, temperature=0.9):
    """
    number: 输出句子个数
    length: 输出最大长度
    top_p: token的概率排在这以上才有效
    temperature: 温度
    """
    inputs = tf.constant([tokenizer.encode(sentence)] * number, dtype=tf.int64)
    length = tf.constant(length, dtype=tf.int64)
    ret = gpt.signatures['serving_default'](
        inp=inputs,
        length=length,
        top_p=tf.constant(top_p, tf.float32),
        temperature=tf.constant(temperature, tf.float32)
    )['output_0']
    return [
        tokenizer.decode(s).replace(' ', '')
        for s in ret.numpy()
    ]


if __name__ == "__main__":
    ret = sample(tokenizer, gpt, '默写英文：\n狗dog\n猫cat\n鸟',
                 3, 10, top_p=0.9, temperature=0.9)
    for x in ret:
        print(x)
        print('-' * 20)
