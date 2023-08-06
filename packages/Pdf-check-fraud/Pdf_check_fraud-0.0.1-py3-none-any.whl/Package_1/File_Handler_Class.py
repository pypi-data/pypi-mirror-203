
import sys
import csv
import os


"""
        class file_handler
"""
class File_Handler_Class:
    """
    Handles files read write csv files
    input: file name
    ouput: none
    """  
    def __init__(self,file_name:os.PathLike,data_file:str) -> None:
        self.file_name = file_name
        self.data_file = data_file
     
    

    def write_file(self,modus)-> None:
        """_summary_

        Args:
            file_name (_type_): _description_
            data_file (_type_): _description_
        """
        try:
            result_file_fp = open(self.file_name,  newline='', mode= modus,encoding='utf-8')
        except (IOError, OSError) as e:
            print(f"Error writing to file {self.file_name} with error nr {e.errno} {e.strerror}\n")
            sys.exit()
        result_file_fp.write(self.data_file)
        result_file_fp.close()
    
    def csv_writer(self,header) -> None:
        """
    function to write to csv_file 
    Args:
       header (_list_): _description_
    """
        try:
            with open(self.file_name, newline='', mode='w') as csvfile:
                try:
                    scorewriter = csv.writer(csvfile, delimiter=';')
                    scorewriter.writerow(header)
                    for result in self.data_file:
                        scorewriter.writerow(result)
                except (IOError) as e:
                    print(f"Error writing to file {csvfile} with errornr: {e.errno} {e.strerror}\n")
                csvfile.close()
        except (IOError) as e:
            print(f"Error opening file with errornr:{e.errno} {e.strerror}\n")
      
# end of csv_write_file function
