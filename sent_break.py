import sys
import nltk.data

def sent_break(src_filename, new_filename):
    ext_counter = 0
    int_counter = 0
    new_line  = ""
    with open(src_filename, encoding="utf-8") as src_file:
        with open(new_filename, "w", encoding="utf-8") as new_file:
            for line_src in src_file:
                ext_counter += 1
                int_counter = 0
                for word_src in line_src[:-1].split():
                    int_counter += 1
                    new_line = new_line + word_src
                    if (int_counter == ext_counter%(len(line_src[:-1].split()) - 1)+1):
                        new_line = new_line + "\n"
                    else:
                        new_line = new_line + " "
                new_file.write(new_line.strip() + "\n")
                new_line  = ""

def sent_join(src_filename, new_filename):
    ext_counter = 0
    new_line  = ""
    with open(src_filename, encoding="utf-8") as src_file:
        with open(new_filename, "w", encoding="utf-8") as new_file:
            for line_src in src_file:
                ext_counter += 1
                if (ext_counter%2 == 0):
                    new_line = new_line[:-1] + " " + line_src
                    new_file.write(new_line)
                else:
                    new_line = line_src
					
def tokenize(src_filename, new_filename):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open(src_filename, encoding="utf-8")
    data = fp.read()
    data = data.replace("\n"," ")
    with open(new_filename, "w", encoding="utf-8") as new_file:
        new_file.write("%s" % '\n'.join(tokenizer.tokenize(data)))
				
if __name__ == '__main__':
    src_filename = sys.argv[1]
    new_filename = sys.argv[2]
    #sent_break(src_filename, new_filename)
    #sent_join(src_filename, new_filename)
    tokenize(src_filename, new_filename)