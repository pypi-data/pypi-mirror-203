## Documentation

## `Process`
Constructor for the Process class.
#### Arguments:
    • name (str)(optional): The name of the executable file for the specified process.
    • pid (int)(optional): The process ID.
    • handle (int)(optional): The process handle.
    • error_code (str)(optional): The error code from a process failure.
#### Returns:
    • Process: Process object
---
## `Process.open`
Open the process with the Query, Operation, Read and Write permissions and return the process handle.
#### Returns:
    • bool: True if the handle exists, False if it doesn't.
---
## `Process.close`
Closes the handle of the process.
#### Returns:
    • int: The last error code from the result after an attempt to close the handle.
---
## `Process.get_all_access_handle`
Gets full access handle of the process.
#### Returns:
    • any: handle of the process
---
## `Process.get_last_error`
Get the last error code.
#### Returns:
    • int: The last error code.
---
## `Process.get_pointer`
Get the pointer of a given address.
#### Arguments:
    • lp_base_address (hex): The address from where you want to get the pointer.
    • offsets List[hex](optional): a list of offets.
#### Returns:
    • int: The pointer of a give address.
---
## `Process.get_modules`
Get the process's modules.
#### Returns:
    • List[int]: A list of the process's modules adresses in decimal.
    • List: An empty list if the process is not open.
---
## `Process.get_base_address`
Get the base address of the process.
#### Returns:
    • hex: The base address of the process.
---
## `Process.thread`
Create a remote thread to the address.
#### Arguments:
    • address (int): The address used to create a thread.
---
## `Process.read`
Read data from the process's memory.
#### Arguments:
    • lp_base_address (int): The process's pointer.
#### Returns:
    • any: The data from the process's memory if succeed if not raises an exception.
---
## `Process.read_string`
Read data from the process's memory.
#### Arguments:
    • lp_base_address (int): The process's pointer.
    • length (int): The length of string
#### Returns:
    • any: The data from the process's memory if succeed if not raises an exception.
---
## `Process.read_byte`
Read data from the process's memory.
#### Arguments:
    • lp_base_address (int): The process's pointer {don't use offsets}
    • length (int)(optional): The length of the bytes to read
#### Returns:
    • List[hex]: The data from the process's memory if succeed if not raises an exception.
---
## `Process.write`
Write data to the process's memory.
#### Arguments:
    • lp_base_address (int): The process's pointer {don't use offsets}
    • value (int): The data to be written to the process's memory
#### Returns:
    • bool: It returns True if succeed if not it raises an exception.
---
## `Process.write_string`
Write data to the process's memory.
#### Arguments:
    • lp_base_address (int): The process' pointer.
    • string (str): The string to be written to the process's memory
#### Returns:
    • bool: It returns True if succeed if not it raises an exception.
---
## `Process.write_byte`
Write data to the process's memory.
#### Arguments:
    • lp_base_address (int): The process' pointer {don't use offsets}.
    • write_bytes (List[hex]): The byte(s) to be written to the process's memor
#### Returns:
    • bool: It returns True if succeed if not it raises an exception.
---
## `ReadWriteMemory`
Constructor for the ReadWriteMemory class.
#### Returns:
    • ReadWriteMemory: ReadWriteMemory object
---
## `ReadWriteMemory.get_process_by_name`
Get the process by the process executable's name and return a Process object.
#### Arguments:
    • process_name (str): The name of the executable file for the specified process.
#### Returns:
    • "Process": A Process object containing the information from the requested Process.
---
## `ReadWriteMemory.get_process_by_id`
Get the process by the process ID and return a Process object.
#### Arguments:
    • process_id (int): The process ID.
#### Returns:
    • "Process": A Process object containing the information from the requested Process.
---
## `ReadWriteMemory.enumerate_processes`
Get the list of running processes ID's from the current system.
#### Returns:
    • List: A list of processes ID's
---
## License

[MIT](https://choosealicense.com/licenses/mit/)

