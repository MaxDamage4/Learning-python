def main():
    N = 1
    summ = 0
    print(f"vvedite eps")
    eps = float(input())
    if eps <= 0:
        print("hui sosi")
        return
    while summ <= 1 - eps:
        summ += 1 / (N * (N + 1))
        N += 1
        print(summ)
    else:
        print("работа программы завершена")


if __name__ == "__main__":
    main()
