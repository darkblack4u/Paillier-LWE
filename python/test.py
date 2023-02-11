file_object1 = open(
    "D:\\Workspace\\Paillier-LWE\\file\\log_client_copy.txt", 'rb')
count = 0
try:
    while True:
        line = file_object1.readline()
        if line:
            print("line=", line)
            count = count + 1
        else:
            break
finally:
    file_object1.close()
print(count)
