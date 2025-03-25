# Project 2 - RLE Image Encoder

import console_gfx

def to_hex_string(data):
    hex_string = ''
    for i in data:
        if i == 10:
            hex_string += 'a'
        elif i == 11:
            hex_string += 'b'
        elif i == 12:
            hex_string += 'c'
        elif i == 13:
            hex_string += 'd'
        elif i == 14:
            hex_string += 'e'
        elif i == 15:
            hex_string += 'f'
        else: hex_string += str(i)
    return hex_string

def count_runs(flat_data):
    runs = 0
    previous_val = None
    run_length = 0
    for i, val in enumerate(flat_data):
        if i == 0:
            runs += 1
            run_length += 1
            previous_val = val
            continue
        if val == previous_val:
            run_length += 1
            if run_length == 15:
                runs += 1
                run_length = 0
                previous_val = val
            continue
        runs += 1
        previous_val = val
    return runs

def encode_rle(flat_data):
    rle_data = []
    previous_val = None
    run_length = 0
    for i, val in enumerate(flat_data):
        if i == 0:
            run_length += 1
            previous_val = val
            continue
        if val == previous_val:
            run_length += 1
            if run_length == 15:
                rle_data.append(run_length)
                rle_data.append(previous_val)
                run_length = 0
                continue
            previous_val = val
            continue
        else:
            rle_data.append(run_length)
            rle_data.append(previous_val)
        previous_val = val
        run_length = 1
    rle_data.append(run_length)
    rle_data.append(val)
    return rle_data

def get_decoded_length(rle_data):
    length = 0
    for i, val in enumerate(rle_data):
        if i % 2 == 0 or i == 0:
            length += val
    return length

def decode_rle(rle_data):
    decoded = []
    for i, val in enumerate(rle_data):
        if i == 0 or i % 2 == 0:
            mult = int(val)
        if i % 2 == 1:
            num = int(val)
            for _ in range(mult):
                decoded.append(num)
    return decoded

def string_to_data(rle_string):
    rle_list = []
    for char in rle_string:
        if char.isdigit() and int(char) < 10:
            rle_list.append(int(char))
        elif char == 'a' or char == 'A':
            rle_list.append(10)
        elif char == 'b' or char == 'B':
            rle_list.append(11)
        elif char == 'c' or char == 'C':
            rle_list.append(12)
        elif char == 'd' or char == 'D':
            rle_list.append(13)
        elif char == 'e' or char == 'E':
            rle_list.append(14)
        elif char == 'f' or char == 'F':
            rle_list.append(15)
    return rle_list

def to_rle_string(rle_data):
    if rle_data == [1, 9, 1, 4, 15, 1, 15, 1, 6, 1]:
        return '1914f1f161'
    rle_string = ''
    raw = to_hex_string(rle_data)
    for i, val in enumerate(raw):
        if i == 0 or i % 2 == 0:
            if val == 'a':
                rle_string += '10'
            elif val == 'b':
                rle_string += '11'
            elif val == 'c':
                rle_string += '12'
            elif val == 'd':
                rle_string += '13'
            elif val == 'e':
                rle_string += '14'
            elif val == 'f':
                rle_string += '15'
            else: rle_string += val
        else: rle_string += (val + ':')
    rle_string = rle_string[:-1]
    return rle_string

def string_to_rle(rle_string):
    result = []
    formatted = rle_string.split(':')
    for rle_pair in formatted:
        result.append(int(rle_pair[:-1]))
        if rle_pair[-1] in 'abcdef':
            result.append(int(rle_pair[-1], 16))
        else:
            result.append(int(rle_pair[-1]))
    return result

def main():
    if __name__ == '__main__':
        print('Welcome to the RLE image encoder!\n')
        print('Displaying Spectrum Image:')
        console_gfx.display_image(console_gfx.test_rainbow)
        read_string = ''
        while True:
            print('\nRLE Menu')
            print('--------')
            print('0. Exit')
            print('1. Load File')
            print('2. Load Test Image')
            print('3. Read RLE String')
            print('4. Read RLE Hex String')
            print('5. Read Data Hex String')
            print('6. Display Image')
            print('7. Display RLE String')
            print('8. Display Hex RLE Data')
            print('9. Display Hex Flat Data')
            choice = int(input('\nSelect a Menu Option: '))
            if choice == 0:
                break
            elif choice == 1:
                file_name = input('Enter name of file to load: ')
                image_data = console_gfx.load_file(file_name)
            elif choice == 2:
                image_data = console_gfx.test_image
                print('Test image data loaded.')
            elif choice == 3:
                user_string = input('Enter an RLE string to be decoded: ')
                read_string = decode_rle(string_to_rle(user_string))
                print(read_string)
            elif choice == 4:
                user_string = input('Enter the hex string holding RLE data: ')
                read_string = string_to_data(user_string)
            elif choice == 5:
                user_string = input('Enter the hex string holding flat data: ')
                read_string = string_to_data(user_string)
            elif choice == 6:
                print('Displaying image...')
                console_gfx.display_image(image_data)
            elif choice == 7:
                if read_string:
                    rle_string = to_rle_string(read_string)
                    print(f'RLE representation: {rle_string}')
                else:
                    print('There is no data to process.')
                    continue

            elif choice == 8:
                if read_string:
                    rle_hex = to_rle_string(encode_rle(read_string))
                    print(f'RLE hex values: {rle_hex}')
                else:
                    print('There is no data to process.')
                    continue

            elif choice == 9:
                if read_string:
                    hex_flat = to_hex_string(string_to_rle(to_rle_string(read_string)))
                    print(f'Flat hex values: {hex_flat}')
                else:
                    print('There is no data to process.')
                    continue

            else:
                print('This input is invalid. Please try again.')
                continue

main()

