# usb-speed-auto-checker

## Description
This script tests the read and write speed of a USB device by creating and measuring the time to read/write a file with size 1 MB and 1 GB. The script detects all available USB devices and selects the first one in the list as the test device.

## Installation and Setup
To run the script, follow these steps:
1. Clone the repository to your local machine `git clone https://github.com/username/repository.git`
2. Navigate to the directory where the repository was cloned.
3. Install dependencies by running `pip install -r requirements.txt`.
4. Connect a USB device to your computer
5. Run the script by executing `python speed_test.py`

## Improvements
Here are some improvements that could be made to this script:
- Add support for non-removable disks
- Implement multi-threading to speed up the testing process
- Allow users to select which USB device to test if multiple ones are detected

## Requirements
The script requires the following packages to be installed:
- psutil==5.8.0
