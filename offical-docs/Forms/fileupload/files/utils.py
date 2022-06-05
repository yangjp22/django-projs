def handleUploadedFile(file):
    with open('files/uploaded/name.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)