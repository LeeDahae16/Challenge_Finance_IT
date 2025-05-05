import sys
import math

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7

    M = int(input())
    answer = 0

    for _ in range(M):
        N, S = map(int, input().split())
        # 최대공약수로 기약분수 만들기
        g = math.gcd(N, S)
        num = S // g    # 분자
        den = N // g    # 분모
        
        # 100000005 제곱을 해야하니까 100000005가 2의 거듭제곱으로 어떻게 표현되는지 확인!
        bits = []
        exp = MOD - 2
        for i in range(63, -1, -1):
            if (exp >> i) & 1:
                bits.append(i)
        
        # 거듭제곱으로 좀 더 빠르게 100000005 제곱 계산하기...!
        target = 1
        for b in bits:
            now = den
            cnt = b
            while cnt > 0:
                now = (now * now) % MOD
                cnt -= 1
            target = (target * now) % MOD
        
        # 놀랍게도 mod 계산이 내 위 뻘짓을 안해도 되게 해준다고 합니다...
        
        # 분자 곱하고 누적
        target = (target * num) % MOD
        answer = (answer + target) % MOD

    print(answer)

if __name__ == "__main__":
    main()
