#!/usr/bin/python2.7

from os import listdir
from os.path import isfile, join, basename
import subprocess

LOCAL_ORIGINAL_PAPER_PATH="/Users/xueting/Documents/kindle/original"
K2PDFOPT = "/Users/xueting/Desktop/k2pdfopt"
LOCAL_KINDLE_PAPER_PATH="/Users/xueting/Documents/kindle/generated/"
files = [join(LOCAL_ORIGINAL_PAPER_PATH,f) for f in listdir(LOCAL_ORIGINAL_PAPER_PATH) if (isfile(join(LOCAL_ORIGINAL_PAPER_PATH,f)) and "pdf" in f)]

for f in files:
    subprocess.call("echo | {} {} -dev 3 -o {}".format(K2PDFOPT, f, join(LOCAL_KINDLE_PAPER_PATH, basename(f))), shell=True)
