from collections import deque
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        queue = deque(skill)
        imp = False
        
        while queue:
            # 선행 스킬을 하나씩 뽑는다.
            pre_sk = queue.popleft()
            skill_tree = list(skill_tree)
            # 배우고자 하는 스킬트리에서 스킬 하나하나 뽑는다.
            for s in skill_tree[:]:
                # 만약 선행 순서에 맞게 스킬이 나왔다면
                if s == pre_sk:
                    # 배우고자 하는 스킬에서 해당 스킬 제외 후 다음 스킬 비교
                    skill_tree.remove(s)
                    break
                # s가 queue에 있다는 것은 선행스킬을 아직 배우지 않은 상태
                elif s in queue:
                    # impposble 처리를 위해 imp를 True로 갱신
                    imp = True
                    break
            # imp 가 True라면 배울 수 없는 스킬트리
            if imp:
                break
            
        if not imp:
            answer += 1
                    
            
    return answer