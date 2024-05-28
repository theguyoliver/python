import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--Physics', help='Physics Score')
    parser.add_argument('--Chemistry', help='Chemistry Score')
    parser.add_argument('--Biology', help='Biology Score')
    args = parser.parse_args()

    print(args.Physics)
    print(args.Chemistry)
    print(args.Biology)

    ps = float(args.Physics)
    cs = float(args.Chemistry)
    bs = float(args.Biology)
    average = None

    if ps is not None and cs is not None and bs is not None:
        average = (ps + cs + bs)/3
    print('Average: %.2f' %average)
