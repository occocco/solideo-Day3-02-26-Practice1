#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
개인정보 자동 탐지 및 마스킹 프로그램
주민등록번호, 전화번호, 이메일, 주소, 신용카드번호를 자동으로 탐지하고 마스킹 처리합니다.
"""

import re
import sys
import os
from typing import Tuple, Dict


class PersonalInfoMasker:
    """개인정보 마스킹 클래스"""

    def __init__(self):
        """마스킹 통계 초기화"""
        self.stats = {
            'resident_number': 0,
            'phone_number': 0,
            'email': 0,
            'address': 0,
            'credit_card': 0
        }

    def mask_resident_number(self, text: str) -> str:
        """
        주민등록번호 마스킹
        패턴: YYMMDD-NNNNNNN 또는 YYMMDDNNNNNNN
        마스킹: YYMMDD-N*******
        """
        # 하이픈 있는 경우: 123456-1234567
        pattern1 = r'\b(\d{6})-(\d{7})\b'

        def replace1(match):
            self.stats['resident_number'] += 1
            return f"{match.group(1)}-{match.group(2)[0]}{'*' * 6}"

        text = re.sub(pattern1, replace1, text)

        # 하이픈 없는 경우: 1234561234567 (13자리 연속 숫자, 앞뒤에 숫자 없음)
        pattern2 = r'(?<!\d)(\d{6})(\d{7})(?!\d)'

        def replace2(match):
            self.stats['resident_number'] += 1
            return f"{match.group(1)}{match.group(2)[0]}{'*' * 6}"

        text = re.sub(pattern2, replace2, text)

        return text

    def mask_phone_number(self, text: str) -> str:
        """
        전화번호 마스킹
        패턴: 010-1234-5678, 01012345678, 02-123-4567, 031-1234-5678 등
        마스킹: 010-****-5678, 010****5678
        """
        # 휴대폰 번호 (010, 011, 016, 017, 018, 019)
        # 하이픈 있는 경우: 010-1234-5678
        pattern1 = r'\b(01[0-9])-(\d{3,4})-(\d{4})\b'

        def replace1(match):
            self.stats['phone_number'] += 1
            return f"{match.group(1)}-{'*' * len(match.group(2))}-{match.group(3)}"

        text = re.sub(pattern1, replace1, text)

        # 하이픈 없는 경우: 01012345678
        pattern2 = r'\b(01[0-9])(\d{3,4})(\d{4})\b'

        def replace2(match):
            self.stats['phone_number'] += 1
            return f"{match.group(1)}{'*' * len(match.group(2))}{match.group(3)}"

        text = re.sub(pattern2, replace2, text)

        # 일반 전화번호 (지역번호 포함)
        # 02-123-4567, 031-1234-5678, 070-1234-5678 등
        pattern3 = r'\b(0\d{1,2})-(\d{3,4})-(\d{4})\b'

        def replace3(match):
            self.stats['phone_number'] += 1
            return f"{match.group(1)}-{'*' * len(match.group(2))}-{match.group(3)}"

        text = re.sub(pattern3, replace3, text)

        return text

    def mask_email(self, text: str) -> str:
        """
        이메일 마스킹
        패턴: username@domain.com
        마스킹: @ 앞 부분 50% 마스킹 (chu****@gov.kr)
        """
        pattern = r'\b([a-zA-Z0-9._-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b'

        def replace(match):
            self.stats['email'] += 1
            username = match.group(1)
            domain = match.group(2)

            # username의 50%를 마스킹
            visible_length = len(username) // 2
            if visible_length < 1:
                visible_length = 1

            masked_username = username[:visible_length] + '*' * (len(username) - visible_length)
            return f"{masked_username}@{domain}"

        return re.sub(pattern, replace, text)

    def mask_credit_card(self, text: str) -> str:
        """
        신용카드번호 마스킹
        패턴: 1234-5678-9012-3456 또는 1234567890123456 (16자리)
        마스킹: 1234-****-****-3456
        """
        # 하이픈 있는 경우: 1234-5678-9012-3456
        pattern1 = r'\b(\d{4})-(\d{4})-(\d{4})-(\d{4})\b'

        def replace1(match):
            self.stats['credit_card'] += 1
            return f"{match.group(1)}-****-****-{match.group(4)}"

        text = re.sub(pattern1, replace1, text)

        # 하이픈 없는 경우: 1234567890123456 (16자리 연속 숫자)
        pattern2 = r'(?<!\d)(\d{4})(\d{4})(\d{4})(\d{4})(?!\d)'

        def replace2(match):
            self.stats['credit_card'] += 1
            return f"{match.group(1)}********{match.group(4)}"

        text = re.sub(pattern2, replace2, text)

        return text

    def mask_address(self, text: str) -> str:
        """
        주소 마스킹
        패턴: 시/도 + 구/군 + 상세주소
        마스킹: 시/도 + 구/군까지만 표시, 나머지는 ****
        예: 서울시 종로구 세종대로 209 -> 서울시 종로구 ****
        """
        # 한국 주소 패턴 (시/도 + 구/군 + 상세주소)
        # 서울특별시, 경기도, 부산광역시 등
        pattern = r'(서울특별시|서울시|서울|부산광역시|부산시|부산|대구광역시|대구시|대구|인천광역시|인천시|인천|광주광역시|광주시|광주|대전광역시|대전시|대전|울산광역시|울산시|울산|세종특별자치시|세종시|세종|경기도|강원도|충청북도|충북|충청남도|충남|전라북도|전북|전라남도|전남|경상북도|경북|경상남도|경남|제주특별자치도|제주도|제주)\s+([가-힣]+(?:구|군))\s+([가-힣0-9\s]+(?:로|길|대로|번길|가|동|리)[0-9\s-]*[가-힣0-9]*)'

        def replace(match):
            self.stats['address'] += 1
            return f"{match.group(1)} {match.group(2)} ****"

        text = re.sub(pattern, replace, text)

        # 간단한 주소 패턴 (구/군 + 동 + 번지)
        pattern2 = r'([가-힣]+(?:구|군))\s+([가-힣]+동)\s+([0-9-]+(?:번지|번)?)'

        def replace2(match):
            self.stats['address'] += 1
            return f"{match.group(1)} {match.group(2)} ****"

        text = re.sub(pattern2, replace2, text)

        return text

    def mask_all(self, text: str) -> str:
        """모든 개인정보 마스킹 적용"""
        # 순서가 중요: 더 구체적인 패턴을 먼저 적용
        text = self.mask_resident_number(text)
        text = self.mask_credit_card(text)
        text = self.mask_phone_number(text)
        text = self.mask_email(text)
        text = self.mask_address(text)

        return text

    def get_stats(self) -> Dict[str, int]:
        """마스킹 통계 반환"""
        return self.stats

    def print_stats(self):
        """마스킹 통계 출력"""
        print("\n" + "=" * 50)
        print("개인정보 탐지 통계")
        print("=" * 50)
        print(f"주민등록번호: {self.stats['resident_number']}개")
        print(f"전화번호: {self.stats['phone_number']}개")
        print(f"이메일: {self.stats['email']}개")
        print(f"주소: {self.stats['address']}개")
        print(f"신용카드번호: {self.stats['credit_card']}개")
        print("=" * 50)

        total = sum(self.stats.values())
        if total == 0:
            print("탐지된 개인정보가 없습니다.")
        else:
            print(f"총 {total}개의 개인정보가 탐지되었습니다.")


def read_file_with_encoding(filepath: str) -> Tuple[str, str]:
    """
    파일을 다양한 인코딩으로 읽기 시도
    반환: (파일 내용, 사용된 인코딩)
    """
    encodings = ['utf-8', 'cp949', 'euc-kr', 'latin-1']

    for encoding in encodings:
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                content = f.read()
                return content, encoding
        except UnicodeDecodeError:
            continue
        except Exception as e:
            raise Exception(f"파일 읽기 오류: {str(e)}")

    raise Exception("지원하는 인코딩으로 파일을 읽을 수 없습니다.")


def main():
    """메인 함수"""
    # 기본 파일 경로
    input_file = 'personal_info_sample.txt'
    output_file = 'masked_result.txt'

    # 명령줄 인자로 파일 경로 지정 가능
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    # 파일 존재 여부 확인
    if not os.path.exists(input_file):
        print(f"오류: 파일을 찾을 수 없습니다 - {input_file}")
        sys.exit(1)

    try:
        # 파일 읽기
        content, encoding = read_file_with_encoding(input_file)
        print(f"파일을 {encoding} 인코딩으로 읽었습니다.")

        # 빈 파일 체크
        if not content.strip():
            print("경고: 빈 파일입니다.")
            return

        # 마스킹 처리
        masker = PersonalInfoMasker()
        masked_content = masker.mask_all(content)

        # 결과 파일 저장
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(masked_content)
            print(f"\n마스킹 결과가 {output_file}에 저장되었습니다.")
        except PermissionError:
            print("오류: 파일 저장 권한이 없습니다.")
            sys.exit(1)
        except Exception as e:
            print(f"오류: 파일 저장 실패 - {str(e)}")
            sys.exit(1)

        # 통계 출력
        masker.print_stats()

    except Exception as e:
        print(f"오류: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
