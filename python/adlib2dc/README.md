# dri-metadata-tools - Adlib XML -> Dublin Core
Scripts for converting metadata from Adlib XML format to Dublin Core.

# Installation
Install Python 3 for your system.

To use the Graphical User Interface install the Python 3 Tkinter module.

Clone the repository from Github.

# Converting Adlib XML to Dublin Core
run the adlib2dc.py file by double clicking, or running from the command line.

Optional command-line parameters are --inputdir --outputdir

If you do not pass the inputdir and outputdir on the command line you will be prompted to enter or select them. If you have Tkinter installed you can select these via a Graphical User Interface, otherwise they can be typed in on the command line.

The script assumes that your asset files are JPEG images. It will look for asset files on a publicly shared Google Drive location as specified in the digital_reference field. If found, it will download these files to an "assets" subfolder in your output directory, with the same base filename as the generated XML file, but with the .jpg extension. If your assets are not JPEG images, or are not available on Google Drive, you may want to modify this script before running it.

