import enum, os
from time_manager import TimeManager, Timer

cateDict = dict()

class LogseqReader:

    class ReadStatus(enum.Enum):
        NeedTimeRecord = 1,
        SkipThisDepth = 2,
        Blank = 3
    
    class Task:
        def __init__(self, taskName, taskTime: Timer=Timer()):
            self.taskName = taskName
            self.taskTime = taskTime
    
    def __init__(self):
        LOGSEQ = '/Users/jean/box/notebook/logseq'
        self.JOURNALS_PATH = os.path.join(LOGSEQ, 'journals/%Y_%m_%d.md')
        self.WORK_TASK_PATH = os.path.join(LOGSEQ, 'pages/工作任务-%Y.md')
        self.MY_TASK_PATH = os.path.join(LOGSEQ, 'pages/%Y任务.md')
        self.CATEGORY_PATH = os.path.join(LOGSEQ, 'pages/行为分类.md')

    def parseCateDict(self):
        pass

    def getTaskListFromMarkdown(self, path: str, defaultCategory: str=None):
        lastdepth = 0
        cateStack = [defaultCategory]
        skipThisDepth = False
        self.status = self.ReadStatus.Blank
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if self.status == self.ReadStatus.NeedTimeRecord:
                    items = line.strip().split('=>')
                    if len(items) == 2:
                        costTime = TimeManager.getTimerFromTime(items[1].strip())
                        if costTime is not None:
                            self.status = self.ReadStatus.SkipThisDepth
                            ;
                depth = 0
                for c in line:
                    if c == '\t':
                        depth += 1
                    else:
                        break
                line = line.strip()
                if depth > lastdepth:
                    if skipThisDepth:
                        continue
                    lastdepth = depth
                elif depth == lastdepth:
                    if line == ':LOGBOOK:':
                        self.status = self.ReadStatus.NeedTimeRecord
                
                
        return []

    def getTaskList(self, date):
        dateTime = TimeManager.getTimeFromDate(date)
        journal_path = TimeManager.fillStrWithTime(self.JOURNALS_PATH)
        self.getTaskListFromMarkdown(journal_path)
        work_task_path = TimeManager.fillStrWithTime(self.WORK_TASK_PATH)
        self.getTaskListFromMarkdown(work_task_path, '工作')
        my_task_path = TimeManager.fillStrWithTime(self.MY_TASK_PATH)
        self.getTaskListFromMarkdown(my_task_path, '提升')
    

class SOURCE(enum.Enum):
    LOGSEQ = LogseqReader
