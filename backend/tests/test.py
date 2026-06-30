from loaders.pdf_loader import PDFLoader

loader = PDFLoader()

doc = loader.load(
    "uploads/pdf/sample.pdf"
)

print(doc.metadata)

print(doc.pages[0])

print(len(doc.pages))