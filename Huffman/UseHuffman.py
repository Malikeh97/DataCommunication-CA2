from huffman import HuffmanCoding

input_txt = input("Enter the text: ")

h = HuffmanCoding(input_txt)

compressed_text = h.compress()
print("Compressed Text: ", compressed_text)

decompressed_text = h.decompress(compressed_text)
print("Decompressed Text: ", decompressed_text)
