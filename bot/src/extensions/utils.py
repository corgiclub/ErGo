from enum import Enum
import cv2
import numpy as np


def regex_equal(keywords) -> str:
    return '|'.join(('^'+k+'$' for k in keywords))


class PicSource(str, Enum):
    Chat = 'chat'
    ChatRecord = 'chat_record'
    Pixiv = 'pixiv'
    Twitter = 'twitter'
    SauceNAO = 'saucenao'


class CQ(str, Enum):
    """
        已进行数据库适配的CQ消息段类型
    """
    Text = 'text'
    Face = 'face'
    Image = 'image'
    Record = 'record'
    Video = 'video'
    At = 'at'
    Poke = 'poke'
    Anonymous = 'anonymous'
    Share = 'share'
    Contact = 'contact'
    Location = 'location'
    Reply = 'reply'
    Xml = 'xml'
    Json = 'json'
    Music = 'music'         # 只发送，不做适配
    Forward = 'forward'     # 需要适配转发消息
    Node = 'node'           # 格式复杂


def get_img_phash(img):
    """
        Get the pHash value of the image, pHash : Perceptual hash algorithm(感知哈希算法)
        if Hamming_distance(pHashA, pHashB) <= 5, it means the two images is similar.

        :param img
        :return: pHash value
    """

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)                # 转为灰度图
    resize_gray_img = cv2.resize(gray_img, (32, 32))                # 缩放
    vis = cv2.dct(cv2.dct(resize_gray_img.astype(np.float32)))      # 二维离散余弦变换
    vis = vis[:8, :8]                                               # 取 DCT 结果的左上角
    vis: np.ndarray = (vis > vis.mean()) + 0                        # 大于均值的为1 小于均值的为0
    p_hash_str = ''.join(vis.flatten().astype(str))                 # 展平并连成串
    p_hash_byte = int(p_hash_str, 2)                                # 以二进制转化为数字
    return p_hash_byte


def ham_dist(a, b):
    """
        计算以 (二进制) 数字形式输入的汉明距离
    """
    return bin(a ^ b).count('1')


if __name__ == '__main__':
    
    pass

