def lay_ten_file(path):
    vi_tri = path.rfind("\\")
    return path[vi_tri + 1:]
def lay_ten_bai_hat(path):
    ten_file = lay_ten_file(path)
    vi_tri = ten_file.rfind(".")
    return ten_file[:vi_tri]
duong_dan = "d:\\music\\muabui.mp3"

print(lay_ten_file(duong_dan))
print(lay_ten_bai_hat(duong_dan))