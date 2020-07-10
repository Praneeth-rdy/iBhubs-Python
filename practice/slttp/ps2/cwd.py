import os

if __name__ == '__main__':
    n = int(input())
    current_path = "/"
    for i in range(n):
        cmd = input().strip()
        path = cmd.split()[-1]
        if not path.startswith("/"):
            path = os.path.join(current_path, path)
        current_path = os.path.abspath(path)
        print(current_path)
