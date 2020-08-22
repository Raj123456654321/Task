def same_person(user_list):
    output_list = [[0]]
    aux_set = [[{user_list[0][0]}, {user_list[0][1]}, {user_list[0][2]}]]
    for i in range(1,len(user_list)):
        for j in range(len(aux_set)):
            if user_list[i][0] in aux_set[j][0] or user_list[i][1] in aux_set[j][1] or user_list[i][2] in aux_set[j][2]:
                aux_set[j][0].add(user_list[i][0])
                aux_set[j][1].add(user_list[i][1])
                aux_set[j][2].add(user_list[i][2])
                output_list[j].append(i)
                break;
            aux_set.append([{user_list[i][0], user_list[i][1], user_list[i][2]}])
            output_list.append([i])
    print(output_list)
    return


if __name__ == "__main__":
    data = [
        ("username1", "phone_number1", "email1"),
        ("usernameX", "phone_number1", "emailX"),
        ("usernameZ", "phone_numberZ", "email1Z"),
        ("usernameY", "phone_numberY", "emailX")
    ]
    print(data)
    same_person(data)