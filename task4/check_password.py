#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""비밀번호 강도 검증 프로그램"""

import re
import os


def check_password_strength(password):
    """비밀번호 강도 점수 계산"""
    score = 0
    feedback = []

    # 길이 체크 (최대 40점)
    length = len(password)
    if length >= 10:
        score += 20
    else:
        feedback.append(f"최소 10자 이상 필요 (현재: {length}자)")

    if length >= 12:
        score += 10
    if length >= 16:
        score += 10

    # 대문자 체크 (15점)
    if re.search(r'[A-Z]', password):
        score += 15
    else:
        feedback.append("영문 대문자 포함 권장")

    # 소문자 체크 (15점)
    if re.search(r'[a-z]', password):
        score += 15
    else:
        feedback.append("영문 소문자 포함 권장")

    # 숫자 체크 (15점)
    if re.search(r'[0-9]', password):
        score += 15
    else:
        feedback.append("숫자 포함 필요")

    # 특수문자 체크 (15점)
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 15
    else:
        feedback.append("특수문자 포함 필요")

    # 한글 체크 (보너스 10점)
    if re.search(r'[가-힣]', password):
        score += 10

    # 연속 문자 체크 (감점)
    if re.search(r'(abc|bcd|cde|123|234|345|456)', password.lower()):
        score -= 10
        feedback.append("연속된 문자 사용 지양")

    # 반복 문자 체크 (감점)
    if re.search(r'(.)\1{2,}', password):
        score -= 10
        feedback.append("반복 문자 사용 지양")

    # 점수 범위 조정
    score = max(0, min(100, score))

    # 등급 결정
    if score >= 81:
        grade = "매우 강함"
        color = "blue"
    elif score >= 61:
        grade = "강함"
        color = "green"
    elif score >= 41:
        grade = "보통"
        color = "yellow"
    elif score >= 21:
        grade = "약함"
        color = "orange"
    else:
        grade = "매우 약함"
        color = "red"

    return {
        'password': password,
        'score': score,
        'grade': grade,
        'color': color,
        'feedback': feedback if feedback else ["개선 필요 없음"]
    }


def main():
    """메인 함수"""
    input_file = 'passwords_to_check.txt'

    if not os.path.exists(input_file):
        print(f"오류: {input_file} 파일이 없습니다")
        return

    results = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # 주석이나 빈 줄 건너뛰기
            if not line or line.startswith('#'):
                continue

            result = check_password_strength(line)
            results.append(result)
            print(f"비밀번호: {line} → 점수: {result['score']}, 등급: {result['grade']}")

    print(f"\n총 {len(results)}개 비밀번호 검증 완료")


if __name__ == '__main__':
    main()
