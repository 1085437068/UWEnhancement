import os


def getfiles():
    #filenames=os.listdir('../DATA/Train/train/UIEB/raw-890')
    filenames=os.listdir('../DATA/Test/test/UIEB/raw-890')
    print(filenames)
    return filenames



if __name__ == '__main__':

    #if not os.path.exists('train.txt'):
    #    os.mknod('train.txt')
    if not os.path.exists('test.txt'):
        os.mknod('test.txt')
    a = getfiles()
    # a.spilt('')
    l = len(a)
    with open("test.txt", "w") as f:
        for i in range(l):
            print(a[i])
            x = a[i]
            f.write(x)
            f.write('\n')
        f.close()

    print()