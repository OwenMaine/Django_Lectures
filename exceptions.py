#use the try, except and finally to check for errors and expressions
try:
    f= open("simple.txt", "w")
    f.write("This is a txt file")
except IO:
    print("EROR!, couldnt read file")
else:
    print("Success")
