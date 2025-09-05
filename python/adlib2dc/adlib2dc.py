#!/usr/bin/env python

import argparse
import os
import tempfile
from lxml import etree as ET
from urllib.parse import urlparse
import requests
import re

gui = True
try:
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    gui = False

global img

def main():
    inputdir, outputdir = setup()
    with tempfile.TemporaryDirectory() as tmpdir:
        convert(inputdir, outputdir)


## Get the inputdir and outputdir by hook or by crook!
## If the machine has Tkinter installed we can use a graphical
## file browser. Otherwise the user can enter the params on the
## command line or via an input prompt
## The multiple methods are there to make it as easy as possible
## for users with different needs and experience to use the tool
def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputdir', help='The input directory')
    parser.add_argument('--outputdir', help='The output directory')
    args = parser.parse_args()

    if gui:
        app = Tk()
        app.title("DRI AdlibXML to Dublin Core")
        canvas = Canvas(app, width = 100, height = 100)
        canvas.pack()      
        img = PhotoImage(file="./assets/dri_ident_tiny.png")      
        canvas.create_image(20,20, anchor=NW, image=img)      
        inputdir = args.inputdir or filedialog.askdirectory(initialdir = ".",
                                    title = "Select input diretory")
        outputdir = args.outputdir or filedialog.askdirectory(initialdir = ".",
                                    title = "Select output diretory")
    else:
        inputdir = args.inputdir or input("Please enter the input directory ")
        outputdir = args.outputdir or input("Please enter the output directory ")

    inputdir = inputdir.rstrip()
    outputdir = outputdir.rstrip()

    return inputdir, outputdir


## parse each file in the inputdir, convert to dc and output to output dir
def convert(inputdir, outputdir):

    infiles = os.listdir(inputdir)
    for f in infiles:
        infile = os.path.join(inputdir, f)
        tree = ET.parse(infile)
        root = tree.getroot()

        # create the new DC xml tree
        dctree = ET.ElementTree(ET.fromstring('<qualifieddc xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:marcrel="http://www.loc.gov/marc.relators/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/marc.relators/ http://imlsdcc2.grainger.illinois.edu/registry/marcrel.xsd" xsi:noNamespaceSchemaLocation="http://dublincore.org/schemas/xmls/qdc/2008/02/11/qualifieddc.xsd"></qualifieddc>'))

        # get the dc root element
        dcroot = dctree.getroot()

        #Populate dcroot with dc ns elements
        for title in root.iter('title'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}title")
            body.text = title.text 

        for identifier in root.iter('object_number'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}identifier")
            body.text = identifier.text

        for description in root.iter('description'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}description")
            body.text = description.text

        for language in root.iter('language'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}language")
            body.text = language.text

        for language in root.iter('inscription.language'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}language")
            body.text = language.text

        for type in root.iter('content.source.general'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}type")
            body.text = type.text

        for type in root.iter('content.classification.scheme'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}type")
            body.text = type.text

        for rights in root.iter('rights.type'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}rights")
            body.text = rights.text

        for subject in root.iter('content.subject.note'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}subject")
            body.text = subject.text

        for format in root.iter('object_name.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}format")
            body.text = format.text

        for date in root.iter('production.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}date")
            body.text = date.text

        for date in root.iter('production.date.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}date")
            body.text = date.text

        if (tree.xpath('count(//recordList/record/creator[not(*) and normalize-space()])') < 1):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}creator")
            body.text = "Unknown"

        for creator in root.iter('creator'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}creator")
            body.text = creator.text

        for subject in root.iter('content.person.name'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}subject")
            body.text = subject.text

        for subject in root.iter('content.subject.note'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}subject")
            body.text = subject.text

        for rights in root.iter('rights.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}rights")
            body.text = rights.text

        for source in root.iter('content.source.specific'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}source")
            body.text = source.text

        for source in root.iter('digital_reference'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/elements/1.1/}source")
            body.text = source.text

        #Populate dcroot with dcterms ns elements
        for alternative in root.iter('object_name'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}alternative")
            body.text = alternative.text

        for extent in root.iter('dimension.type'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}extent")
            body.text = extent.text

        for ispartof in root.iter('research.reference_number'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}isPartOf")
            body.text = ispartof.text

        for medium in root.iter('material.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}medium")
            body.text = medium.text

        for created in root.iter('content.date.note'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}created")
            body.text = created.text

        for temporal in root.iter('production.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}temporal")
            body.text = temporal.text

        for temporal in root.iter('production.date.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}temporal")
            body.text = temporal.text

        for spatial in root.iter('field_coll.notes'):
            body = ET.SubElement(dcroot, "{http://purl.org/dc/terms/}spatial")
            body.text = spatial.text


        # Output the new dc XML tree
        outfile = os.path.join(outputdir, f)
        dctree.write(outfile, encoding='utf-8', xml_declaration=True)


        # Download image files 
        for source in root.iter('digital_reference'):
            urlparts = urlparse(source.text)
            path = urlparts.path
            tmp = re.sub("/file/d/", "", path)
            assetid = re.sub("/view", "", tmp)
            dlurl = "https://drive.google.com/uc?id="+assetid

            assetsdir = os.path.dirname(outputdir) + "/assets"
            if not os.path.exists(assetsdir):
                os.makedirs(assetsdir)
            req = requests.get(dlurl)
            
            tmp = re.sub(".xml", "", f)
            assetfile = assetsdir + "/" + tmp + ".jpg"

            open(assetfile, 'wb').write(req.content)



if __name__ == '__main__':
    main()
