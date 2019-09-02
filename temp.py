def solution(record):
    answer = []
    commands = []
    user_key = {} 
    
    # user_id와 nick 매핑
    for i in range(len(record)):
        commandline = record[i].split(' ')
        commands.append(commandline[0] + ' ' + commandline[1])
        if commandline[0] == "Leave":
            continue
        else:
            user_key[commandline[1]] = commandline[2]
    
    # 메시지 출력        
    for i in range(len(commands)):
        command = commands[i].split(' ')
        if command[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % user_key[command[1]])
        elif command[0] == 'Leave':
            answer.append('%s님이 나가셨습니다.' % user_key[command[1]])
        else:
            continue
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))