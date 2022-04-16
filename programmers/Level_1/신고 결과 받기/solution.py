from collections import defaultdict

def get_reporter_and_person(people):
    reporter, person = people.split(" ")
    return reporter, person

def get_report_dict(report):
    dic = defaultdict(set)
    for people in report:
        reporter, person = get_reporter_and_person(people)
        dic[reporter].add(person)
    return dic

def get_reported_count(id_list, report_dict):
    dic = defaultdict(int)
    for person_id in id_list:
        for person in report_dict[person_id]:
            dic[person] += 1
    return dic

def get_suspended_list(reported_count, k):
    answer = []
    for person in reported_count:
        if reported_count[person] >= k:
            answer.append(person)
    return answer

def get_result_mail_count(suspended_list, id_list, report_dic):
    answer= []
    for person in id_list:
        count = 0
        for p in report_dic[person]:
            if p in suspended_list:
                count += 1
        answer.append(count)
    return answer

def solution(id_list, report, k):
    answer = []
    report_dic = get_report_dict(report)
    reported_count = get_reported_count(id_list, report_dic)
    suspended_list = get_suspended_list(reported_count, k)
    answer = get_result_mail_count(suspended_list, id_list, report_dic)
    return answer