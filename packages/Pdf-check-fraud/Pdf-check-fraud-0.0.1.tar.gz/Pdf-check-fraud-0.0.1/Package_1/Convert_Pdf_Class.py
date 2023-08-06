from pypdf import PdfReader
from typing import BinaryIO



class Convert_Pdf_Class:
    def __init__(self,fname: BinaryIO) -> None:
        self.fname = fname 
    """
    concert pdf to text file. 
    function is called from convertMultiple
    
    Args:
        fname (_filepointer_): pdf file to convert
        pages (_type_, optional): _description_. Defaults to None.

    Returns:
        filepointer : txt file converted pdf
    """
    def do_convert(self) -> str:
        pdf = PdfReader(self.fname)
        number_of_pages = len(pdf.pages)
        text_all = ''
        # print (f"number of pages {number_of_pages}")
        for pagenr in range(0, number_of_pages):
            # comment: 
            page =  pdf.pages[pagenr]
            text = page.extract_text()
            text_all = text_all + text
        # end for
        return (text_all)
        

    

        
    
# end of convert
