from ntpath import join


message1 = input("Enter message 1: ")
message2 = "meetmeoutside"
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "bdufghweiufgwdlknflndklfnlkireupowqirpnmajcmlwoidychnsjvbxnlzowueorpnsjskakeoirywis"
result = ""

def encrypt(key):
    result = message2.replace(" ", "")
    position_list= []
    key_position_list = []
    result_list = []
    for i in result:
        position = alphabet.find(i)
        position_list.append(position)
        new_key = key[0:len(result)]
        print("NEWKEY", new_key)
    for i in new_key:
        key_position = alphabet.find(i)
        key_position_list.append(key_position)
    key_output_list = [(x + y)%len(alphabet) for x, y in zip(position_list, key_position_list)]
    for i in key_output_list:
        result_list.append(alphabet[i]) 
    print(position_list)
    print(key_position_list)
    print(key_output_list)
    print(result_list)
    print(''.join(result_list))
    return ''.join(result_list)

encrypt(key)

