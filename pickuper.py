import os
import shutil

b = []
path = 'E:\\70 图片文档\\web\\world_cosplay.id'
filelist = os.listdir(path)
x = 20
for i in range(0, len(filelist), x):
    b.append(filelist[i:i + x])
z = 1
for m in b:
    for n in m:
        tempPath = '%s\\%s' % (path, n)
        tempp = '%s第%s弹' % (path, z)
        if os.path.isdir(tempp) is False:
            os.mkdir(tempp)
        distPath = '%s第%s弹\\%s' % (path, z, n)
        shutil.copy(tempPath, distPath)
    z += 1
print('好的完事了')
