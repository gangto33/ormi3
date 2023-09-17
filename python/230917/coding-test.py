# 코딩테스트 연습 - 연습문제 - 호텔 대실

def solution(book_time):
    book_time.sort()
    rooms = []
    
    for time in book_time:
        out = list(map(lambda x: x.split(':'), time))
        print(out)
        if not rooms:
            rooms.append(int(out[1][0]) * 60 + int(out[1][1]) + 10)
            
        else:
            if all(room > int(out[0][0]) * 60 + int(out[0][1]) for room in rooms):
                rooms.append(int(out[1][0]) * 60 + int(out[1][1]) + 10)
            else:
                for room in rooms:
                    if room <= int(out[0][0]) * 60 + int(out[0][1]):
                        rooms.remove(room)
                        rooms.append(int(out[1][0]) * 60 + int(out[1][1]) + 10)
                        break
                        
    return len(rooms)