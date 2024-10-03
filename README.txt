Running the Program
This code takes terminal responses. To run the program, follow these steps:
1. Open project up in a python supported IDE.
2. Run main.py: Locate the file named main.py within your project directory. Use the "Run" functionality provided by your IDE to execute this script.
3. Provide Input: When prompted, enter the desired filenames for the files to be generated.
4. File Generation: Once the program finishes processing, the generated files will be available in the same project directory.

Assumptions made
1. The lookup csv does not have any trailing or leading whitespace in it except newlines.
2. The flow log data is in .txt format.
3. There are no trailing or leading whitespace in the example.txt except newline
4. All data files is compact (i.e, entries are not separated by another newline )
5. Only Version 2 of flow log data has been tested
6. Default Logs were used for testing only

Testing
Testing has only been done with the default logs. No unit testing has been made.

Analysis
All functions meet the standard of a time complexity of O(n) for parsing and creation.
Space complexity is around O(n) to O(n^2).
