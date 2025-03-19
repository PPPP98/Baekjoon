def beadsort(input_list):

    """Bead sort."""

    return_list = []

    # 입력의 최대값만큼 많은 요소를 포함하는 '전치된 목록'을 초기화한다.

    # 효과적으로, 입력 구슬의 '가장 높은' 열을 가져와 평평하게 배치한다.

    transposed_list = [0] * max(input_list)

    for num in input_list:

    # 입력 목록의 각 요소(각 '구슬 열')에 대해

    # 열이 높이만큼 전치된 목록의 많은 요소를 증가시켜 '구슬을 평평하게 눕힙니다'.

    # 이들은 이전 추가 위에 누적된다.

        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]

    # 이제 구슬을 떨어뜨렸다. 전치 해제하려면

    # 떨어진 구슬의 '가장 아래 행'을 계산한 다음

    # 전치된 목록의 각 '열'에서 1을 빼서 이 행을 제거하는 것을 흉내낸다.

    # 열이 현재 행만큼 충분히 높이 도달하지 못하면

    # transposed_list의 값은 <= 0이 된다.

    for i in range(len(input_list)):

    # 값 > i를 세는 것은 현재 '가장 아래 행'에

    # 얼마나 많은 구슬이 있는지 알려주는 방법이다.

    # 파이썬의 부울은 정수로 평가될 수 있다. True == 1 및 False == 0.

        return_list.append(sum(n > i for n in transposed_list))

    # 결과 목록은 내림차순으로 정렬된다.

    return return_list