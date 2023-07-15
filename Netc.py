#!/usr/bin/env python3

PATH = "Netcat\\Netcat.txt"

class ASCII_CONV:
    def __init__(self, file_path) -> None:
        self.flag = ""
        self.file_path = file_path
        print(self.file_path)
    
    def ascii_decoder(self) -> str:
        with open(self.file_path) as ascii_file:
            for line in ascii_file:
                self.flag += chr(int(line.strip("\n")))
            return self.flag

if __name__ == "__main__":
    ascii_conversion = ASCII_CONV(PATH)
    print(ascii_conversion.ascii_decoder())




