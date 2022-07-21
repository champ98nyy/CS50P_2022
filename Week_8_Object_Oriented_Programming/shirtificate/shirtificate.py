# CS50P 2022 - PSET 8
# CS50 CS50 Shirtificate

"""
Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called
shirtificate.pdf similar to this one for John Harvard, with these specifications:

    • The orientation of the PDF should be Portrait
    • The format of the PDF should be A4, which is 210mm wide by 297mm tall
    • The shirt’s image should be centered horizontally
    • The user’s name should be on top of the shirt, in white text
    • The top of the PDF should “CS50 Shirtificate” as text, centered horizontally

All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely.
And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface)
to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!
"""

from fpdf import FPDF


class Shirtificate:

    # Initialize a shirtificate with the user's name on it
    def __init__(self, name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font('helvetica', 'B', 40)
        self.pdf.cell(0, 60, 'CS50 Shirtificate', new_x='LMARGIN', new_y='NEXT', align='C')
        self.pdf.image('shirtificate.png', h=self.pdf.eph/1.42)
        self.pdf.set_font_size(24)
        self.pdf.set_text_color(255, 255, 255)

        # Add text to t-shirt, using white-stroked font
        with self.pdf.local_context(text_mode='STROKE', line_width=1.5):
            self.pdf.set_draw_color(255, 255, 255)
            self.pdf.cell(190, -250, txt=f'{name} TOOK CS50', align='C')

    # Save final pdf file
    def save(self, name):
        self.pdf.output(name)

# Request user to input name, capitalize all letters and remove leading/trailing white space
name = input('Name: ').upper().strip()

# Create new Shirtificate object with the user's name
certificate = Shirtificate(name)

# Save certificate
certificate.save('shirtificate.pdf')