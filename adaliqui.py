from docx import Document

# Create a Document object
doc = Document()

# Content to add as a paragraph
ncontent = "This is the content of the paragraph."

# Add a paragraph with ncontent
doc.add_paragraph(ncontent)

# Save the document
doc.save('example.docx')
