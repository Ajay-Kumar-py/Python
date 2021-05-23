import zipfile

with zipfile.ZipFile("C:/Users/abhishek/PycharmProjects/travello/travello.zip", 'r') as zip_ref:
    zip_ref.extractall("C:\\Users\\abhishek\\PycharmProjects\\travello")

    with zipfile.ZipFile('D:\\travello\\travello.zip', 'r') as zip_ref:
        zip_ref.extractall('D:\\travello')
