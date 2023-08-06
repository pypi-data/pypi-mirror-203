
# Class for program check simularity of pdf files
# ask for pdf dir and convert text files. These text files are used
# to be compared and the results are writen into a csv file
#
# jfh 22/3/2023
#
# ------------------- The New Way with history and clear -------------------
import PySimpleGUI as sg
import pathlib
import Package_1
import threading

"""

    Copyright 2021, 2022 PySimpleGUI
"""


class Create_Windows_Class:

    def __init__(self) -> None:
        self = self
        self.THREAD_KEY = '-THREAD-'
        self.DL_START_PDF_KEY = '-START CONVERTING PDF TO TEXT-'
        self.DL_START_TXT_SIM_KEY = '-START SIMULARITY CHECKING OF TEXT FILE'
        self.DL_END_KEY = '-END CONVERTING AND CHECKING-'
        self.DL_THREAD_EXITNG = '-THREAD EXITING-'

    def the_thread(self, window, values) -> None:
        """
        The thread that communicates with the application through the window's events.

        """
        #print(f"Items are: {pathlib.WindowsPath(values['-PDF-']) ,values['-TXT-'],values['-RESULT-']}")
        pdf_dir = pathlib.WindowsPath(values['-PDF-'])
        txt_dir = pathlib.WindowsPath(values['-TXT-'])
        result_file = pathlib.WindowsPath(values['-RESULT-'])                           
        # Data sent is a tuple of thread name
        window.write_event_value(self.THREAD_KEY, '*** The thread starts.... "converting and checking simularity" ***')
        #
        # Create instance of class read_filenames_dir_class
        theclass_pdf = Package_1.Read_Filenames_Dir_Class(pdf_dir)
        #
        # Call method search all pdf files of class and create pdf file list  
        pdf_file_list = theclass_pdf.search_all_files('pdf') 
        #print(f"file list is {pdf_file_list}\n")
        #
         # create instance of class concert file extension
        the_class_file_convert = Package_1.Convert_File_Extension_Class(pdf_file_list,txt_dir)
        # 
        # call function to create file list of all text files
        txt_file_list = the_class_file_convert.convert_file_extension()
        
        the_file_num = 0
        #
        # for all pdf file in pdf_file_list do
        #
        for pdf_file in pdf_file_list:
            fname = open(pdf_file,'rb')
            pdf_convert = Package_1.Convert_Pdf_Class(fname=fname)
            pdf_text = pdf_convert.do_convert()
            # print(f"pdf text is {pdf_text} \n")
            handlefiles = Package_1.File_Handler_Class(txt_file_list[the_file_num],pdf_text)
            handlefiles.write_file("a")
            the_file_num = the_file_num +1
        # Data sent is a tuple of thread name
        #
        # Create instance of compare_txt_class
        # print(f"compare-txt-class \n")
        comparecls = Package_1.Compare_Txt_Class(txt_dir)
        #
        # call function do_compare to compare all txt files in txt_dir
        comparison_result=comparecls.do_compare()
        #print(f"type of comparsion_result is {type(comparison_result)}\n")
        #print(f" the result is {comparison_result} \n")
        #
        # create instance of file_handler_class
        do_outputcls = Package_1.File_Handler_Class(result_file,comparison_result)
        #
        # create header of csv file
        header = ['Files', 'Simularity score']
        #
        # write result and header to csv file
        #print(f"write result to csv file \n")
        do_outputcls.csv_writer(header)
       # window.write_event_value(
       #     (self.THREAD_KEY, self.DL_START_TXT_SIM_KEY), 2)
        
        # Data sent is a tuple of thread name
        #print(f"key is {self.DL_END_KEY}\n")
        window.write_event_value(self.DL_END_KEY,'end of checking')
      
    

    
    def create_window(self):
        """_create window_

        Returns:
            _type_: _window_
        """
        layout = [[sg.Text('Select PDF directory input')],
                  [sg.Input(key='-PDF-',size=(50, 1), focus=True), sg.FolderBrowse()],
                  [sg.Text('Select Text ouput directory')],
                  [sg.Input(key='-TXT-',size=(50, 1)),sg.FolderBrowse()],
                  [sg.Text('Select ouput file')],
                  [sg.Input(size=(50, 1), key='-RESULT-')],
                  [sg.Text(key='-STATUS-')],
                  [sg.Button('Check'), sg.B('Clear'), sg.Button('Exit')]]

        return (sg.Window('Check PDF simularity', layout, finalize=True))

    def do_window(self):
        """_summary_
        """
        window = self.create_window()
    
        timeout = thread = False

        while True:
            event, values = window.read(timeout=timeout)
            #if event != sg.TIMEOUT_KEY:
            #   print (f" event is: {event}\n")
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == 'Check' and not thread:
                sg.user_settings_set_entry('-FOLDERPDF-', value=['-PDF-'])
                window['-PDF-'].update(value=sg.user_settings_get_entry('-PDF-'))
                sg.user_settings_set_entry('-FOLDERTXT-', value=['-TXT-'])
                window['-TXT-'].update(value=sg.user_settings_get_entry('-TXT-'))
                sg.user_settings_set_entry('-RESULTFILE-', value=['-RESULT-'])
                window['-RESULT-'].update(
                    value=sg.user_settings_get_entry('-RESULT-'))
                thread = threading.Thread(target= self.the_thread, args=(window,values),daemon=True)
                thread.start()
               # thread = window.start_thread(lambda: self.the_thread(
                #    window, values), (self.THREAD_KEY, self.DL_THREAD_EXITNG))
            elif event == 'Clear':
                sg.user_settings_set_entry('-FOLDERPDF-', '')
                window['-PDF-'].update(value='')
                sg.user_settings_set_entry('-FOLDERTXT-', '')
                window['-TXT-'].update(value='')
                sg.user_settings_set_entry('-RESULTFILE-', '')
                window['-RESULT-'].update(value='')
            elif event == self.THREAD_KEY:
                #print ('start checking')
                window['-STATUS-'].update(value='start checking')
            elif event == self.DL_END_KEY:
                thread.join(timeout=0)
                window['-STATUS-'].update(value='End checking')
                #print('Check finished\n')
                thread, message, progress, timeout = None, '', 0, None     # reset variables for next run
        window.close()

"""
def main():
    the_windows = Create_windows()
    the_windows.do_window()


if __name__ == "__main__":
    main()
"""