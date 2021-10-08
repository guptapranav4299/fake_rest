import threading,time,pdb

class Downloader_Class(threading.Thread):

    def run(self):
        print("Current Task Downloading")
        for i in range(1,6):
            self.i = i
            time.sleep(2)

        return "Hello World"


class Working_Class(threading.Thread):

    def run(self):
        for i in range(1,6):
            print("Working class running: %i (%i)"%(i,dow.i))
            time.sleep(1)
            dow.join()

            print("Task Completed")


if __name__=="__main__":
    dow = Downloader_Class()
    dow.start()

    time.sleep(1)

    wor = Working_Class()
    wor.start()

    t3 = Working_Class()
    t3.start()