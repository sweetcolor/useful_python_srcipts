# useful_python_scripts
some useful scripts for different home admin works

## Script "list_directory_with_file_sizes"

#### Overview

This script print directory list with files sizes in readable view
like this

    [download]
      [download/Photo]
        abstract-grunge-butterflies.jpg  --  6.60 Mb
        alps-dolomites-mountain.jpg  --  825.60 Kb
        anri-edmon-kross-cypress.jpg  --  4.54 Mb
      [download/wallpaper]
        germany-frankfurt-germaniya.jpg  --  757.11 Kb
        0170104.jpg  --  324.50 Kb
        [download/wallpaper/New]
          0310003.jpg  --  200.81 Kb
          0310018.jpg  --  1.12 Mb
          0310022.jpg  --  1.51 Mb

Also script create .txt file with directory name, which consist same list
#### Using

    python3 list_directory_with_file_sizes.py -r <dir_name>
    
#### Parameters
##### -r
Reverse walking all subdirectory

## Script "move_images"

#### Overview

This script move all images in directory and subdirectories 
in new images folder same subdirectories 

#### Using

    python3 move_images.py <dir_name>
    
This script remove some Windows trashes file
like Zone.Identifier, Thumbs.db and Thumbs.db:encryptable

#### Using

    python3 move_images.py -d <dir_name>

#### Parameters
##### -d
directory with trash

##### -h
help info

## License

BSD v3 License