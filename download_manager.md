# Download Manager

aim is to organize downloaded files into folders based on their type. for example: .png, .jpeg into images, .pdf into documents or folders, .temp into temporary folders etc.

## Logic

- phase-1: Keep watching the downloads folder for any new files.
- phase-2: When a new file is detected, read the extension of this file.
- phase-3: According to the extension, reallocate the file to a respective folder.

---

## visualization

    |-----------|
    | phase-1   |
    |-----------|
         |
         v
    |-----------|
    |  phase-2  |
    |-----------|
         |
         v
    |-----------|
    |  phase-3  |
    |-----------|

## Deep-dive into the visualisation

      |---------------------------------|
      |     count number of files       |<-------|
      |     in the folder (count)       |        |
      |---------------------------------|        |
                     |                           | NO
                     v                           |
           |---------------------|               |
 |-------->|        count>0      |---------------|
 |         |---------------------|
 |                   | YES
 |                   v
 |         |---------------------|
 |         |  read the file name |
 |         |  and get the ext    |
 |         |---------------------|
 |                   |
 |                   v
 |         |---------------------|
 |         |  k = extension      |
 |         |---------------------|
 |                    |
 |                    v
 |         |---------------------|
 |         | k in dict.keys()    |
 |         |---------------------|
 |                    |
 |            YES     |    NO
 |        ____________|______________
 |       |                           |
 |       v                           v
 |   |------------|           |-----------|
 |   | relocate to|           | move to   |
 |   | respective |           | 'others'  |
 |   |   folder   |           |  folder   |
 |   |------------|           |-----------|
 |         |_______________________|
 |                      |
 |                      |
 |                      v
 |              |----------------|
 |--------------| count= count-1 |
                |----------------|

---

### deep-dive into phase-1

  so we are basically counting the number of files in the downloads folder so that we know how many we have to sort.

- for that we are using a function from the `os library`.
- because we want to check every few seconds so that we know when there is a new file, we use a function from the `time library`.
- we store the number of files in the folder in a variable `count`, and check if `count>0`
  - if it is: we proceed to our next phase
  - if it is not: we go back to checking the number of files in the folder every few seconds.

### deep-dive into phase-2

  here we read the file name to get the extension of the file

- to read the extension, we use the `Path` function from the `pathlib library`, with which we can access the file name and its extension.
- we store the extension name into a variable `ext`.

### deep-dive into pahse-3

  this is where our organisation takes place

- we use the dictionary (key: value pairs) in python to map extensions to folders, for example: {".pdf": Path("C:\users\f1"), ".jpeg": Path("C:\users\f2"), ".png": Path("C:\users\f2")} etc. in a dictionary the values can be repeated but the keys cannot be.
- so we check if the `k` is amongst the keys of the dictionary or not:
  - if it is: we access the folder path through the key and store this file in the respective folder.
  - if it is not: we store the file in a separate folder for now, lets say 'others'.
- now we set the `count= count-1`, and go back to checking if `count>0`, and continue accordingly.

## progress

- whenever there is a new file in the downloads folder, it is being sorted, checks every 15 seconds and is working fine.
- also a seperate python code file, that when run can be used to sort another specific folder, by taking the path as input from the user, into the same folders that files are being sort into in the downloads folder.

## under process

- when there is a new folder inside the downlaods folder, our sim is to sort the files present inside the new folder.
- and to create a loop such that if there are more sub folders inside the new one, it'll check and do the same.

## future works

- customized sorting (as in the user gets to choose what folder to save this file in, just by pressing a few keys)
- create a new folder whenever needed on its own.
- zip
