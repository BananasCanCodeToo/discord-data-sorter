# Discord Data Sorter
## What it's about
Easily Sort all messages you've sent on discord into more user friendly folders

## Prerequisites
* Nothing! Uses built in libraries from python

## Usage
1. Request Data from discord (Settings > Privacy & Safety)
2. Download your data (When it becomes available)
3. Copy and paste it into the `INPUT` folder
4. Run `SORT_FILES.py`
5. Look through your message data (Sorted by name instead of ID) in `OUTPUT`

## Debugging
* Your `INPUT`/`OUTPUT` folder should look something like this:
  - INPUT
    - account
      - user.json
      - avatar.jpeg
    - activity
      - analytics
      - modeling
      - reporting
      - tns
    - messages
      - A bunch of folders with numerical names
    - servers
      - A slightly less amount (Maybe more, it depends) of folders with numerical names
    - .gitkeepfolder
    - README.txt
  - OUTPUT
    - .gitkeepfolder
    - messages (Only Appears after you run the program)

* If you have any other errors, please feel free to make an issue request
