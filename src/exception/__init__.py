import os,sys

class CustomeException(Exception):
    def __init__(self,error_message:Exception, error_details:sys):
        self.error_message = CustomeException.get_detailed_error_message(error_message=error_message,
                                                                         error_details=error_details)
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details:sys)->str:
        _, _, exce_tb = error_details.exc_info()

        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in execution of: 
        [{file_name}] at
        try block line number : [{try_block_line_number}]
        exception block line number : [{exception_block_line_number}]
        Error Message : [{error_message}]
        """ 

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomeException.__name__.str()