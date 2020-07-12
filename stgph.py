import re
img_name = ""


def read_img(path):
    with open(path, "br") as f:
        global img_name
        img_name = re.split("[/.]", path)
        return f.readlines()


def write_img(processed_byte):
    with open(f"{img_name[-2]}-stgph.{img_name[-1]}", "bw") as f:
        for item in processed_byte:

            f.write(item)


write_img(read_img("test.jpg"))
x = read_img("test.jpg")
x = x
print(x)