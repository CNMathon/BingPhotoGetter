# getBingPhoto
Python applet that exists in order to get the Bing daily wallpaper.

## Quick Start
### Installation dependency file
```
pip install requests
pip install bs4
```

### Select image storage directory
> This is the default and recommended file storage path for the project. 
> If you need to change it, you can modify the value of the variable directly in the ```app.pyw``` file. 
> But what needs to be noted is the slash direction in the file path(especially for Windows users).
```
file_folder = 'C:/Users/Mathon/Pictures/BingWallpapar'
```

### Daily download
- Windows
  - Use Task scheduler in the control panel of Windows to automate projects.
- Linux & Mac
  - GUN