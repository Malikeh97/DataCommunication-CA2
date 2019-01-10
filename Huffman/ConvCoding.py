class ConvolutionalCoding:
    def __init__(self, input_string):
        self.input_string = input_string
        self.encoded_str = ''
        self.cur_state = 0

    def update_state(self, input_char):
        nextState = 0
        if(self.cur_state == 0 and input_char == "0"):
            self.cur_state = 0
            self.encoded_str = self.encoded_str + "00"
        elif(self.cur_state == 0 and input_char == "1"):
            self.cur_state = 2
            self.encoded_str = self.encoded_str + "11"
        elif(self.cur_state == 1 and input_char == "0") :
            self.cur_state = 0
            self.encoded_str = self.encoded_str + "10"
        elif(self.cur_state == 1 and input_char == "1") :
            self.cur_state = 2
            self.encoded_str = self.encoded_str + "01"
        elif(self.cur_state == 2 and input_char == "0") :
            self.cur_state = 1
            self.encoded_str = self.encoded_str + "11"
        elif(self.cur_state == 2 and input_char == "1") :
            self.cur_state = 3
            self.encoded_str = self.encoded_str + "00"
        elif(self.cur_state == 3 and input_char == "0") :
            self.cur_state = 1
            self.encoded_str = self.encoded_str + "01"
        else:
            self.cur_state = 3
            self.encoded_str = self.encoded_str + "10"
        return;

    def encode_string(self):
        for i in range(len(self.input_string)):
            self.update_state(self.input_string[i])
        return self.encoded_str
