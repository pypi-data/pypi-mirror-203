# Declare smartsheet functions
import requests
import json
from decimal import Decimal
import re
import datetime
#####################

#Initialize smartsheet class
class SmartSheet():

    """
    A class representing the Smartsheet API.
    
    Attributes:
    - sheet_id (int): the ID of the Smartsheet.
    - api_token (str): the API token for authorization.
    - api_url (str): the API URL for the Smartsheet.
    - std_header (dict): the standard header to be sent with each request.
    
    Methods:
    - get_sheet(): gets the sheet details.
    - add_smartsheet_row(payload): adds a new row to the Smartsheet.
    - delete_smartsheet_row(row_id): deletes a row from the Smartsheet.
    - sheet_column_ids(): gets the column IDs of the Smartsheet.
    - sheet_row_ids(): gets the row IDs of the Smartsheet.
    - get_column_info(columnid): gets the details of a specific column.
    - get_column_values(column_name_list): gets the values of specific columns.
    - update_cell_text(row_id, column_id, value): updates the value of a cell in the Smartsheet.
    - column_names(): gets the column names of the Smartsheet.
    - get_sheet_row(row_id): gets the details of a specific row.
    - update_row(payload): updates the values of a row.
    - upload_attachment(row_id, attachment, filename): uploads an attachment to a specific row.
    - get_sheet_attachments(): gets the attachments of the Smartsheet.
    - update_attachment(attachment, filename, attachmentId): updates an attachment of the Smartsheet.
    - get_attachment_url(attachment_id): gets the download URL for a specific attachment.
    - list_attachment_versions(attachment_id): gets the versions of a specific attachment.
    - delete_attachment(attachment_id): deletes a specific attachment.
    - column_dictionary(column_names, column_ids): creates a dictionary of columns and their IDs.
    - add_columns(payload): adds new columns to the Smartsheet.
    - add_rows_payload_creater(data, column_headers, add_row_position, additional_settings): creates a payload to add new rows to the Smartsheet.
    """


    def __init__(self, sheet_id, api_token):
        """
        Initializes a new Smartsheet object with the given sheet ID and API token.
        """

        self.api_url =  "https://api.smartsheet.com/2.0/"
        self.api_token = api_token
        self.std_header =  {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}  
        self.sheet_id = sheet_id
    

    def get_sheet(self) -> dict:
        """
        Gets the details of the Smartsheet.
        
        Returns:
        - dict: the sheet details.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def add_smartsheet_row(self, payload: list) -> dict:
        """
        Adds a new row to the Smartsheet.
        
        Parameters:
        - payload (dict): the row data to be added to the Smartsheet.
        
        Returns:
        - dict: the response data from the API call.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/rows"
        payload = json.dumps(payload, default=json_decode_handler)
        r = requests.post(api_url, headers=self.std_header, data=payload)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def delete_smartsheet_row(self, row_id: int) -> dict:
        """Deletes the row with the specified ID.

        Args:
            row_id (int): The ID of the row to delete.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/rows?ids={row_id}"
        r = requests.delete(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def sheet_column_ids(self) -> list:
        """Gets a list of column IDs for the specified sheet.

        Returns:
            list: A list of column IDs.
        """
        sheet = self.get_sheet()
        col_ids = []
        for columns in sheet["columns"]:
            col_id = columns["id"]
            col_ids.append(col_id)
        return col_ids


    def sheet_row_ids(self) -> list:
        """Gets a list of row IDs for the specified sheet.

        Returns:
            list: A list of row IDs.
        """
        sheet = self.get_sheet()
        row_ids = []
        for row in sheet["rows"]:
            row_id = row["id"]
            row_ids.append(row_id)
        return row_ids


    def get_column_info(self, columnid: int) -> dict:
        """
        Retrieves information about a specific column in the Smartsheet sheet.

        Args:
            columnid (int): The ID of the column to retrieve information about.

        Returns:
            dict: A dictionary containing information about the requested column.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/columns/{columnid}"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()
    
    
    def get_column_values(self, column_name_list: list) -> dict:
        """
        Retrieves the values for the specified columns in the Smartsheet sheet.

        Args:
            column_name_list (list): A list of column names for which to retrieve values.

        Returns:
            dict: A dictionary containing the values for the specified columns.
        """
        self.get_sheet() 
        row_ids = self.sheet_row_ids()
        col_names = self.column_names() 
        col_ids = self.sheet_column_ids()
        num_cols = len(col_ids)
        col_range = list(range(num_cols))
        col_index_dict = create_dictionary_fr_list(col_names, col_range)
        master_data_dict = dict.fromkeys(column_name_list)#create dictionary of with keys of column names
        for key in master_data_dict.keys():
            master_data_dict[key] = []

        for key in list(col_index_dict.keys()):#remove columns that are not needed from dictionary
            if key not in column_name_list:
                col_index_dict.pop(key)

        for row_id in row_ids:
            data = self.get_sheet_row(row_id)
            for col_name, col_index in col_index_dict.items():
                try:
                    master_data_dict[col_name].append(data["cells"][col_index]["value"])
                except KeyError:
                    master_data_dict[col_name].append("")
        
        return master_data_dict


    def update_cell_text(self, row_id, column_id, value):
        """
        Updates the text value of a cell in a row with the given row ID and column ID.

        Args:
            row_id (int): The ID of the row containing the cell to update.
            column_id (int): The ID of the column containing the cell to update.
            value (str): The new text value to set for the cell.

        Returns:
            dict: A dictionary containing information about the updated row, including its ID and a list of updated cells.

        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/rows"
        payload = json.dumps([{"id": row_id, "cells": [{"columnId": column_id, "value": value}]}])
        r = requests.put(api_url, headers=self.std_header, data=payload)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def column_names(self):
        """
        Creates a new Smartsheet with the given name in the specified folder.

        Args:
            folderid (int): The ID of the folder in which to create the new Smartsheet.
            api_token (str): The API token to use for authentication.
            name (str): The name to give to the new Smartsheet.

        Returns:
            None
        """
        sheet = self.get_sheet()
        column_names = []
        for columns in sheet["columns"]:
            column_names.append(columns["title"])
        return column_names


    def get_sheet_row(self, row_id):
        """
        Retrieves the details of a single row in the specified Smartsheet.
        
        Args:
        - row_id (int): The ID of the row to retrieve.
        
        Returns:
        - dict: A dictionary containing the row data, including its cells.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/rows/{row_id}"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def update_row(self, payload):
        """
        Updates a row in the Smartsheet specified by the provided payload.
        
        Args:
        - payload: A dictionary containing the row data to update. It should have the following format:
            {
                "id": [row_id],
                "cells": [
                    {
                        "columnId": [column_id],
                        "value": [new_value]
                    },
                    ...
                ]
            }
        
        Returns:
        - A dictionary containing the updated row data.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/rows"
        payload = json.dumps(payload, default=json_decode_handler)
        r = requests.put(api_url, headers=self.std_header, data=payload)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def upload_attachment(self, row_id, attachment, filename):
        """
        Uploads an attachment to a row in a Smartsheet sheet.

        :param row_id: The ID of the row to attach the file to.
        :type row_id: str
        :param attachment: The path to the file to attach.
        :type attachment: str
        :param filename: The name of the file to attach.
        :type filename: str
        :return: A dictionary containing information about the attachment.
        :rtype: dict
        """
        file_header = {"Authorization": f"Bearer {self.api_token}", "Content-Disposition": f"attachment; filename={filename}", "Content-Type": "application/pdf", "Content-Lenght": ""}
        api_url = f"{self.api_url}sheets/{self.sheet_id}/rows/{row_id}/attachments"
        with open(attachment, 'rb') as f:
            data = f.read()
            r = requests.post(api_url, headers=file_header, data=data)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def get_sheet_attachments(self):
        """
        Returns a JSON object containing metadata about all attachments associated with the current sheet.

        Returns:
            A JSON object containing metadata about all attachments associated with the current sheet.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/attachments"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def update_attachment(self, attachment, filename, attachmentId):
        """
        Uploads a new version of an attachment to a Smartsheet row.
        
        Args:
            attachment (str): The file path of the attachment to upload.
            filename (str): The name of the attachment file.
            attachmentId (str): The ID of the attachment to update.
        
        Returns:
            A dictionary containing the updated attachment information.
        """
        file_header = {"Authorization": f"Bearer {self.api_token}", "Content-Disposition": f"attachment; filename={filename}", "Content-Type": "application/pdf", "Content-Lenght": ""}
        api_url = f"{self.api_url}sheets/{self.sheet_id}/attachments/{attachmentId}/versions"
        with open(attachment, 'rb') as f:
            data = f.read()
            r = requests.post(api_url, headers=file_header, data=data)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def get_attachment_url(self, attachment_id):
        """
        Gets the download URL for a specific attachment.

        Args:
            attachment_id (str): The ID of the attachment.

        Returns:
            str: The URL to download the attachment.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/attachments/{attachment_id}"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        download_info = r.json()
        download_url = download_info["url"]
        return download_url 


    def list_attachment_versions(self, attachment_id):
        """
        Retrieves a list of versions of a specific attachment.

        Args:
            attachment_id (int): The ID of the attachment to retrieve versions of.

        Returns:
            dict: A dictionary containing information about the versions of the attachment, including the version ID and creation date.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/attachments/{attachment_id}/versions"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()


    def delete_attachment(self, attachment_id):
        """
        Deletes the attachment with the specified attachment ID from the sheet.

        Parameters:
            attachment_id (str): The ID of the attachment to be deleted.

        Returns:
            None: The function does not return anything. If the deletion was successful, the attachment will no longer exist in the sheet. If the deletion was not successful, an error message will be printed to the console.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/attachments/{attachment_id}"
        r = requests.delete(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)

    
    def column_dictionary(self, column_names, column_ids):
        """
        Given a list of column names and column IDs, create a dictionary that maps column names to their respective column IDs.
        
        Args:
            column_names (list): A list of strings representing column names.
            column_ids (list): A list of strings representing column IDs.
        
        Returns:
            dict: A dictionary with column names as keys and column IDs as values.
        """
        dictionary = dict(zip(column_names, column_ids))
        return dictionary

    
    def add_columns(self, payload):
        """
        Adds new columns to a Smartsheet sheet.

        Args:
            payload (dict): A dictionary containing the column specifications.

        Returns:
            dict: A JSON object containing the response from the Smartsheet API call.
        """
        api_url = f"{self.api_url}sheets/{self.sheet_id}/columns"
        payload = json.dumps(payload, default=json_decode_handler)
        r = requests.post(api_url, headers=self.std_header, data=payload)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()
    
    def add_rows_payload_creator(self, data: list, column_headers: list, add_row_position: str, additional_settings: dict, rows_to_skip: int) -> list:
            """
            Creates a payload for adding new rows to a Smartsheet.

            Args:
                data (list): A list of data to be added to the sheet. Each element of the list represents a new row.
                column_headers (list): A list of the column headers in the order they appear in the sheet.
                add_row_position (str): A string indicating whether new rows should be added at the top or bottom of the sheet.
                additional_settings (dict): A dictionary containing additional settings for the new rows, such as formatting or cell linking.

            Returns:
                list: A list of dictionaries containing the new row data.

            """
            # Make a copy of the data so we can modify it without changing the original list.
            new_data = []
            for row in data:
                new_data.append(list(row))
            
            # Get the IDs of the columns in the sheet, so we can map column headers to column IDs later.
            col_names = self.column_names()
            col_ids = self.sheet_column_ids()
            col_dict = self.column_dictionary(col_names, col_ids)

            add_payload = []
            rows_payload = []
            counter = 1
            
            #set rows to skip to 0 if not specified
            if rows_to_skip == None:
                rows_to_skip = 0

            # Regular expressions for matching decimal and percentage values in cells.
            decimal_regex = re.compile(r"\d+\.\d+")
            percent_pattern = re.compile(r"\d+%")

            # Loop over the rows of data, creating a payload for each row.
            for row in new_data:
                if counter > rows_to_skip:
                    col_counter = 0
                    for col in column_headers:
                        
                        # Check if the cell value is a decimal or percentage value, and convert it if necessary.
                        decimal_regex_test = decimal_regex.search(str(row[col_counter]))
                        datetime_test = isinstance(row[col_counter], datetime.datetime)

                        if decimal_regex_test and not datetime_test:
                            percent_test = percent_pattern.search(str(row[col_counter]))
                            if percent_test:
                                # Convert percentage value to decimal.
                                new_per_value = float(str(row[col_counter]).replace("%", ""))
                                rows_payload.append({"columnId": col_dict[col], "value": new_per_value})
                            else: 
                                # Convert decimal value to float.
                                new_dec_value = float(row[col_counter])
                                rows_payload.append({"columnId": col_dict[col], "value": new_dec_value})

                        # Check if the cell value is a datetime object, and format it if necessary.
                        if datetime_test:
                            new_value = row[col_counter].strftime("%m/%d/%Y")
                            rows_payload.append({"columnId": col_dict[col], "value": new_value})

                        # Otherwise, just add the cell value as-is.
                        elif not decimal_regex_test and not datetime_test:
                            rows_payload.append({"columnId": col_dict[col], "value": row[col_counter]})
                        col_counter += 1
                        
                    # Create a dictionary with the row data and additional settings, if any.
                    payload_dict = {
                        add_row_position: True,
                        "cells": rows_payload,
                    }
                        
                    if len(additional_settings) > 0:
                        add_payload.append({
                            **payload_dict,
                            **additional_settings
                        })
                    else:
                        add_payload.append({
                            **payload_dict
                        })
                    
                    rows_payload = []

                counter += 1 
            
            return add_payload


class SmartFolder:
    """
    A class for interacting with Smartsheet folders using the Smartsheet API.

    Attributes:
        folderid (int): The ID of the folder.
        api_token (str): The API access token for Smartsheet.

    Methods:
        get_folder(): Returns the metadata for the folder.
        create_folder(name: str): Creates a subfolder with the specified name in the current folder.
    """

    def __init__(self, folderid: int, api_token: str):
        """
        Initializes a new instance of the SmartFolder class.

        Args:
            folderid (int): The ID of the folder.
            api_token (str): The API access token for Smartsheet.
        """
        self.api_url = "https://api.smartsheet.com/2.0/folders"
        self.api_token = api_token
        self.std_header = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
        self.folderid = folderid

    def get_folder(self) -> dict:
        """
        Returns the metadata for the folder.

        Returns:
            dict: A dictionary containing the metadata for the folder.
        """
        api_url = f"{self.api_url}/{self.folderid}"
        r = requests.get(api_url, headers=self.std_header)
        if r.status_code != 200:
            print(r.status_code, r.text)
        return r.json()

    def create_folder(self, name: str):
        """
        Creates a subfolder with the specified name in the current folder.

        Args:
            name (str): The name of the new subfolder.
        """
        api_url = f"{self.api_url}/{self.folderid}/folders"
        r = requests.post(api_url, headers=self.std_header, data={"name": name})
        if r.status_code != 200:
            print(r.status_code, r.text)



def create_smartsheet(folderid, api_token, name):
    """
    Creates a new Smartsheet in the specified folder with the given name.

    Args:
        folderid (int): The ID of the folder in which to create the Smartsheet.
        api_token (str): The API token used to authenticate the request.
        name (str): The name to give the new Smartsheet.

    Returns:
        None

    """
    api_url = f"https://api.smartsheet.com/2.0/folders/{folderid}/sheets"
    header =  {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
    payload = {"name": name, "columns": [{"title": "Primary Column", "primary": True, "type": "TEXT_NUMBER"}]}
    payload = json.dumps(payload, default=json_decode_handler)
    r = requests.post(api_url, headers=header, data = payload)
    if r.status_code != 200:
        print(r.status_code, r.text)


def create_dictionary_fr_list(first_list, second_list):
    """
    Creates a dictionary that maps the elements of two lists together.

    Args:
        first_list (list): The list of keys to use in the dictionary.
        second_list (list): The list of values to use in the dictionary.

    Returns:
        dict: A dictionary mapping the elements of the two lists together.

    """
    dictionary = dict(zip(first_list, second_list))
    return dictionary


def json_decode_handler(obj):
    """
    Decodes JSON objects and converts Decimal values to floats.

    Args:
        obj (Any): The object to decode.

    Returns:
        Any: The decoded object.

    Raises:
        TypeError: If the object is not JSON serializable.

    """
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

