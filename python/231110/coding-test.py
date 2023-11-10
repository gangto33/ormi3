# 코딩테스트 연습 - Summer/Winter Coding(~2018) - 스킬트리

def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for skill_tree in skill_trees:
        for i in reversed(range(1, len(skill))):
            if skill_tree.find(skill[i]) != -1:
                if skill_tree.find(skill[i]) < skill_tree.find(skill[i-1]) or skill_tree.find(skill[i-1]) == -1:
                    answer -= 1
                    break
                else:
                    break
        
    return answer
