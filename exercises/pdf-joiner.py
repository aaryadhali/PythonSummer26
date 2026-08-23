from pypdf import PdfWriter

merger = PdfWriter()

# List the PDFs you want to combine (in order)
pdf_files = ["C:/Users/aarya/Downloads/26-27specfincircumappeal.pdf", "C:/Users/aarya/Downloads/JaspalFinalExitPacket.pdf"]

for pdf in pdf_files:
    merger.append(pdf)

# Write the combined pages into a new file
merger.write("appeal_and_unemployment_proof.pdf")

# Close the merger to free up system resources
merger.close()

print("PDFs merged successfully!")