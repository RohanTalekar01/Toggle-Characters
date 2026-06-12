def toggleChar(str):
    result=""

    for i in range(len(str)):
        ch=str[i]

        if ch.isupper():
            result +=ch.lower()
        else:
            result +=ch.upper()
    return result

if __name__ == "__main__":
    str="GeEkSfOrGeEkS"
    x=toggleChar(str)
    print(x)
            
    
