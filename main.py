import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
import PyPDF2
from pdf2docx import Converter
import img2pdf
import fitz  # PyMuPDF
import tempfile
from pathlib import Path

class PDFToolsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Tools Suite")
        self.root.geometry("1200x800")
        
        # Selected files
        self.selected_files = []
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File Selection Area
        file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
        file_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(file_frame, text="Select Files", command=self.select_files).grid(row=0, column=0, padx=5)
        ttk.Button(file_frame, text="Clear Selection", command=self.clear_selection).grid(row=0, column=1, padx=5)
        
        # Selected files listbox
        self.files_listbox = tk.Listbox(file_frame, height=5, width=80)
        self.files_listbox.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Conversion Options
        convert_frame = ttk.LabelFrame(main_frame, text="Convert PDF", padding="10")
        convert_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(convert_frame, text="Convert to Word", command=self.convert_to_word).pack(fill=tk.X, pady=2)
        ttk.Button(convert_frame, text="Convert to Images", command=self.convert_to_images).pack(fill=tk.X, pady=2)
        ttk.Button(convert_frame, text="Convert to PowerPoint", command=self.convert_to_ppt).pack(fill=tk.X, pady=2)
        
        # PDF Operations
        operations_frame = ttk.LabelFrame(main_frame, text="PDF Operations", padding="10")
        operations_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(operations_frame, text="Merge PDFs", command=self.merge_pdfs).pack(fill=tk.X, pady=2)
        ttk.Button(operations_frame, text="Split PDF", command=self.split_pdf).pack(fill=tk.X, pady=2)
        ttk.Button(operations_frame, text="Compress PDF", command=self.compress_pdf).pack(fill=tk.X, pady=2)
        ttk.Button(operations_frame, text="Add Password", command=self.add_password).pack(fill=tk.X, pady=2)
        
        # PDF Editing
        edit_frame = ttk.LabelFrame(main_frame, text="PDF Editing", padding="10")
        edit_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(edit_frame, text="Rotate Pages", command=self.rotate_pages).pack(fill=tk.X, pady=2)
        ttk.Button(edit_frame, text="Extract Pages", command=self.extract_pages).pack(fill=tk.X, pady=2)
        ttk.Button(edit_frame, text="Add Page Numbers", command=self.add_page_numbers).pack(fill=tk.X, pady=2)
        
        # OCR and Forms
        ocr_frame = ttk.LabelFrame(main_frame, text="OCR & Forms", padding="10")
        ocr_frame.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(ocr_frame, text="OCR Scan", command=self.ocr_scan).pack(fill=tk.X, pady=2)
        ttk.Button(ocr_frame, text="Create Form", command=self.create_form).pack(fill=tk.X, pady=2)
        ttk.Button(ocr_frame, text="Add Logo", command=self.add_logo).pack(fill=tk.X, pady=2)

    def select_files(self):
        files = filedialog.askopenfilenames(
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        self.selected_files.extend(files)
        self.update_files_listbox()
        
    def clear_selection(self):
        self.selected_files.clear()
        self.update_files_listbox()
        
    def update_files_listbox(self):
        self.files_listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.files_listbox.insert(tk.END, os.path.basename(file))

    def convert_to_word(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "Please select PDF files first!")
            return
            
        for pdf_file in self.selected_files:
            output_file = pdf_file.rsplit('.', 1)[0] + '.docx'
            converter = Converter(pdf_file)
            converter.convert(output_file)
            converter.close()
        messagebox.showinfo("Success", "Conversion completed!")

    def convert_to_images(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "Please select PDF files first!")
            return
            
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return
            
        for pdf_file in self.selected_files:
            doc = fitz.open(pdf_file)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                output_file = os.path.join(output_dir, f"page_{page_num+1}.png")
                pix.save(output_file)
        messagebox.showinfo("Success", "Images extracted!")

    def merge_pdfs(self):
        if len(self.selected_files) < 2:
            messagebox.showwarning("Warning", "Please select at least 2 PDF files to merge!")
            return
            
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if not output_file:
            return
            
        merger = PyPDF2.PdfMerger()
        for pdf in self.selected_files:
            merger.append(pdf)
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Success", "PDFs merged successfully!")

    def split_pdf(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "Please select a PDF file to split!")
            return
            
        pdf_file = self.selected_files[0]
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return
            
        pdf = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf.pages)):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf.pages[page_num])
            output_file = os.path.join(output_dir, f"page_{page_num+1}.pdf")
            with open(output_file, 'wb') as out:
                pdf_writer.write(out)
        messagebox.showinfo("Success", "PDF split successfully!")

    def compress_pdf(self):
        messagebox.showinfo("Info", "Compression feature would go here")

    def rotate_pages(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "Please select a PDF file!")
            return
            
        angle = tk.simpledialog.askinteger("Rotate", "Enter rotation angle (90, 180, 270):", 
                                         minvalue=90, maxvalue=270)
        if not angle:
            return
            
        pdf_file = self.selected_files[0]
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        
        for page in pdf_reader.pages:
            page.rotate(angle)
            pdf_writer.add_page(page)
            
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_file:
            with open(output_file, 'wb') as f:
                pdf_writer.write(f)
            messagebox.showinfo("Success", "Pages rotated successfully!")

    def add_password(self):
        if not self.selected_files:
            messagebox.showwarning("Warning", "Please select a PDF file!")
            return
            
        password = tk.simpledialog.askstring("Password", "Enter password:", show='*')
        if not password:
            return
            
        pdf_file = self.selected_files[0]
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()
        
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
            
        pdf_writer.encrypt(password)
        
        output_file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if output_file:
            with open(output_file, 'wb') as f:
                pdf_writer.write(f)
            messagebox.showinfo("Success", "Password protection added!")

    def extract_pages(self):
        messagebox.showinfo("Info", "Page extraction feature would go here")

    def add_page_numbers(self):
        messagebox.showinfo("Info", "Page numbering feature would go here")

    def ocr_scan(self):
        messagebox.showinfo("Info", "OCR scanning feature would go here")

    def create_form(self):
        messagebox.showinfo("Info", "Form creation feature would go here")

    def add_logo(self):
        messagebox.showinfo("Info", "Logo addition feature would go here")

    def convert_to_ppt(self):
        messagebox.showinfo("Info", "PowerPoint conversion feature would go here")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToolsApp(root)
    root.mainloop()
