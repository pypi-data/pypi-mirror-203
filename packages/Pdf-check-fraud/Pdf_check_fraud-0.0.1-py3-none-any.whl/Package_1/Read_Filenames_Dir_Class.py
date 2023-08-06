import pathlib
import os

class Read_Filenames_Dir_Class:
    """
        Class Read all filename with certain extension:
         
    """  
    def __init__(self, the_dir:os.PathLike) -> None:
        self.the_dir = the_dir
    
    def search_all_files(self,the_extent) -> list:
        """

        Args:
            the_extent (_type_): _description_

        Returns:
            _type_: _description_
        """
        dirpath=pathlib.WindowsPath(self.the_dir)
        if not( "." in the_extent):
            the_extent = "."+ the_extent
        file_list =[]
        if dirpath.is_dir():
            for the_file in dirpath.iterdir():
                if the_file.is_file() and the_file.suffix == the_extent:
                    file_list.append(pathlib.WindowsPath(the_file))
            return file_list
        else:
            print(f"the directory {self.the_dir}is not a directory \n ")
            exit()
        