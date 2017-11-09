def fun(s):
    # return True if s is a valid email, else return False
    
    #It must have the username@websitename.extension format type.
    if s.count('@') != 1 or s.count('.') != 1:return False
    username , rest = s.split("@")
    website , extension = rest.split('.')
    
    #The username can only contain letters, digits, dashes and underscores.
    if username.replace("_","").replace("-","").isalnum() == False: return False
    #The website name can only have letters and digits.
    if website.isalnum() == False: return False
    #The maximum length of the extension is 3. 
    if len(extension)>3 or len(extension)==0: return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
