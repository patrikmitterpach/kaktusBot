from glob import glob

def fileToModule(file):
    path = file.split('/')
    return path[-2], path[-1] # returns the last file in a listing

def discordModulePath(folder, module):
    return f'lib.extensions.{ folder }.{ module[:-3] }'

def findExtensions(dir):
    extensionList = []
    
    files = glob('./lib/extensions/*/*.py')
    for file in files:
        folder, module = fileToModule(file)                 # *.py           
        discordPath = discordModulePath(folder, module)     # lib.extensions.*.*

        extensionList.append( discordPath )
    return extensionList