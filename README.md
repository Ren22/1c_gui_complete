# Single cell analysis GUI #
The tool provides an interactive GUI that wraps up computational methods for single cell analysis into a step by step pipeline. Reference: https://www.biorxiv.org/content/10.1101/510222v1

## Installation:

GUI:

`git clone https://github.com/Ren22/1c_gui_complete.git`

Main package with the computational methods:

`git clone https://git.embl.de/nigmetzi/spaceM.git`

Put both directories into one next to each other.

<strong><em>Common to all systems:</em></strong>

- Use provided `requirements.txt` file from `./env_files` and install it with pip
- Install [metaspace](https://github.com/metaspace2020/metaspace/tree/master/metaspace/python-client) package from github
- Install [Fiji 2014 June 02](https://imagej.net/Fiji/Downloads)
</ul>
<strong><em>Windows:</em></strong>

Install [Cellprofiler 3.1.8](https://cellprofiler.org/releases/)

<strong><em>Ubuntu:</em></strong>  
Install [Cellprofiler 3.1.3](https://github.com/CellProfiler/CellProfiler/wiki/Conda-Installation) into the conda environment 

<strong><em>Requirements:</em></strong>  
As datasets can be quite heavy to process make sure you are using minimum:
- RAM: >=16 Gb
- CPUs: >=4
    
<strong><em>Check out more details and demo demonstration on:</em></strong>  
https://www.evernote.com/shard/s329/sh/ee15d31d-dc98-47e9-ac9b-cd6ec70eb600/59a06ef8ec67a62b231598f6ec7b6d3e
