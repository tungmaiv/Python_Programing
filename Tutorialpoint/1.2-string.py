import sys

print(sys.executable)
print(sys.version)

str = 'Hello World!'
greeting = 'Hello'
fname = 'Tung'
lname = 'Vu'
msg = f'{greeting}, {fname.upper()} {lname.upper()}. Welcome!'
print(str)           # Prints complete string
print(str[0])        # Prints first character of the string
print(str[2:5])      # Prints characters starting from 3rd to 5th
print(str[2:])       # Prints string starting from 3rd character
print(str * 2)       # Prints string two times
print(str + "TEST")  # Prints concatenated string
print(msg)

sample_url = "https://www.google.com.hn.vn"
print(f"Top level domain is: {sample_url[-4:]}")
print(f"Company name is: {sample_url[-10:-4]}")
print(f"Domain name is: {sample_url[8:]}")

print(sample_url.find(".", 12))
print(sample_url.count("."))
domain_name = sample_url[8:]
print(f"FDN is: {domain_name}")
i = 0
begin_pos = 0
end_pos = domain_name.find(".")

while i <= domain_name.count("."):
    if i != domain_name.count("."):
        print(f"Domain part is: {domain_name[begin_pos:end_pos]}")
    else:
        print(f"Top domain is: {domain_name[begin_pos:len(domain_name)]}")
    begin_pos = end_pos + 1
    end_pos = domain_name.find(".", begin_pos)
    print(end_pos)
    i += 1
# print(dir(msg))
# print(help(str.find))
