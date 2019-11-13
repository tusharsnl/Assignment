def log_extractor(file):
    f=open(file,"r")
    print('hey')
    f1 = f.readlines()
    list_valid_entries=[]
    for x in f1:
        if("ERROR".lower() in x.lower()):
            list_valid_entries.append(x)
        elif("WARNING".lower() in x.lower()):
            list_valid_entries.append(x)
    dict_error_warnings={}

    list_e_w=[]
    for each_str in list_valid_entries:
        if("ERROR" in each_str):
            l=each_str.split("ERROR")
        else:
            l=each_str.split("WARNING")
            if(len(l)==2):
                dict_error_warnings['Date/Time']=l[0].strip()
                dict_error_warnings['Message']=l[1].strip()
        list_e_w.append(dict_error_warnings.copy())
        dict_error_warnings.clear()

    print(list_e_w)
    f2=open("output.txt","w+")
    for each in list_e_w:
        f2.write(str(each))

file_name="test.log"
log_extractor(file_name)
