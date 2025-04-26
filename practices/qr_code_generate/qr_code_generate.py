"""
Write a program to generate a QR code based on user input, such as text or a
URL. The QR code should be saved as an image file that can be scanned with a
smartphone.

Optional Enhancements
• Add options for the user to choose the color of the QR code. This will allow
users to generate QR codes that match their style or branding.
• Implement a feature that lets the user generate multiple QR codes at once by
providing a list of URLs or texts. Each QR code should be saved with a unique
filename.
"""


#
# check type
    # input Define three color for user choose this
    # if correct
        # break choose
    # elif
        # print try again
# input Define style for user choose this
# input Define branding for user choose this
# Loop
    # input Ask you want to countinue 
    # input Text user wanna generate
    # Generate and save into file with date formate filename_ddmmyy_hhmmsssss png

from enum import Enum
import datetime, calendar
import qrcode, qrcode.constants
import qrcode.image.styles.colormasks as colorMasks
import qrcode.image.styledpil as styledpil
import qrcode.image.styles.moduledrawers as moduledDrawers
from pathlib import Path

ROOTDIR = Path(__file__).parent
class ColorStyle(Enum):
    black = "black"
    green = "green"
    white = "white"
    red = "red"
    
    def getRgb(self) -> tuple[int]:
        if self is ColorStyle.green:
            return (0, 100, 0)
        elif self is ColorStyle.red:
            return (205, 92, 92)
        elif self is ColorStyle.black:
            return (1, 1, 1)
        else:
            return (255, 255, 255)
  
while True:
    try:
        frontColorChoice = ColorStyle(input("What do you want front color {black, green, white, red}: ").lower())
        backColorChoice = ColorStyle(input("What do you want back color {black, green, white, red}: ").lower())
        break
    except ValueError:
        print("Invalid choice, try again! ")
while True:
    try:
        # PythonTraining/PythonTraining/practices/qr_code_generate/image_center.jpeg
        embeddedImage = str(input("Input path center image custom: "))
        break
    except ValueError:
        print("Invalid choice, try again! ")

qrCode = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H)
qrCode.add_data("Toi la hung")
qrCode.make(True)
img = qrCode.make_image(image_factory=styledpil.StyledPilImage,
                        color_mask=colorMasks.SolidFillColorMask(back_color=backColorChoice.getRgb(), front_color=frontColorChoice.getRgb()),
                        embeded_image_path = embeddedImage,
                        module_drawer=moduledDrawers.GappedSquareModuleDrawer())
try:
    currentDate = datetime.datetime.now()
    savePath = f"{ROOTDIR}/qrGenerated/{currentDate.strftime("asds_%d%m%Y_%H%M%S%f")}.png"
    img.save(savePath)
except FileNotFoundError:
    print("Invalid path, try again")
