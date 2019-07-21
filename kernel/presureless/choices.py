class TicketStatus:
    """Check Open or Close Status of a post
    
    Arguments:
        is_charfield {[bool]} -- check for charfield models or positiveintegerfield
    """

    def __init__(self, is_charfield = True):
               
        if is_charfield:
            self.CLOSE = 'c'
            self.OPEN = 'o'
        else:
            self.CLOSE = 0
            self.OPEN = 1
        
    
    def is_open(self, value):
        """[summary]
    
        Arguments:
            Postable {[str, int]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        return True if value == self.OPEN else False
    
    def is_close(self, value):
        return True if value == self.CLOSE else False
    
    def get_close(self):
        return self.CLOSE
    
    def get_open(self):
        return self.OPEN
    
    def get_status(self):
        status = (
            (self.CLOSE, 'Close'),
            (self.OPEN, 'Open'),
        )

        return status
