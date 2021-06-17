from mosse import mosse
import argparse
import os
parse = argparse.ArgumentParser()
parse.add_argument('--lr', type=float, default=0.125, help='the learning rate')
parse.add_argument('--sigma', type=float, default=100, help='the sigma')
parse.add_argument('--num_pretrain', type=int, default=128, help='the number of pretrain')
parse.add_argument('--rotate', action='store_true', help='if rotate image during pre-training.')
parse.add_argument('--record', action='store_true', help='record the frames')

if __name__ == '__main__':
    img_base = 'datasets/test_public'
    img_dir = os.listdir(img_base)
    for i in img_dir:

        args = parse.parse_args()

        tracker = mosse(args, i)
        tracker.start_tracking()
