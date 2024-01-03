# Program to check if a abstring is a substring of another string

def substrCheck(str1, str2):
    M = len(str1)
    N = len(str2)
    if M > N:
        # substring cannot be larger than string
        return 0
    else:
        # check if str1 is substring of str2
        x = N - M + 1 + 1 
        flag = False
        for i in range(0, x):
            if i <= x-2:
                for j in range(0, M):
                    if str1[j] != str2[i+j]:
                        break
                    elif str1[j] == str2[i+j]:
                        #print(str1[j] + " " + str2[i+j])
                        if j+1 == M:
                            flag = True
                            return i+1
                            break
            elif i == x-1:
                if flag == False:
                    return -1
                    break

# str1 = input("Enter a substring, then press enter: ")
# str2 = input("Enter a string, then press enter: ")
str1 = "bcd"
str2 = "abcdefg"

print("Checking whether \"" + str(str1) + "\" is a substring of \"" + str(str2) + "\"...")
result = substrCheck(str1, str2)

if result == 0:
    print("The substring cannot be longer than the string!")
elif result == -1:
    print("The substring does not occur in the string.")
elif result >= 1:
    print("The substring first occurs at index " + str(result) + ".")


