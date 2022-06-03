class RunIdInfo():
    """ Class to store the run id and the file name 
    """
    file_name: str
    run_id: str
    base_file_name: str
    date: str
    def __init__(self, file_name: str, run_id: str, base_file_name: str, date: str) -> None:
        """Constructor

        Args:
            file_name (str): Name of the file to process
            run_id (str): Run id of the file
            base_file_name (str): Name of the file without extension and date
            date (str): Date of the run
        """
        self.file_name = file_name
        self.run_id = run_id
        self.base_file_name = base_file_name
        self.date = date
    
    def __str__(self) -> str:
        return "Run Id Info: \n file_name='{}'\n run_id='{}'\n base_file_name='{}'\n date='{}'\n".format(self.file_name, self.run_id, self.base_file_name, self.date)
    
class Attributes():
    """ Class to store the attributes of a run
    """
    internal_attributes: list
    external_attributes: list
    informational_attributes: list
    def __init__(self, internal_attributes: list, external_attributes: list, informational_attributes: list) -> None:
        """Constructor

        Args:
            internal_attributes (list): List of internal attributes
            external_attributes (list): List of external attributes
            informational_attributes (list): List of informational attributes
        """
        self.internal_attributes = internal_attributes
        self.external_attributes = external_attributes
        self.informational_attributes = informational_attributes
        
    @property
    def model_attributes(self):
        """ Returns the attributes to be used in the model
        
        Returns:
            list: List of attributes to be used in the model
        """
        return self.internal_attributes + self.external_attributes
    
    @property
    def all_attributes(self):
        """Returns all attributes
        
        Returns:
            list: List of all attributes
        """
        return self.internal_attributes + self.external_attributes + self.informational_attributes
    
    def __str__(self) -> str:
        return "Attributes: \n internal_attributes='{}'\n external_attributes='{}'\n informational_attributes='{}'\n".format(self.internal_attributes, self.external_attributes, self.informational_attributes)