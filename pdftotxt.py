from docling.document_converter import DocumentConverter

name = "your_file_name"
source_path = ".pdf"
source = name+source_path
converter = DocumentConverter()
result = converter.convert(source)

print(result.document.export_to_markdown())

print(result.document.export_to_document_tokens())

with open(name+".txt", "w", encoding='utf-8') as f:

    f.write("\n\nMarkdown Conversion:\n")

    f.write(result.document.export_to_markdown())