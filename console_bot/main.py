import re
import handlers

OPERATIONS = {
    'hello': handlers.hello,
    'add': handlers.adding,
    'change': handlers.changing,
    'phone': handlers.get_phones,
    'show all': handlers.show_all,
    'show part': handlers.show_part,
    'remove contact': handlers.remove_contact,
    'remove phone': handlers.remove_phone,
    'close': handlers.good_bye,
    'good bye': handlers.good_bye,
    'exit':handlers.good_bye, 
}

COMMAND_WORDS = '|'.join(OPERATIONS)

def parser(message: str) -> tuple[str|None, str|None, str|None]:
    '''
    Parse message to command, name and number.
    command: one of the COMMAND_WORD at the beginning
    new_number: didgits at the end of the message after space
    old_namber: didgits before new number after space
    name: all symbols between command and number
    '''
    def clean_message(message:str, text_match:re.Match):
        if text_match:
            text = text_match.group(1)
            message = re.sub(text, '', message)
            text = text.strip().lower
        return message, text


    def get_number(message: str) -> tuple[str, str]:
        '''Get number as digits at the end'''
        number = ''
        message = message.rstrip()
        number_match = re.search(fr' (\d+)$', message)
        if number_match:
            number = number_match.group(1)
            message = re.sub(number, '', message)
            number = number.strip()
        return message, number
    
    def get_date(massage: str) -> tuple[message, ]

    command = ''
    message = message.lstrip()
    command_match = re.search(fr'^({COMMAND_WORDS})\b', message, re.IGNORECASE)

    if command_match:
        command = command_match.group(1)
        message = re.sub(command, '', message)
        command = command.lower()

    message, new_number = get_number(message)
    message, old_number = get_number(message)

    name = message.strip()
    return command, name, new_number, old_number 


def main():
    address_book = handlers.address_book
    while True:
        inp = input('Write your command: ')
        command, name, new_number, old_number  = parser(inp)
        try:
            hendler = OPERATIONS[command]
        except KeyError:
            print('There are no command')
            continue
        output = hendler(name, new_number, old_number)
        print(output)
        if output == 'Good bye':
            break
    return address_book

if __name__ == '__main__':
    main()