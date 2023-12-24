file = open('trial_file.txt', 'r')

text = 'the clever red fox jumps over the super high wall and falls on the back of the zebra'
file.seek(0)
count_list = file.readlines()
for i in text:
        
        for j in range (len(count_list)):
            read = count_list[j]
            if i == read[0]:
                read_list = list(read.split('='))
                read_list[1] = int(read_list[1])+1
                count_list[j] = f"{read_list[0]}={read_list[1]}\n"
file.close()
file = open('trial_file.txt', 'w')
file.seek(0)
file.writelines(count_list)