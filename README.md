# Ultra PDF

## 📄 Description
Ultra PDF is a powerful, user-friendly desktop application that provides comprehensive PDF manipulation capabilities. Built with Python, it offers a modern graphical user interface for handling all your PDF-related tasks.

## ✨ Features

### File Conversion
- Convert PDFs to Microsoft Word (DOCX)
- Convert PDFs to Excel formats
- Convert PDFs to PowerPoint presentations
- Export PDFs to various image formats (JPG, TIFF, PNG)
- Create PDFs from documents and images

### PDF Manipulation
- Merge multiple PDF files into one
- Split PDFs into individual pages
- Reorder, delete, and insert pages
- Rotate pages to any angle
- Extract specific pages
- Add page numbers
- Compress PDFs to reduce file size

### Security & Sharing
- Protect PDFs with passwords
- Add watermarks and logos
- Share files for e-signing
- Track e-signature responses
- Create and manage web forms

### Advanced Features
- OCR (Optical Character Recognition) for scanned documents
- Edit text and images within PDFs
- Bulk processing capabilities

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Required Libraries
```bash
pip install pillow
pip install PyPDF2
pip install pdf2docx
pip install PyMuPDF
pip install img2pdf
```

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/nhattan86/Ultra-PDF
cd ultra-pdf
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python ultra_pdf.py
```

## 🚀 Quick Start Guide

1. Launch the application
2. Use the "Select Files" button to choose PDF files
3. Selected files will appear in the listbox
4. Choose an operation from the available buttons
5. Follow any additional prompts
6. Find your processed files in the specified output location

## 💻 Usage Examples

### Converting PDF to Word
```python
# Select your PDF file
# Click "Convert to Word"
# Choose output location
# Wait for conversion to complete
```

### Merging PDFs
```python
# Select multiple PDF files
# Click "Merge PDFs"
# Choose output location
# Get your merged PDF
```

### Adding Password Protection
```python
# Select PDF file
# Click "Add Password"
# Enter your password
# Save protected PDF
```

## ⚙️ Configuration
No additional configuration is required for basic usage. The application uses default settings that work for most cases.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues
- Large PDF files may take longer to process
- Some features require additional memory for processing
- OCR accuracy depends on the quality of the original document

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛠️ Built With
- [Python](https://www.python.org/) - The programming language used
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI library
- [PyPDF2](https://pypdf2.readthedocs.io/) - PDF processing
- [pdf2docx](https://pdf2docx.readthedocs.io/) - PDF to Word conversion
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF manipulation
- [Pillow](https://python-pillow.org/) - Image processing

## 🔄 Version History
* 1.0.0
    * Initial Release
    * Basic PDF operations
* 1.1.0
    * Added OCR capabilities
    * Improved GUI
* 1.2.0
    * Added e-signature features
    * Performance improvements
