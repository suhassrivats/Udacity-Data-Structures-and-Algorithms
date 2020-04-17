import sys
import heapq


def encoded_text(huffman_dict, data):
    huffcode = ''
    for c in data:
        huffcode += str(huffman_dict[c])

    return huffcode


def huffman_encoding(data):
    """
    More common bits = fewer bits
    Less common bits = more bits
    """
    huff = dict()
    global huffman_dict
    huffman_dict = {}


    # Take a string and determine the relevant frequencies of the characters
    for char in data:
        huff[char] = huff.get(char, 0) + 1

    # Transform the list into a heap tree structure
    heap = [[frequency, [symbol, '']] for symbol, frequency in huff.items()]
    heapq.heapify(heap)
    # print(heap)

    if len(heap) == 1:
        huffman_dict[heap[0][1][0]] = str(heap[0][0])
        # print(huffman_dict)
        huffcode = encoded_text(huffman_dict, data)
        return huffcode, heap

    while len(heap) > 1:
        left = heapq.heappop(heap)
        # print('left = ', left)
        right = heapq.heappop(heap)
        # print('right = ', right)

        # Add `0` to left and `1` to right
        for value in left[1:]:
            value[1] = '0' + value[1]
        # print('left add 0 =', left)
        for value in right[1:]:
            value[1] = '1' + value[1]
        # print('right add 1 =', right, '')

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    # Make a dictionary of a char and its binary code
    huffman_list = right[1:] + left[1:]
    huffman_dict = {a[0]: str(a[1]) for a in huffman_list}
    # print(huffman_dict)
    huffcode = encoded_text(huffman_dict, data)

    return huffcode, heap


def huffman_decoding(data, tree):
    decoded_text = ''
    current_code = ''

    for bit in data:
        current_code += bit

        if current_code in huffman_dict.values():
            for key in huffman_dict:
                if current_code == huffman_dict[key]:
                    decoded_text += key
                    current_code = ""
    return decoded_text


if __name__ == "__main__":
    codes = {}

    print('***** Testcase 1 *****')
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))

    print('\n***** Testcase 2 *****')
    a_great_sentence = "aabbccd"
    print("The size of the data is: {}".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))

    print('\n***** Testcase 3 *****')
    a_great_sentence = "xxyyz"
    print("The size of the data is: {}".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}".format(decoded_data))
