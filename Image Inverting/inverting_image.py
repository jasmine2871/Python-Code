"""Retrieves the size of a bmp image and crops the image


Submitted by Jasmine 
This script reads a bmp file and retrieves the size information and other
details. It then takes the image and flips it upside down 180 degrees.
"""


def retrieve_int(file_handle, num_bytes):
    """ Converts bytes read from a file into an int
    :param file_handle: file
    :param num_bytes: number of bytes to be read
    :return: an integer representation of the bytes
    This function affects the file as it moves the pointer.
    It handles the binary data as representing numbers
    specified as Little Endian.
    """
    num_bytes = bytearray(file_handle.read(num_bytes))
    # Data in bmp files is in Little Endian format
    num_bytes.reverse()
    num_int = 0
    for byte in num_bytes:
        num_int = num_int * 256 + byte
    return num_int


# Task 1.1 Read and interpret the header
filename = input("What is the image file to be flipped? ")
if filename == "":
    filename = "Arenal Volcano-Lodge-n-Spring Costa Rica.bmp"

while True:
    try:
        imageFile = open(filename, "br")
    except FileNotFoundError:
        print()
        print("File could not be opened, please check if the file name is typed correctly.")
        print("Please type in desired image file or press enter for default file.")
        filename = input("What is the image file to be flipped? ")
        if filename == "":
            filename = "Arenal Volcano-Lodge-n-Spring Costa Rica.bmp"
    else:
        break

descriptor = imageFile.read(2)
file_size = retrieve_int(imageFile, 4)
unspecified = retrieve_int(imageFile, 4)
offset = retrieve_int(imageFile, 4)
header_size = retrieve_int(imageFile, 4)
image_width = retrieve_int(imageFile, 4)
image_height = retrieve_int(imageFile, 4)
color_planes = retrieve_int(imageFile, 2)
bits_per_pixel = retrieve_int(imageFile, 2)

print(descriptor)
print(f"File size: {file_size} bytes")
print(f"The offset is {offset} bytes")
print(f"The header size is {header_size}")
print(f"Image is {image_width} (w) x {image_height} (h)")
print(f"Planes: {color_planes}")
print(f"It uses {bits_per_pixel} bits per pixel")


# Task 1.2 Save a copy of the header and get ready to read the data
imageFile.seek(0)
header_copy = imageFile.read(offset)

# Task 1.3 Load the pixel information in a 2D-List
bytes_per_pixel = bits_per_pixel // 8
padding_length = (-bytes_per_pixel * image_width % 4)
print(f"Padding is {padding_length}")
print(f"Bytes per pixel is {bytes_per_pixel}")

pixel_table = []
for row in range(image_height):
    horiz_pixels = []  # This will contain the pixels in the horizontal line.
    for hor_pos in range(image_width):
        horiz_pixels.append(imageFile.read(bytes_per_pixel))
#     # This is the end of the horizontal line. Padding bytes
#     # if present will follow. Use image_bmp.read(padding_length)
#     # to read them and ignore them.
#     # We make the 2-D list by appending the lists with the horizontal lines.
    horiz_pixels += imageFile.read(padding_length)
    pixel_table.append(horiz_pixels)

# Task 1.4 Invert the image and save the output
splitFilename = filename.split('.')
splitFilename[-2] = splitFilename[-2] + ' inverted'
output_file_name = '.'.join(splitFilename)

output_file = open(output_file_name, 'bw')

reversed_pix_table = pixel_table.copy()
reversed_pix_table.reverse()
output_file.write(header_copy)
for horiz_pixels in reversed_pix_table:
    horiz_pixels.reverse()
    horiz_line = b""
    for pixel in horiz_pixels:
        horiz_line += pixel
    horiz_line_pad = horiz_line + bytes(padding_length)
    output_file.write(horiz_line_pad)


output_file.close()
imageFile.close()
