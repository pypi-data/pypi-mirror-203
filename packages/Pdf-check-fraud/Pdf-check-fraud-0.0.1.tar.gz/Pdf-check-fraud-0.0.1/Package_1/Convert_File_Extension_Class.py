import pathlib3x as pathlib
import os



class Convert_File_Extension_Class:
    def __init__(self, file_list_pdf:list,txt_dir:os.PathLike) -> None:
        self.file_list_pdf = file_list_pdf
        self.txt_dir = txt_dir 
    """
        creates a list with text files from a list of the PDF files
        to be checked. So that these text file can be checked for simularity

        Args:
            file_list_pdf (_list_): _list of pdf files_
            txt_dir (_windowspath_): _directory with the converted text files_

        Returns:
            _list_: _file list of all text files_
    """
        
    def convert_file_extension(self)-> list:
        file_list_txt=[]
        for thepdffile in self.file_list_pdf:
            file_name_stem = pathlib.WindowsPath(thepdffile).stem
            #print(f"self.txt_dir is: {self.txt_dir} \n file_name_stem is: {file_name_stem} \n" )
            path_file_name_stem = pathlib.PureWindowsPath(self.txt_dir,pathlib.WindowsPath(file_name_stem).append_suffix('.txt'))
            file_list_txt.append(path_file_name_stem)
        return file_list_txt
    