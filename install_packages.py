import os
# run file for install package


def install() -> None:
    """
    for install package
    :return:
    None
    """
    os.system("pip install -r requrments.txt")


if __name__ == "__main__":
    install()