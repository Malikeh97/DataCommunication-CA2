from ConvCoding import ConvolutionalCoding

input_txt = input("Enter the input string: ")

CC = ConvolutionalCoding(input_txt)

encoded_str = CC.encode_string()

print("Encoded String is:", encoded_str)
