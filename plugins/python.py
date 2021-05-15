from pyrogram import Client, filters
from pyrogram.types import Message
from .utils.utils import modules_help

from io import StringIO
import sys


@Client.on_message(filters.command(['ex', 'py'], ['.']) & filters.me)
def user_exec(client: Client, message: Message):
    code = ''
    try:
        code = message.text.split(".ex ")[1]
    except IndexError:
        try:
           code = message.text.split(".ex\n")[1]
        except IndexError:
            pass

    result = sys.stdout = StringIO()
    try:
        exec(code)
        
        message.edit(f'''<b>Code:</b>
<code>{code}</code>
<b>Result</b>:
<code>{result.getvalue()}</code>
''')
    except:
        message.edit(f'''<b>Code:</b>
<code>{code}</code>
<b>Result</b>:
<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>
''')


modules_help.update({'python': '''<b>Help for |python|\nUsage:</b>
<code>.ex [python code]</code>
<b>[Python code execution]</b>''', 'python module': '<b>• Python</b>:<code> ex</code>\n'})
