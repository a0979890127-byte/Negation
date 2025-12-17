#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Negation.main import askLoki


def main():
    testLIST = [
        "他來以前我就走了",
        "他沒來以前我就走了",
        "醫生來以前，張三就死了",
        "醫生還沒來以前，張三就死了"
    ]

    refDICT = {}  # 你目前沒有用到參考資料，可留空

    for inputSTR in testLIST:
        resultDICT = askLoki(inputSTR, refDICT=refDICT)
        print(f"\nINPUT: {inputSTR}")
        print(resultDICT)

    return None


if __name__ == "__main__":
    main()
