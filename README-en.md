# DocSpector
## Keyword Finder for Texts in Documents

By Eric Schöbel

**DocSpector** is a PyQt5-based desktop application designed to search for keywords in various document types within a specified directory (and its subdirectories). The application supports text files, Microsoft Word documents and inserted text boxes in PDF files. Users can specify a directory to search and input keywords to find documents containing those keywords.


**Features**

+ Directory Selection ("Ordnerpfad festlegen"): Allows users to select a directory containing documents to be searched. The content of the documents is loaded. Subfolders are also taken into account.
+ Keyword Search ("Stichwortsuche starten"): Users can input potentially multiple keywords separated by a '+' character to search for within the documents.
+ Results Display: Displays the filenames and found keywords in a table view. Hovering over the filename displays the full file path. Clicking the filename opens the file.
+ User Interface: A sleek, dark-themed interface with clear instructions on the buttons.
+ "Beenden": Terminates the application.


**Application**

The program is written in *Python*. An executable version can be downloaded [here](https://github.com/EricSchoebel/DocSpector/releases).

Screenshot of the interface:

![GUI](./Screenshot_GUI.png "GUI")

## License Information

This project is licensed under the GNU General Public License v3.0 (GPLv3). For more details on the license, please see the [LICENSE](./LICENSE) file included in this repository.

### Third-Party Software

This project uses software from third-party libraries, which are subject to their own licenses. For a detailed list of these third-party libraries and their respective licenses, please refer to the [Third-Party-Notices](./THIRD-PARTY-NOTICES.md) document.

