from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    # 왼쪽 인덱스를 0으로 초기화합니다.
    leftIdx = 0
    # 오른쪽 인덱스를 배열의 마지막 인덱스로 초기화합니다.
    rightIdx = len(nums) - 1
    
    # 왼쪽 인덱스가 오른쪽 인덱스보다 작거나 같은 동안 반복합니다.
    while leftIdx <= rightIdx:
        # 중간 인덱스를 계산합니다.
        centerIdx = (rightIdx + leftIdx) // 2
        # 중간 인덱스의 값을 가져옵니다.
        centerVal = nums[centerIdx]
        
        # 중간 값이 목표값과 같으면 중간 인덱스를 반환합니다.
        if target == centerVal:
            return centerIdx
        
        # 중간 값이 목표값보다 작으면 왼쪽 인덱스를 중간 인덱스의 다음으로 설정합니다.
        if centerVal < target:
            leftIdx = centerIdx + 1
        # 중간 값이 목표값보다 크면 오른쪽 인덱스를 중간 인덱스의 이전으로 설정합니다.
        else:
            rightIdx = centerIdx - 1
    
    # 목표값을 찾지 못한 경우 -1을 반환합니다.
    return -1

# 함수 테스트
print(binarySearch(nums=[-1, 1, 3, 5, 9, 18], target=9))  # 4를 출력합니다.