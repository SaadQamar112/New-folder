def shutdown_system():
    command = input("Enter command: ").strip().lower()
    if command == "shutdown":
        print("System is shutting down...")
        return True
    else:
        print("Invalid command.")
        return False

def main():
    while True:
        if shutdown_system():
            break

if __name__ == "__main__":
    main()
