# we want to use pdflatex to build the final document
# we should collate everything into a large file first
all: 
	python3 addContent.py -i main.tex -o main_with_content.tex
	pdflatex main_with_content
	bibtex main_with_content
	pdflatex main_with_content
	pdflatex main_with_content
ifeq ($(OS),Windows_NT)
	mv main_with_content.pdf ../builds/MMIVActivities_latest.pdf
	start ../builds/MMIVActivities_latest.pdf
else
	mv main_with_content.pdf ../builds/MMIVActivities_latest.pdf
	open ../builds/MMIVActivities_latest.pdf
endif
