# Configure
_permitted_names = {
    'TheGroupName',
} # The set of groups' name that you want to analyze.
_admin_names = set() # The set of the name of the administrators that can use "--clean" to clean the data.
# (However, everyone can change his or her own name to one of the admin names, so this may be useless.)

class Group(object):
    def __init__(self):
        self.sentences = dict() # 'sentence': count
        self.repeaters = dict() # 'repeater': count

_groups = dict() # The dict of Group

def message_filter(msg):
    """Return True if the message cannot be considered as a repeat."""
    if msg == '' or '--' in msg or 'List:\n' in msg:
        return True
    return False

def onQQMessage(bot, contact, member, content):
    if contact.name not in _permitted_names:
        return
    if contact.name not in _groups:
        _groups[contact.name] = Group()
    counter(contact.name, member.name, content)
    
    group = _groups[contact.name]
    if content == '--list repeaters':
        list_str = 'Repeaters List:'
        for repeater in group.repeaters.keys():
            list_str += '\n' + repeater + ': ' + str(group.repeaters[repeater]) + ' times.'
        bot.SendTo(contact, list_str)
    if content == '--list sentences':
        list_str = 'Sentences List:'
        for sentence in group.sentences.keys():
            if group.sentences[sentence] == 0:
                continue
            list_str += '\n「' + sentence + '」: ' + str(group.sentences[sentence]) + ' times.'
        bot.SendTo(contact, list_str)
    if content == '--clean':
        if member.name not in _admin_names and not bot.isMe(contact, member):
            bot.SendTo(contact, 'Permission Denied.')
            return
        group.sentences.clear()
        group.repeaters.clear()
        bot.SendTo(contact, 'Cleaned.')

def counter(group, name, msg):
    if message_filter(msg):
        return
    group = _groups[group]
    if msg in group.sentences:
        group.sentences[msg] += 1
        if name in group.repeaters:
            group.repeaters[name] += 1
        else:
            group.repeaters[name] = 1
    else:
        group.sentences[msg] = 0
