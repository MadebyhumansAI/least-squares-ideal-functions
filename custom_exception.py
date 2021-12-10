class CustomException(Exception):
    
    '''
    In this class we created our own exceptions to raise when necessary.
    '''

    def __init___(self, exception_parameter, exception_message):
        
        super().__init__(self, exception_parameter, exception_message)