# Project 2 - RLE Image Encoder

import console_gfx

def to_hex_string(data):
    hex_string = ''
    for i in data:
        if i in range(0,10):
            hex_string += str(i)
        if i == 10:
            hex_string += 'a'
        if i == 11:
            hex_string += 'b'
        if i == 12:
            hex_string += 'c'
        if i == 13:
            hex_string += 'd'
        if i == 14:
            hex_string += 'e'
        if i == 15:
            hex_string += 'f'
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
            for i in range(mult):
                decoded.append(num)
    return decoded

def string_to_data(rle_string):
    rle_list = []
    for char in rle_string:
        if char.isdigit() and int(char) < 10:
            rle_list.append(int(char))
        elif char == 'a':
            rle_list.append(10)
        elif char == 'b':
            rle_list.append(11)
        elif char == 'c':
            rle_list.append(12)
        elif char == 'd':
            rle_list.append(13)
        elif char == 'e':
            rle_list.append(14)
        elif char == 'f':
            rle_list.append(15)
    return rle_list

def main():
    print('Welcome to the RLE image encoder!\n')
    print('Displaying Spectrum Image:')
    console_gfx.display_image(console_gfx.test_rainbow)

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
        elif choice == 6:
            console_gfx.display_image(image_data)
        else:
            print('This input is invalid. Please try again.')
            continue

