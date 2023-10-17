require 'rmagick'
include Magick
require 'pry'
# file_name = "Screenshot.png"
file_name = "triangle.png"
image = ImageList.new(file_name)
grayscale_image = image.quantize(256, Magick::GRAYColorspace)
grayscale_image.write("gray.png")

# result = exec("python3 script2.py #{file_name}")
# puts result


result = exec("python3 script.py #{file_name}")
puts result