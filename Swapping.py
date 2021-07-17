def swapFileData():
    file1 = input("Enter the first file name: ")
    file2 = input("Enter the second file name: ")
    data_a = open(file1,"r")
    a = data_a.read()
    data_b = open(file2,"r")
    b = data_b.read()

    with open(file1,'w') as data_a:
        data_a.write(b)

    with open(file2,'w') as data_b:
        data_b.write(a)    
    print("The files have been swapped!")
    swapFileData()        




