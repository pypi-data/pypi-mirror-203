from datetime import datetime, timedelta

# 获取环比
def day_on_day(number, lastNumber):
    """
    获得环比
    :param number: 比较数据 int 
    :param lastNumber: 被比较数据 int
    :return:环比
    """
    result = ('{:.2%}'.format(
        (number - lastNumber) / lastNumber if lastNumber else 1)
    ) if number - lastNumber != 0 else '0%'
    return result

# 获取前多少天时间
def get_before_date(days):
    """
    获取当前时间n天前日期 
    :param days: 前n天
    :return:
    """
    day_now = datetime.now()
    date = (day_now - timedelta(days=int(days))).strftime("%Y-%m-%d %H:%M:%S")
    return date
