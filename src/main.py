from textnode import TextNode
from htmlnode import HTMLNode
from inline import *
import os
import shutil


def copy_static():

    print("starting copy static")

    static_dir = os.path.join(os.getcwd(), "static")
    public_dir = os.path.join(os.getcwd(), "public")
   
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    def copy_rec(src, dst):
        if os.path.isfile(src):
            shutil.copy(src,dst)
            print(f"Copied file: {src} to {dst}")
        elif os.path.isdir(src):
            dst_dir = os.path.join(dst, os.path.basename(src))
            os.mkdir(dst_dir)
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst_dir, item)
                copy_rec(s, d)

    copy_rec(static_dir, public_dir)


    
        

def main():
    copy_static()

if __name__ == "__main__":
    main()