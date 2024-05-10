import os

def main():
    env = os.getenv('MY_ENV', 'prod')  # Default to 'prod' if not set
    print(f"Running in {env} environment")
print(__name__)
if __name__ == "__main__":
    main()



#set MY_ENV=dev
#echo %MY_ENV%
#python main.py
