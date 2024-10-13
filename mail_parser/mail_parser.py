#######################
# @author: RaffaDNDM
# @date:   2022-03-02
#######################

import email
from termcolor import cprint
import argparse

LINE = "_________________________________________________________"


def mail_analyzer(mail_file):
    return email.message_from_file(mail_file)
    

def arg_parser():
    '''
    Parser of command line arguments
    '''
    #Parser of command line arguments
    parser = argparse.ArgumentParser()
    #Initialization of needed arguments
    parser.add_argument("-mail", "-file", "-f", dest="file", help="Filepath of the e-mail (.eml) to be analysed.")
    #Parse command line arguments
    args = parser.parse_args()
    
    #Check if the arguments have been specified on command line
    if not args.file:
        parser.print_help()
        exit(1)
    
    mail_file=args.file
    print("\n")
    cprint('Mail file:   ', 'yellow', attrs=['bold',], end='')
    print(f'{mail_file}', end='\n\n')

    return mail_file


def menu(msg):
    # To get to headers, you treat the Message() as a dict:    
    cprint('\nSelect the header you want to visualize'+LINE, 'blue')
    keys=msg.keys()
    for i in range(len(keys)):
        cprint(f"{i+1}. {keys[i]}", 'cyan')
    
    cprint('CTRL+C to stop the program...', 'green')
    cprint(LINE, 'blue')  

    try:
        choice = int(input())
        
        if choice<1 or choice>(len(keys)+1):
            raise ValueError
        else:
            cprint(f'{keys[choice-1]}:', 'yellow')
            print(msg[keys[choice-1]])

    except ValueError:
        print(f"Insert a number in range 1-{len(keys)+1}", 'red')


def main():
    mail_file = arg_parser()

    with open(mail_file, 'r') as fd:
        msg = mail_analyzer(fd)

        try:
            while True:
                menu(msg)
        except KeyboardInterrupt:
            exit(0)


if __name__=="__main__":
    main()