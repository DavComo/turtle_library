Illustrator Export:  
    Firstly, create any file in illustrator. 
    Note that you cannot use curves, only straight lines. The only exception to that is circles which cannot be ovals.
    Then, select all the shapes in the document (Except the circles) and click:
        Object > Shape > Expand Shape
    and then:
        Object > Path > Add Anchor Points
    Then, go to:
        File > Export > Export As... 
    and make sure you use SVG as your file export format.
    Once you have exported your file, go to the main.py file and change the 'file_dir' variable to the absolute or relative path of your .svg file.
    You can get the absolute path of your .svg file by two-finger clicking on it, then holding 'option' key and click 'Copy filename.svg as Pathname'
    After clicking export, an 'SVG Options' window should show up. Make sure to select 'Presentation Attributes' for the 'Styling' option. And then click 'Ok'
    Lastly, run the main.py file and you'll see your .svg file be drawn by turtle.


!Important!
    There is a way to add objects that don't have straight lines only and aren't circles, although it is experimental.
    Select the object and go to:
        Object > Path > Add Anchor Points
    and repeat this step a few more times. The more times you do this, the less sharp the corners will be in the next step but the longer they will take to draw. x5 is recommended. Next, go to:
        Path > Simplify...
    and click the three dots to open the expanded menu. Next, select the 'Convert to Straight Lines' and turn down the 'Corner Point Angle Threshold' to 0 degrees.
    You can then export the file as mentioned above. 
    Keep in mind this method makes circle and rectangle functions in the svg_parser.py file useless and converts all shapes to polygons, but doesn't work with objects called "Compound Path" in illustrator.


Progress Information:
    Drawing "example1.svg"; 13.4%; Object #31/313 (76%)
        "example1.svg" : Name of file with extension
        13.4% : Overall file progress
        Object #31/313 : Index of the object currently being drawn out of the total
        (76%) : Object progress
    Number of digits after decimal point can be adjusted using the 'progress_digits' variable in the main.py file
