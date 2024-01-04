from input import SOURCE, LogseqReader


if __name__ == "__main__":
    source = SOURCE.LOGSEQ.value
    reader = source()