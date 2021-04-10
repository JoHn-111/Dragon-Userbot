from pyrogram import Client, filters
from .utils.utils import modules_help
import subprocess
from threading import Thread
from .utils.utils import requirements_list
import asyncio


def restart(client, message):
    client.restart()
    message.edit('<code>Restart was successful!</code>')
    
    
async def update_restart(client, message):
    client.restart()
    await message.edit('<code>Restart was successful!</code>')
    await asyncio.sleep(3)
    await message.edit('<code>Update process completed!</code>')
    
@Client.on_message(filters.command('restart', ['.']) & filters.me)
async def restart_comand(client, message):
    await message.edit('<code>Restarting...</code>')
    Thread(target=restart, args=(client, message)).start()
    
@Client.on_message(filters.command('update', ["."]) & filters.me)
async def update(client, message):
    await message.edit('<code>Updating...</code>')
    pip_update = subprocess.Popen(["python3", "-m", "pip", "install", "--upgrade", "pip"], stdout=subprocess.PIPE)
    process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    for lib in range(len(requirements_list)):
        process = subprocess.Popen(["pip3", "install", "-U", f"{requirements_list[lib]}"], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    await message.edit('<code>Restarting...</code>')
    Thread(target=update_restart, args=(client, message)).start()
    
    
modules_help.update({'updater': '''<b>Help for |Updater|\nUsage:</b>
<code>.update</code>
<b>[Updating the userbot. If new modules are available, they will be installed]</b>
<code>.restart</code>
<b>[Restart userbot]</b>''', 'updater module': '<b>• Updater</b>:<code> update, restart</code>\n'})
