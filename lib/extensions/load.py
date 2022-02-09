from glob import glob

def fileToModule(file):
    return file.split('/')[-1] # returns the last file in a listing

def discordModulePath(module):
    return f'lib.extensions.{ module[:-3] }.{ module[:-3] }'

def findExtensions(dir):
    extensionList = []
    
    files = glob('./lib/extensions/*/*.py')
    for file in files:
        module = fileToModule(file)                 # *.py           
        discordPath = discordModulePath(module)     # lib.extensions.*.*

        extensionList.append( discordPath )
    return extensionList