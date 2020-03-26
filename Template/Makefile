# we want to use pdflatex to build the final document
# we should collate everything into a large file first
all:
	python3 addContent.py -i main.tex -o main_with_content.tex
	pdflatex main_with_content.tex
	pdflatex main_with_content.tex
	#mv main_with_content.pdf ../builds/MMIVActivities_latest.pdf
	#open ../builds/MMIVActivities_latest.pdf

