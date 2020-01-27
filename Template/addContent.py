#!/bin/env python3
#
# Add known entries to the template tex file.
# Two arguments
#  <1> - input: the main tex document
#  <2> - output: the output tex document that should be created

import sys
import getopt
import glob


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
    print("Input file is \"%s\"" % (inputfile))
    print("Output file is \"%s\"" % (outputfile))

    # read the main template
    main_tex = ''
    with open(inputfile, 'r') as reader:
        main_tex = reader.read()

    # we replace the following placeholders
    replacements = {'%%PLACEHOLDERSOFTWARE%%': 'Software',
                    '%%PLACEHOLDEREVENTS%%': 'Events'}

    for replacement in replacements:
        text = ''
        key = replacement
        folder = replacements[key]
        print("replace %s with content from folder %s" % (key, folder))
        template = ''
        with open("pieces/%s.temp" % (folder)) as reader:
            template = reader.readlines()

        # now look for content
        files = glob.glob("../%s/*/*.md" % (folder))
        for file in files:
            print("parse the content in %s" % file)
            # add the parsed fields to the template
            thistext = template

            # add the template at the end of 'text'
            text = "%s\n%s" % (text, thistext)

        # now replace key in main_tex with 'text'
        main_tex.replace(key, text)

    # now save the new main_tex to disc again
    with open(outputfile, 'w') as writer:
        writer.write(main_tex)
    print("done..")


if __name__ == "__main__":
    main(sys.argv[1:])
