def solution(record):
    answer = []
    commands = []
    user_key = {}
    for i in range(len(record)):
        commandline = record[i].split(' ')
        commands.append(commandline[0] + ' ' + commandline[1])
        if commandline[0] == "Leave":
            continue
        else:
            user_key[commandline[1]] = commandline[2]
            
    for i in range(len(commands)):
        command = commands[i].split(' ')
        if command[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % user_key[command[1]])
        elif command[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % user_key[command[1]])
        else:
            continue
    return answer