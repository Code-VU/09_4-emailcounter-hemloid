def countEmail():
    # This first line is provided for you
    name = input("Enter file: ")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    list_of_names = dict()

    for line in handle:
        if line.startswith('From '):
            new_line = line.split()[1]

            if new_line not in list_of_names:
                list_of_names[new_line] = 1

            else:
                list_of_names[new_line] += 1


    value = list_of_names.values()
    maxValue = max(value)

    
    print(max(list_of_names, key=list_of_names.get), maxValue)

                
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
