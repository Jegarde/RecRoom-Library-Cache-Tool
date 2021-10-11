# RecRoom-Cache-Library-Tool
A handy tool to deal with the Library cache file.

![image](https://user-images.githubusercontent.com/13438202/136818657-6e35aa2c-04d2-4fba-99fa-49b50540b54a.png)

# Features
- Parse Library cache
- Remove Library cache

# Parsing
The script parses the Library cache file into a readable format. 
It categorizes every URL by their file extension. (`.png`, `.jpg`, `.room` etc.) It also displays the file's cache date.
Once done parsing, it exports the parsed library in a `.txt` file. This may change in the future to be easier to work with.

![image](https://user-images.githubusercontent.com/13438202/136818861-80294c44-6cd9-406b-a1d7-e015cfb5832b.png)

# Locating the Library file
The script tries to automatically locate the Library file from AppData. `%userprofile%\AppData\LocalLow\Against Gravity\Rec Room`
However, the script prioritizes files found in the same directory. Remember, that the cache file MUST be named 'Library' without any file extensions.
If the Library file can't be found from AppData, try launching Rec Room and opening the Play tab.
