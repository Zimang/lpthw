import sys
script, input_encoding, error = sys.argv
#.script把
#b'' 告诉py这是byte string

def main(language_file, encoding, errors):
    line = language_file.readline()
    #如果readline返回了任意字符则line为真
    if line:
        print_line(line, encoding,errors)
        return main(language_file,encoding,errors)

def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors)
    cooked_string = raw_bytes.decode(encoding,errors=errors)
    print(raw_bytes,"<===>",cooked_string)


languages = open("languages.txt",encoding="utf-8")

main(languages,input_encoding,error)
