try:
    a = [10, 20, 30]
    print(a[3])
except Exception as e:
    print(f"에러 메시지: {e}")

try:
    n = int('20%')
except Exception as e:
    print(f"에러 메시지: {e}")

try:
    a = 100 + '200'
except Exception as e:
    print(f"에러 메시지: {e}")
