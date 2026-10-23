def solution(n, info):
    answer = [-1]
    max_diff = 0
    ryan = [0] * 11

    def backtracking(depth, arrows):
        nonlocal answer, max_diff

        if depth == 10:
            ryan[10] = arrows  # 남은 화살은 모두 0점에 배치

            # 점수 계산
            apeach_score, ryan_score = 0, 0

            for i in range(11):
                score = 10 - i

                if info[i] == 0 and ryan[i] == 0:
                    continue
                elif info[i] < ryan[i]:
                    ryan_score += score
                else:
                    apeach_score += score

            diff = ryan_score - apeach_score

            if diff > max_diff:
                max_diff = diff
                answer = ryan.copy()

            # 점수 차이가 같으면 낮은 점수에 화살을 더 많이 쏜 경우 선택
            elif diff > 0 and diff == max_diff:
                for i in range(10, -1, -1):
                    if ryan[i] > answer[i]:
                        answer = ryan.copy()
                        break
                    elif ryan[i] < answer[i]:
                        break

            ryan[10] = 0 # 상위 단계로 되돌아가기 위해 초기화
            return

        # 1. 현재 점수에 화살을 쏘지 않는 경우
        ryan[depth] = 0
        backtracking(depth + 1, arrows)

        # 2. 어피치보다 1발 더 쏘는 경우
        needed = info[depth] + 1
        if arrows >= needed:
            ryan[depth] = needed
            backtracking(depth + 1, arrows - needed)
            ryan[depth] = 0  # 원상 복구

    backtracking(0, n)

    return answer