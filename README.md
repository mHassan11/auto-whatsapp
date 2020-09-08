# whatsapp_automation
Sending automated messages to WhatsApp contacts and groups. 

## Auto-WhatsAPP


- Python tool used for sending automated message to WhatsApp.
   - Predefined list of contacts or groups.
   - sends a crafted Message.
- Can be used with ``cron job`` and ``windows scheduler``.
- This project provides pythonic interface for sending WhatsApp messages.

**NOTE**: [Selenium](https://www.selenium.dev/) can be used to modify the tool for your use-case.


### Installation

`Auto-WhatsApp` is succesfully tested on Python 3.6+.

- To clone the newest code from GitHub, use:
  ```
  git clone "https://github.com/mHassan11/auto-whatsapp.git"
  ```
- Move to the directory by (Linux):
  ```
  cd auto-whatsapp
  ```
- To get the install requirements (Python Packages and Librarues):
  ```
  pip install -r requirements.txt
  ```
  OR
  ```
  pip3 install -r requirements.txt

### Usage
1. Add a list of whatsapp contacts or groups, line by line, on a text file (.txt) extension or modify the existing files ```(groupnames_all.txt/groupnames_small.txt)```. This is case sensitive.
2. Add your crafted message in the `message.txt` file.
3. Open `arguments.txt` and modify the second line according to name of file in step 1 above.
4. Double click `whatsapp_group_tool.exe` or use the following command:
```
python whatsapp_group_tool.py
```
OR
```
python3 whatsapp_group_tool.py
```
**NOTE**: Step 1 and 3 are case sensitve. Be carefull!!

### More

`auto-WhatsAPP` is not intended to be used in such a violent or harmful way. Instead, it developed for `educational` use only.
### Task List
- [x] An sending messages.
   - [x] single user
   - [x] crafted message
   - [x] list of users
   - [x] formatting of messages

- [ ] Adding a pythonic interface for receving messages

If you have any issues or suggestions, [please submit an issue on GitHub](https://github.com/mHassan11/auto-whatsapp/issues) or [email me](mailto:mhassan.3939@gmail.com). 
[**All contributions are appreciated!**](https://github.com/mHassan11/auto-whatsapp)

![](http://gph.is/1sEZ3jm)
