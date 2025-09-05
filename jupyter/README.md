# dri-metadata-tools - Jupyter Notebooks
A selection of Jupyter Notebooks for preparing metadata.

Jupyter notebooks are documents that blends text, code and its output. They are often used to share a researcher's work in a transparent way, allowing all of the research processes and steps to be understood and reproduced.

The notebooks provided here allow users to manipulate metadata. They may ask you to upload some files or provide a link to metadata online. By running the code in these notebooks on your metadata, you can clean or transform it in some way which will help you to produce rich metadata for ingest into the Digital Repository of Ireland, or another platform that supports Dublin Core metadata.

To use these notebooks, it is not necessary to fully understand what the code is doing. You simply need to run the code blocks in the correct order, and provide the appropriate input when requested.

Each notebook is explained below.

## DRI_Ingest_Template_to_XML.ipynb
A Jupyter Notebook file to convert the [DRI Metadata Template spreadsheet](https://doi.org/10.7486/DRI.qn603p95v-8) to Dublin Core XML files.

To use this notebook, you need your metadata in a .xlsx spreadsheet format, with the Dublin Core metadata field names as column headings. If you don't already have your metadata in a suitable format, download and populate the [DRI Metadata Template spreadsheet](https://doi.org/10.7486/DRI.qn603p95v-8) with your metadata.

You can use tools such as [OpenRefine](https://openrefine.org/) to clean your metadata, but in order to use this notebook, you must re-export the cleaned metadata as a .xlsx file.

This notebook contains three code steps which must be executed in order. Before executing these, you must upload your metadata spreadsheet to a location accessible to your notebook, and create an output folder for the Dublin Core XML files. If you are using MyBinder to run the notebook, you should click on the Folder icon on the top left corner of the screen to open the File Manager.

![Screenshot showing the folder icon and File Manager in MyBinder.](./assets/FileBrowser.png)

As you execute the steps, you may see some output messages or be asked to provide input. This will happen immediately below the currently executing step. It is important to read these to see if you have encountered any errors, or to provide input when required.

![Screenshot showing code output and input prompts when running a code cell.](./assets/InputOutput.png)

If you see any errors in the input area you will likely have to re-run that step.

### Steps
1. The "Initialisation" step will set up the environment for the notebook and will ask you to identify the input metadata file and the output folder. It also creates some code functions which will be used.
2. The "Check and Clean the Metadata" step reads in your metadata file and performs some checks to make sure that it can be converted to Dublin Core XML files. It will ask you to identify the tab in your spreadsheet that contains the metadata and may ask you to identify the DC field to which to map any columns of your spreadsheet that it does not recognise.
3. The "Process Metadata and create XML files" step creates one XML file in Dublin Core format for each row in your spreadsheet. When all rows are processed, it will attempt to create a zipfile and tar.gz archive of the output folder which you can download.

You can download this notebook to run in your preferred Jupyter Notebooks environment, or lauch this notebook in Binder by clicking on the Binder button. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Digital-Repository-of-Ireland/dri-metadata-tools/HEAD?urlpath=%2Fdoc%2Ftree%2Fjupyter%2FDRI_Ingest_Template_to_XML.ipynb)

