import os


videoPath = os.path.normpath(r'D:\Enjoy_Source\Movies\宁\风犬少年flv')
vinlist = os.listdir(videoPath)
vinlist.remove('run.bat')
voutlist = [x.replace('.flv','.mp4') for x in vinlist]
ffmpegCmd = 'ffmpeg -i "{}" "{}"'
print(vinlist)
print(voutlist)
f = open('run.bat',"w",encoding='utf-8')
for i in range(len(vinlist)):
    f.write(ffmpegCmd.format(vinlist[i],voutlist[i])+'\n')
f.write("pause\n")
f.close()
