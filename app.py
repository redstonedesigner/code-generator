import yaml, random, sys
from colorama import init
init()
from colorama import Fore, Back, Style

# Get amount from sys.argv
try:
    amount = int(sys.argv[1])
except:
    print(Back.RED+' ERROR '+Back.RESET+' Please specify an amount of codes to generate.')
    quit()

# Prepare progress bar function
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = Fore.GREEN+'█'+Fore.RESET, printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# Load config
class Config:
    def __init__(self):
        try:
            # Load valid config
            cfg = yaml.load(open('config.yml','r'),Loader=yaml.Loader)
            self.charset = cfg['charset']
            self.format = cfg['format']
        except Exception as e:
            print(str(e))
            # Handle invalid config
            print(Back.RED+' ERROR '+Back.RESET+' Invalid configuration file.  Regenerating...')
            # Generate valid config
            with open('config.yml','w') as file:
                file.write("charset: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'\nformat: '####-####-####-####'")
                file.close()
            print(Back.RED+' ERROR '+Back.RESET+' Config file regenerated.  Please take a moment to customise the configuration before running the program again.')
            quit()
        # Check that amount will not cause infinite loops
        randomise_count = 0
        for i in self.format:
            # If character is to be randomised:
            if i == '#':
                randomise_count += 1
            else:
                continue
        # Compute number of possibilities
        possibilities = len(self.charset)**randomise_count
        if possibilities <= amount:
            print(Back.YELLOW+' WARNING '+Back.RESET+' Generating this number will cause an infinite loop.  Aborting...')
            quit()

config = Config()
codes = []

# Create output file
with open('codes.txt','w') as file:
    # For each code:
    for i in range(0,amount):
        code = ''
        # For each character within the format:
        for k in config.format:
            # If character is to be randomised:
            if k == '#':
                # Generate random character from charset and append it to the code
                code += str(random.choice(config.charset))
            # If character is not to be randomised:
            else:
                # Append character to code
                code += str(k)
        while code in codes:
            code = ''
            for k in config.format:
                if k == '#':
                    code += str(random.choice(config.charset))
                else:
                    code += str(k)
        # Write code to file on a new line
        file.write(code+'\n')
        # Advance progress bar
        printProgressBar(i+1,amount,prefix='Generating...',suffix="("+str(i+1)+"/"+str(amount)+")",length=50)
    # Close file when all codes are generated
    file.close()
    # Print success message
    print(Back.GREEN+' SUCCESS '+Back.RESET+' Codes generated and can be found in codes.txt')
