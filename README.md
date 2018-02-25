# HackerCamp-Summer-2018
## Infrastructure Engineering Assignment

Assignment in the HackerCamp Summer 2018(Infrastructure Engineering)

Requirements:
```
python3
```

There are 3 python script files included in this assignment.
  - ScanFiles.py is a python script which scans the folder recursively. The folder or the drive to be scaned must be given as a command-line arguments passed to the script and it will make a corresponding log file with in the same folder.
    To run the code:
    ```
    python3 ScanFiles.py /home
    ```
  - LargestFIle.py is the python script which identifies the 10 files which has the lasgest size in the given folder. The folder or the drive to be scaned must be given as a command-line arguments passed to the script and it will print the desired output.
    To run the code:
    ```
    bash
    python3 LargestFIle.py /home
    ```
    Output:
    ```
    bash
    Name and location of the file:  /home/lashuk/Downloads/Softwares/onlyoffice-desktopeditors_amd64.deb
    Size of the file:  158.7 MB 

    Name and location of the file:  /home/lashuk/Downloads/Softwares/atom-amd64.deb
    Size of the file:  78.0 MB 

    Name and location of the file:  /home/lashuk/Downloads/Softwares/boostnote_0.9.0_amd64.deb
    Size of the file:  46.7 MB 

    Name and location of the file:  /home/lashuk/Downloads/franz_5.0.0-beta.16_amd64(1).deb
    Size of the file:  45.3 MB 

    Name and location of the file:  /home/lashuk/Downloads/franz_5.0.0-beta.16_amd64.deb
    Size of the file:  45.3 MB 

    Name and location of the file:  /home/lashuk/Downloads/Softwares/code_1.20.1-1518535978_amd64.deb
    Size of the file:  42.2 MB 

    Name and location of the file:  /home/lashuk/Downloads/everdo_0.18.0_amd64.deb
    Size of the file:  41.5 MB 

    Name and location of the file:  /home/lashuk/Documents/pdf/matlab_prog.pdf
    Size of the file:  5.8 MB 

    Name and location of the file:  /home/lashuk/Documents/pdf/matlab_tutorial.pdf
    Size of the file:  2.5 MB 

    Name and location of the file:  /home/lashuk/Downloads/Softwares/privoxy_3.0.20-1_amd64.deb
    Size of the file:  628.0 KB
    ```
  - Sort_Move.py is the python script to rearrange files in given desktop into documents. The files are sorted based on their extensions and are moved to folders (for each different type of extension). If it encounters a new file type, it will create a new folder.
    To run the code:
    ```
    bash
    python3 Sort_Move.py
    ```
