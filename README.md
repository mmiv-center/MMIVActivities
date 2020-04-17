## Activities of the Mohn Medical Imaging and Visualization Center

This repository stores records of the MMIV activities starting from 2019.

### How to get the latest report

There should be a checked in version of the final document created by this repository in the 'builds' folder

### How to contribute to this report

Reach out to Hauke and Noeska or make a pull-request

### How to build and compile a fresh report

Run the makefile in the 'Template' directory

## For Windows users
You need to be able to run **make** before you're ready to build anything. Also, you need Ghostscript to compress the PDF as well as an installed LateX environment set up. 
Here's one way to go about all this:
1. Download [minGW](http://www.mingw.org/)
2. Install **mingw-base-bin** and **msys-base-bin**
3. Add the mingw **bin** directory to the environment variable path
4. Download and install [Ghostscript](https://www.ghostscript.com/download/gsdnld.html) and also add that **bin** directory to the path
5. Download and install a LateX building environment if you don't have one already, for example [Tex Live](https://www.tug.org/texlive/)
5. Run your msys.bat file, which you can find in C:\MinGW\msys\1.0\ (if you installed MinGW on C:)
6. Navigate to the directory where your Github repository lives, and run the build with the command **mingw32-make** 
```cd /c/
cd GitHub/MMIVActivities/Template/
mingw32-make
```
7. Your fresh build will be in GitHub/MMIVActivities/builds
