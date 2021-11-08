from datetime import datetime

WAREKI_START = {
   '令和': datetime(2019, 5, 1),
   '平成': datetime(1989, 1, 8),
   '昭和': datetime(1926, 12, 25),
   '大正': datetime(1912, 7, 30),
   '明治': datetime(1873, 1, 25)
}

y, m, d = map(int, input().split())


def convert_to_wareki(y, m, d):
    """西暦の年月日を和暦の年に変換する."""
    y_m_d = datetime(y, m, d)
    if WAREKI_START['令和'] <= y_m_d:
        era_str = '令和'
    elif WAREKI_START['平成'] <= y_m_d:
        era_str = '平成'
    elif WAREKI_START['昭和'] <= y_m_d:
        era_str = '昭和'
    elif WAREKI_START['大正'] <= y_m_d:
        era_str = '大正'
    else:
      era_str = '明治'
    print(era_str+"年" +str(m) + "月" +str(d)+"日")


convert_to_wareki(y, m, d)
#print(era_str+"年" +str(m) + "月" +str(d)+"日")
