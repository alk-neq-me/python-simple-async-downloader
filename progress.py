def progress_bar(progress, width=40):
    left = width * progress // 100
    right = width - left
    
    tags = "=" * left + ">"
    spaces = " " * right
    percents = f"{progress:.0f} %"
    
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)


if __name__ == "__main__":
    print("please run main.py")
