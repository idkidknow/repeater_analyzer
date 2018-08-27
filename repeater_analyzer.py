# Configure
_permitted_names = {
    'TheGroupName',
} # The set of groups' name that you want to analyze.
_admin_names = set() # The set of the name of the administrators that can use "--clean" to clean the data.
# (However, everyone can change his or her own name to one of the admin names, so this may be useless.)

_sentences = dict() # 'sentence': count
_repeaters = dict() # 'repeater': count

def message_filter(msg):
    """Return True if the message cannot be considered as a repeat."""
    if msg == '[图片]' or '--' in msg or 'List:\n' in msg:
        return True
    return False

def onQQMessage(bot, contact, member, content):
    if contact.name not in _permitted_names:
        return
    counter(member.name, content)
    
    if content == '--list repeaters':
        list_str = 'Repeaters List:'
        for repeater in _repeaters.keys():
            list_str += '\n' + repeater + ': ' + str(_repeaters[repeater]) + ' times.'
        bot.SendTo(contact, list_str)
    if content == '--list sentences':
        list_str = 'Sentences List:'
        for sentence in _sentences.keys():
            if _sentences[sentence] == 0:
                continue
            list_str += '\n「' + sentence + '」: ' + str(_sentences[sentence]) + ' times.'
        bot.SendTo(contact, list_str)
    if content == '--clean':
        if member.name not in _admin_names and not bot.isMe(contact, member):
            bot.SendTo(contact, 'Permission Denied.')
            return
        _sentences.clear()
        _repeaters.clear()
        bot.SendTo(contact, 'Cleaned.')

def counter(name, msg):
    if message_filter(msg):
        return
    if msg in _sentences:
        _sentences[msg] += 1
        if name in _repeaters:
            _repeaters[name] += 1
        else:
            _repeaters[name] = 1
    else:
        _sentences[msg] = 0
