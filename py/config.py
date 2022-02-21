# def main(): # 1
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
 
# def main(): # 2
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("Couldn't find the config.txt file!")
 
def main(): # 3
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
 
if __name__ == '__main__':
    main()