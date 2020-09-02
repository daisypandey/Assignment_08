#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# Daisy Pandey, August 31, 2020, created file
# Daisy Pandey, August 31, 2020, added pseudocode
# Daisy Pandey, September 1, 2020, Added code to class CD, class FileIO, and class IO, Created and added code to class DataProcessor
# Daisy Pandey, September 1, 2020, Added code to main body of script, used pickle module to store and load information as binary information 
# Daisy Pandey, September 1, 2020, Added structured error handiling to handle errors, updated docstrings 
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []     # list of Object to hold data
objFile = None          # file object

class CD:
    """Stores data about a CD:

    properties:
        cdId: (int) with CD ID
        cdTitle: (string) with the title of the CD
        cdArtist: (string) with the artist of the CD
        
    methods:
        getters: allows to access the private attributes 
        setters: allows to set the value to private attributes
        __str__(): returns a string representation of the object
    """
    # Initialize Component of the CD class
    def __init__(self, intId, strTitle, strAtrist):
        
        # private variables 
        self.__cdId = int(intId)
        self.__cdTitle = strTitle.title()       #title() -> Return a version of the string where each word is titlecased.
        self.__cdArtist = strAtrist.title()
    

    # Getters and Setters Properties Decorators for CD id, title, and artist   
    # getter method to get the properties using an object
    @property
    def cdId (self):
        return self.__cdId
    # setter method to change the value 'id' using an object
    @cdId.setter
    def cdId (self, id):
        self.__cdId = int(id)
    
    # getter method to get the properties using an object    
    @property
    def cdTitle (self):
        return self.__cdTitle
    # setter method to change the value 'title' using an object
    @cdTitle.setter
    def cdTitle (self, title):
        self.__cdTitle = title
    
    # getter method to get the properties using an object  
    @property
    def cdArtist (self):
        return self.__cdArtist
    # setter method to change the value 'artist' using an object
    @cdArtist.setter
    def cdArtist (self, artist):
        self.__cdArtist = artist
        
    def __str__(self):
        return f'{self.cdId}\t{self.cdTitle} (by:{self.cdArtist})'      

# -- PROCESSING -- #
class DataProcessor:
    """Adding CD data to the inventory"""
     
    @staticmethod 
    def add_data(strID, strTitle, strArtist, table):
        """Function to add data to the 2D table (list of CD objects) 
        
        Handles ValueError exception type for negative and non-numeric values
       
        Args: 
            StrID (string): Input parameter for CD ID. 
            Strtitle (string): Input parameter for CD Title.
            StArtist (string): Input parameter for CD Artist.
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime
            
          Returns: 
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime
        """               
        # Handling exception for negative numbers and string values
        try:
            intID = int(strID)  
            if intID <= 0:
                raise ValueError
        except ValueError:            
            print('====Error!!=====')
            print(f'You entered {strID}, which is not a valid entry for ID.')
            print('Please enter a number that is greater than zero.')
            print()
            return
        
        # Add item to the table
        cdId = strID
        cdTitle = strTitle
        cdArtist = strArtist
        addCd = CD(cdId, cdTitle, cdArtist)
        table.append(addCd)
        return table
            
class FileIO:    
    """Processes data to and from file:

    properties:

    methods:
        write_file(file_name, table): -> None
        read_file(file_name): -> (a list of CD objects)

    """
    """Processing the data to and from binary file"""

    @staticmethod
    def read_file(file_name):
        """Function to manage data ingestion from binary file to a list of CD objects

        Reads the data from a binary file identified by file_name into a 2D table (list of CD objects)
      

        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime

        Returns:
            data
        """
        # Load exisitng data from binary file        
        with open(file_name, 'rb') as objFile:
            data = pickle.load(objFile)           
            return data

    @staticmethod
    def write_file(file_name, table):
        """Function to save data to a binary file
        
        Writes the data to a binary file identified by file_name into a 2D table (list of CD objects)
             
        Args:
            file_name(string): name of file used to write the data to 
            table(list of CD objects): 2D data structure (list of CD objects) that hold the data during runtime
            
        Returns:
            None
        """
        # Save data to a binary file              
        with open(file_name, 'wb') as objFile:
            pickle.dump(table, objFile)    

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime.

        Returns:
            None.
        """
        # Display current inventory
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
        
    @staticmethod
    def get_userInput():
        """Function to get user input for ID, CD title, and CD artist
        
        Args:
            None.
            
        Returns:
            StrID (string): Input for CD ID. 
            Strtitle (string): Input for CD Title.
            StArtist (string): Input for CD Artist.
        """
        # Ask user for new ID, CD Title and Artist
        strID = input('Enter ID: ').strip()               
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist
    
# -- Main Body of Script -- #
# When program starts, read in the currently saved Inventory if exist, if not create one
# If file does not exist, handle error with FileNotFoundError exception
try:
    lstOfCDObjects = FileIO.read_file(strFileName)
except FileNotFoundError:
    FileIO.write_file(strFileName, lstOfCDObjects)

# Start main loop
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

# Process menu selection
    # Process exit first
    if strChoice == 'x':
        break
    
    # Process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects.clear()
            table = FileIO.read_file(strFileName)
            lstOfCDObjects.extend(table)
            IO.show_inventory(lstOfCDObjects) # Display Inventory to user
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects) 
        continue  # start loop back at top.
    
    # Process add a CD
    elif strChoice == 'a':
        # Store user inputs
        userInputId, userInputTitle, userInputArtist = IO.get_userInput()
        
        # Add data to the 2D table (list of CD objects)      
        DataProcessor.add_data(userInputId, userInputTitle, userInputArtist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects) 
        continue  # start loop back at top.
    
    # Process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects) 
        continue  # start loop back at top.
                
    # Process save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            FileIO.write_file(strFileName, lstOfCDObjects) # Calling write_file function 
            print('Data saved to file.')
            print()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # Catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
