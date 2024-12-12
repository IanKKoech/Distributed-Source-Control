import sys
from dsc.repository import DistributedSourceControl

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        return

    command = sys.argv[1]
    if command == "init":
        print(DistributedSourceControl.init())
    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: python main.py add <file>")
        else:
            print(DistributedSourceControl.add(sys.argv[2]))
    elif command == "commit":
        if len(sys.argv) < 3:
            print("Usage: python main.py commit <message>")
        else:
            print(DistributedSourceControl.commit(" ".join(sys.argv[2:])))
    elif command == "log":
        print(DistributedSourceControl.log())
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
