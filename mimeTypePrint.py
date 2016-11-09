from numpy.lib.format import magic

def mime(file):
    mime = magic.Magic(mime=True)
    print mime.from_file(file)



if __name__ == '__main__':

    mime("/Users/mac/Desktop/1.php")

