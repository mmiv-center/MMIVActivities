#!/bin/env python3
#
# Add known entries to the template tex file.
# Two arguments
#  <1> - input: the main tex document
#  <2> - output: the output tex document that should be created

import sys
import getopt
import glob
import re


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, _ = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('addContent.py -i <main.tex> -o <main_with_content.tex>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('addContent.py -i <main.tex> -o <main_with_content.tex>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == '' or outputfile == '':
        print('addContent.py -i <main.tex> -o <main_with_content.tex>')
        sys.exit(2)
    print("Start processing")
    print("  Input file is \"%s\"" % (inputfile))
    print("  Output file is \"%s\"" % (outputfile))
    print("")

    # read the main template
    main_tex = ''
    with open(inputfile, 'r') as reader:
        main_tex = reader.read()
    if main_tex != '':
        print("read main template done...")
    else:
        print("Error: no %s file found." % (inputfile))
        sys.exit(-1)

    # we replace the following placeholders
    replacements = {'%%PLACEHOLDERSOFTWARE%%': 'Software',
                    '%%PLACEHOLDEREVENTS%%': 'Events',
                    '%%PLACEHOLDERDISSERTATIONS%%': 'Dissertations',
                    '%%PLACEHOLDERHIGHLIGHTS%%': 'Highlights',
                    '%%PLACEHOLDERPROJECTS%%': 'Projects',
                    '%%PLACEHOLDERINTRODUCTIONS%%': 'Introduction'
                    }

    c = 0
    for replacement in replacements:
        print("Replacement %d" % (c))
        c = c + 1
        text = ''
        key = replacement
        folder = replacements[key]
        print("  replace %s with content from folder %s" % (key, folder))
        template = ''
        with open("pieces/%s.temp" % (folder)) as reader:
            template = reader.readlines()
        template = "".join(template)

        # now look for content
        files = sorted(glob.glob("../%s/*/*.md" % (folder)))
        for file in files:
            print("  parse the content in %s" % file)
            file_content = ''
            with open(file, 'r') as f:
                file_content = f.read()

            # add the parsed fields to the template
            thistext = template
            # what are the keys in the template
            m = re.findall('%%[a-zA-Z0-9]+%%', thistext)
            d = {}
            for n in m:
                n_base_text = n.replace("%", "")
                d[n_base_text] = ''
                # check if we have a value in file_content
                if n_base_text == "text":
                    # special case, we take everything in the file that comes after
                    s = re.search("text:(.*)$", file_content,
                                  re.MULTILINE | re.DOTALL)
                else:
                    s = re.search(
                        n_base_text + ": ([^\n]+)", file_content, re.IGNORECASE)
                try:
                    d[n_base_text] = s.group(1)
                except:
                    pass

            # now replace in thistext all the occurences of our pattern
            for k, v in d.items():
                thistext = thistext.replace("%%%%%s%%%%" % k, v)
            # add the template at the end of 'text'
            text = "%s\n%s" % (text, thistext)

        # now replace key in main_tex with 'text'
        main_tex = main_tex.replace(key, text)

    # now save the new main_tex to disc again
    with open(outputfile, 'w') as writer:
        writer.write(main_tex)
    print("done..")


if __name__ == "__main__":
    main(sys.argv[1:])
