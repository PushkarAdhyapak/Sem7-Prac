import heapq
from collections import defaultdict, Counter
import time

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(text):
    frequency_counter = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency_counter.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = Node(None, left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, code, huffman_codes):
    if node.char:
        huffman_codes[node.char] = code
    if node.left:
        build_huffman_codes(node.left, code + "0", huffman_codes)
    if node.right:
        build_huffman_codes(node.right, code + "1", huffman_codes)

def huffman_encoding(text):
    if len(text) == 0:
        return "", {}

    start_time = time.time()
    root = build_huffman_tree(text)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    encoded_text = "".join(huffman_codes[char] for char in text)
    end_time = time.time()

    total_time = end_time - start_time
    return encoded_text, huffman_codes, total_time

def main():
    input_text = input("Enter the input string: ")
    encoded_text, huffman_codes, total_time = huffman_encoding(input_text)

    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")

    print("Encoded Text:", encoded_text)
    print("Total time taken:", total_time, "seconds")

if __name__ == "__main__":
    main()

