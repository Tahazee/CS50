import fpdf.fpdf
import fpdf.enums
pdf=fpdf.FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
inp=input("Enter your name: ").upper()

# Title
pdf.cell(200, 10, txt="CS50 Shirtificate", ln=True, align="C")

pdf.image("shirtificate.png",w=100,h=200,x=(110/2))
pdf.set_font("Arial", size=12, style="B")
pdf.set_text_color(255,255,255)

pdf.text(x=80, y=80, txt=inp)
pdf_width=210
image_width=100


pdf_file_path = "shirtificate.pdf"
pdf.output(pdf_file_path)
