import GPUtil
from tabulate import tabulate


def getGpuInfo():
    gpus = GPUtil.getGPUs()
    gpuList = []

    for gpu in gpus:
        gpuInfo = {
            "id": gpu.id,
            "name": gpu.name,
            "load": f"{gpu.load * 100:.1f}%",
            "freeMemory": f"{gpu.memoryFree}MB",
            "usedMemory": f"{gpu.memoryUsed}MB",
            "totalMemory": f"{gpu.memoryTotal}MB",
            "temperature": f"{gpu.temperature}°C",
            "uuid": gpu.uuid,
        }
        gpuList.append(gpuInfo)

    return gpuList


def printGpuInfo(gpuList):
    headers = [
        "ID",
        "Name",
        "Load",
        "Free Memory",
        "Used Memory",
        "Total Memory",
        "Temperature",
        "UUID",
    ]
    table = [
        [
            gpu["id"],
            gpu["name"],
            gpu["load"],
            gpu["freeMemory"],
            gpu["usedMemory"],
            gpu["totalMemory"],
            gpu["temperature"],
            gpu["uuid"],
        ]
        for gpu in gpuList
    ]
    print(tabulate(table, headers=headers))


if __name__ == "__main__":
    gpuList = getGpuInfo()
    printGpuInfo(gpuList)

# Exception has occurred: ModuleNotFoundError
# No module named 'distutils'
# File "C:\Users\ottob\Documents\python\gpuInfo\gpuInfoUpdated.py", line 1, in <module>
# import GPUtil
# ModuleNotFoundError: No module named 'distutils'
