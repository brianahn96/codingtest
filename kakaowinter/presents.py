# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    answer = 0
    friendict = dict()
    giftindex = dict()
    nextmonth = dict()
    for friend in friends:
        friendict[friend] = {key: 0 for key in friends}
        giftindex[friend] = 0
        nextmonth[friend] = 0
    
    for gift in gifts:
        giver, receiver = gift.split()
        friendict[giver][receiver] += 1
        giftindex[giver] += 1
        giftindex[receiver] -= 1
        
    
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            if friendict[friends[i]][friends[j]] > friendict[friends[j]][friends[i]]:
                nextmonth[friends[i]] += 1
            elif friendict[friends[i]][friends[j]] < friendict[friends[j]][friends[i]]:
                nextmonth[friends[j]] += 1
            else:
                if giftindex[friends[i]] > giftindex[friends[j]]:
                    nextmonth[friends[i]] += 1
                elif giftindex[friends[i]] < giftindex[friends[j]]:
                    nextmonth[friends[j]] += 1
                else:
                    pass
    
    for friend, present in nextmonth.items():
        answer = max(answer, present)
    
    return answer