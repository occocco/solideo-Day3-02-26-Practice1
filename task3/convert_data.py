#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV ↔ JSON 양방향 데이터 포맷 변환기
정부 부서 데이터를 CSV와 JSON 형식 간 변환하고 무결성을 검증합니다.
"""

import csv
import json
import sys
import os
from typing import List, Dict, Any, Tuple


class DataConverter:
    """데이터 포맷 변환 클래스"""

    def __init__(self):
        """변환 통계 초기화"""
        self.stats = {
            'csv_to_json_success': 0,
            'json_to_csv_success': 0,
            'errors': 0,
            'warnings': 0
        }
        self.error_log = []

    def detect_encoding(self, filepath: str) -> str:
        """
        파일 인코딩 자동 감지

        Args:
            filepath (str): 파일 경로

        Returns:
            str: 감지된 인코딩 (utf-8, cp949, euc-kr 중 하나)
        """
        encodings = ['utf-8', 'cp949', 'euc-kr']

        for encoding in encodings:
            try:
                with open(filepath, 'r', encoding=encoding) as f:
                    f.read()
                    return encoding
            except (UnicodeDecodeError, FileNotFoundError):
                continue

        return 'utf-8'  # 기본값

    def csv_to_json(self, csv_file: str, json_file: str) -> bool:
        """
        CSV 파일을 JSON 형식으로 변환

        Args:
            csv_file (str): 입력 CSV 파일 경로
            json_file (str): 출력 JSON 파일 경로

        Returns:
            bool: 변환 성공 여부
        """
        # 파일 존재 확인
        if not os.path.exists(csv_file):
            self.error_log.append(f"오류: {csv_file} 파일이 없습니다")
            self.stats['errors'] += 1
            return False

        try:
            # 인코딩 감지
            encoding = self.detect_encoding(csv_file)
            print(f"CSV 파일 인코딩: {encoding}")

            # CSV 읽기
            data = []
            with open(csv_file, 'r', encoding=encoding) as f:
                csv_reader = csv.DictReader(f)

                # 헤더 확인
                if csv_reader.fieldnames is None:
                    self.error_log.append("오류: CSV 헤더가 없습니다")
                    self.stats['errors'] += 1
                    return False

                for row_num, row in enumerate(csv_reader, start=2):
                    # 컬럼 수 확인
                    if len(row) != len(csv_reader.fieldnames):
                        warning = f"경고: {row_num}행의 컬럼 수가 일치하지 않습니다"
                        self.error_log.append(warning)
                        self.stats['warnings'] += 1

                    # 데이터 타입 변환 (숫자로 변환 가능한 것은 변환)
                    converted_row = {}
                    for key, value in row.items():
                        converted_row[key] = self._convert_value(value)

                    data.append(converted_row)

            # 빈 데이터 확인
            if not data:
                self.error_log.append("경고: 변환할 데이터가 없습니다")
                self.stats['warnings'] += 1
                return False

            # JSON 저장
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            self.stats['csv_to_json_success'] = len(data)
            print(f"CSV → JSON 변환 완료: {len(data)}개 레코드")
            return True

        except Exception as e:
            self.error_log.append(f"오류: CSV → JSON 변환 실패 - {str(e)}")
            self.stats['errors'] += 1
            return False

    def json_to_csv(self, json_file: str, csv_file: str) -> bool:
        """
        JSON 파일을 CSV 형식으로 변환

        Args:
            json_file (str): 입력 JSON 파일 경로
            csv_file (str): 출력 CSV 파일 경로

        Returns:
            bool: 변환 성공 여부
        """
        # 파일 존재 확인
        if not os.path.exists(json_file):
            self.error_log.append(f"오류: {json_file} 파일이 없습니다")
            self.stats['errors'] += 1
            return False

        try:
            # JSON 읽기
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # JSON 유효성 확인
            if not isinstance(data, list):
                self.error_log.append("오류: JSON은 배열 형식이어야 합니다")
                self.stats['errors'] += 1
                return False

            if not data:
                self.error_log.append("경고: 변환할 데이터가 없습니다")
                self.stats['warnings'] += 1
                return False

            # 헤더 추출 (첫 번째 객체의 키)
            fieldnames = list(data[0].keys())

            # CSV 저장
            with open(csv_file, 'w', encoding='utf-8', newline='') as f:
                csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(data)

            self.stats['json_to_csv_success'] = len(data)
            print(f"JSON → CSV 변환 완료: {len(data)}개 레코드")
            return True

        except json.JSONDecodeError as e:
            self.error_log.append(f"오류: 유효하지 않은 JSON 형식입니다 - {str(e)}")
            self.stats['errors'] += 1
            return False
        except Exception as e:
            self.error_log.append(f"오류: JSON → CSV 변환 실패 - {str(e)}")
            self.stats['errors'] += 1
            return False

    def _convert_value(self, value: str) -> Any:
        """
        문자열 값을 적절한 데이터 타입으로 변환

        Args:
            value (str): 변환할 값

        Returns:
            Any: 변환된 값 (int, float, 또는 str)
        """
        if not value or not isinstance(value, str):
            return value

        # 정수 변환 시도
        try:
            if '.' not in value and value.lstrip('-').isdigit():
                return int(value)
        except (ValueError, AttributeError):
            pass

        # 실수 변환 시도
        try:
            return float(value)
        except (ValueError, AttributeError):
            pass

        # 변환 실패 시 원본 문자열 반환
        return value

    def verify_integrity(self, original_file: str, converted_file: str) -> Tuple[bool, str]:
        """
        변환 전후 데이터 무결성 검증

        Args:
            original_file (str): 원본 파일 경로
            converted_file (str): 변환된 파일 경로

        Returns:
            Tuple[bool, str]: (검증 성공 여부, 결과 메시지)
        """
        try:
            # 원본 CSV 읽기
            encoding = self.detect_encoding(original_file)
            with open(original_file, 'r', encoding=encoding) as f:
                original_data = list(csv.DictReader(f))

            # 변환된 CSV 읽기
            with open(converted_file, 'r', encoding='utf-8') as f:
                converted_data = list(csv.DictReader(f))

            # 레코드 수 비교
            if len(original_data) != len(converted_data):
                return False, f"레코드 수 불일치: 원본 {len(original_data)}, 변환 {len(converted_data)}"

            # 각 행 비교
            for i, (orig, conv) in enumerate(zip(original_data, converted_data)):
                for key in orig.keys():
                    orig_val = self._convert_value(orig[key])
                    conv_val = self._convert_value(conv[key])

                    if orig_val != conv_val:
                        return False, f"{i+2}행, {key} 컬럼 불일치: {orig_val} != {conv_val}"

            return True, "데이터 무결성 검증 완료"

        except Exception as e:
            return False, f"검증 오류: {str(e)}"

    def print_stats(self):
        """변환 통계 출력"""
        print("\n" + "=" * 60)
        print("데이터 변환 통계")
        print("=" * 60)
        print(f"CSV → JSON 변환: {self.stats['csv_to_json_success']}개 레코드")
        print(f"JSON → CSV 변환: {self.stats['json_to_csv_success']}개 레코드")
        print(f"오류: {self.stats['errors']}개")
        print(f"경고: {self.stats['warnings']}개")

        if self.error_log:
            print("\n오류/경고 로그:")
            for log in self.error_log:
                print(f"  - {log}")

        print("=" * 60)


def main():
    """메인 함수"""
    converter = DataConverter()

    # 파일 경로
    original_csv = 'government_data.csv'
    json_file = 'government_data.json'
    converted_csv = 'government_data_converted.csv'

    print("데이터 포맷 변환 시작...\n")

    # 1. CSV → JSON 변환
    print("[1단계] CSV → JSON 변환")
    csv_to_json_success = converter.csv_to_json(original_csv, json_file)

    if csv_to_json_success:
        # 2. JSON → CSV 변환 (검증용)
        print("\n[2단계] JSON → CSV 변환 (검증)")
        json_to_csv_success = converter.json_to_csv(json_file, converted_csv)

        if json_to_csv_success:
            # 3. 데이터 무결성 검증
            print("\n[3단계] 데이터 무결성 검증")
            is_valid, message = converter.verify_integrity(original_csv, converted_csv)

            if is_valid:
                print(f"✓ {message}")
            else:
                print(f"✗ {message}")
                converter.stats['errors'] += 1

    # 통계 출력
    converter.print_stats()

    # 종료 코드 반환
    return 0 if converter.stats['errors'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
