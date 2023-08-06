
import pysimilar
import os

class Compare_Txt_Class:
    """_summary_
    compare all txt file in directory with pysimilar
    input:
        dir: directory with all text files to be compared.
    output:
       List files with comparision result 
       [['welcome.txt vs hi.txt', 0.6053485081062917],
        ['welcome.txt vs hello.txt', 0.0],
        ['hi.txt vs hello.txt', 0.0]]
    """
    def __init__(self, dir_txt:os.PathLike) -> None:
        self.dir_txt = dir_txt
        
    def do_compare(self)-> list:
        pysimilar.extensions= '.txt'
        comparison_result = pysimilar.compare_documents(self.dir_txt)
        return comparison_result
       
           