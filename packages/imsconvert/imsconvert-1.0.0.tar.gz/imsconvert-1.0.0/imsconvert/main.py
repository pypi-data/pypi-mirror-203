from os.path import isdir
from os import mkdir
import sys
import glob
import h5py as h5
from . reader import Reader
from . writer import Writer
from . cliops import Cliops

def main():
    projectPath = "C:\\ProgramData\\MBF Bioscience\\ImarisConvert"

    dbg = {
        "Image": True,
        "Marker": True,
        "Filament": True,
        "Surface": True,
        "MegaSurface": True
    }

    colors = {
        "Markers": [
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0)
        ],
        
        "Contours": [
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255)
        ],
        
        "Trees": [
            (255, 255, 0),
            (0, 255, 0),
            (255, 0, 0),
            (255, 0, 255),
            (0, 255, 255),
            (96, 128, 255),
            (223, 223, 96),
            (255, 128, 0),
            (128, 255, 0),
            (255, 96, 128),
            (255, 160, 96),
            (64, 160, 255),
            (255, 196, 32),
            (160, 96, 255)
        ],
        
        "MegaSurfaces": [
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 255, 0),
            (255, 255, 255),
            (0, 128, 128),
            (192, 220, 192),
            (166, 202, 240),
            (255, 251, 240),
            (128, 0, 0),
            (128, 128, 0),
            (0, 0, 128),
            (0, 128, 0),
            (128, 0, 128),
            (128, 128, 128),
            (0, 255, 255),
            (255, 255, 0)
        ]
    }

    clo = Cliops()
    clo.parseArgs(sys.argv)

    logStr = ""
    if clo.doLog:
        logStr += "Filename\tImage Data\tPoints\tFilaments\tSurfaces\n"

    if isdir(projectPath + "\\IMS"):
        
        colorID = {
            "Markers": 0,
            "Contours": 0,
            "Trees": 0,
            "MegaSurfaces": 0
        }
        
        def incColorID(name):
            if name in colorID.keys():
                if colorID[name] == len(colors[name]) - 1:
                    colorID[name] = 0
                else:
                    colorID[name] += 1
        
        def clamp(num):
            return max(0, min(num, 255))
        
        def rgbToHex(rgb):
            return "#{0:02x}{1:02x}{2:02x}".format(clamp(rgb[0]), clamp(rgb[1]), clamp(rgb[2]))
        
        for filename in glob.glob(projectPath + "\\IMS\\*.ims"):
            print('Now reading "' + filename[filename.rfind("\\")+1:] + '"...')
            file = h5.File(filename, "r")
            rdr = Reader()
            wrt = Writer()
            
            #read image info
            scaling = None
            imageStr = ""
            #DEBUG
            if dbg["Image"]:
                scaling = rdr.readImageInfo(file)
                if scaling is None:
                    print("  WARNING: NO IMAGE DATA FOUND")
                    scaling = (
                        (1,1,1,1),
                        (1,1,1,1),
                        (1,1,1,1)
                    )
                else:
                    imageStr += wrt.xmlImageBlock([filename[filename.rfind("\\")+1:-3] + "jpx"], scaling, scaling[2][3])
            
            #read marker info
            pointsStr = ""
            pointsNum = 0
            markerSets = False
            if "Points50" in file["Scene/Content"]:
                markerSets = True
            #DEBUG
            if dbg["Marker"]:
                points = rdr.readPointsData(file, pointsNum)
                while(True):
                    if points is None:
                        break
                    else:
                        if markerSets:
                            pointsStr += wrt.xmlMarkerBlock(pointsNum + 1, points, setName = "PTS: " + rdr.readPointsName(file, pointsNum), color = rgbToHex(colors["Markers"][colorID["Markers"]]))
                        else:
                            pointsStr += wrt.xmlMarkerBlock(pointsNum + 1, points, color = rgbToHex(colors["Markers"][colorID["Markers"]]))
                        incColorID("Markers")
                        pointsNum += 1
                        points = rdr.readPointsData(file, pointsNum)
                if points is None and pointsNum == 0:
                    print("  WARNING: NO POINT DATA FOUND")
            
            #read filament info
            #vessel option
            filamentstr = ""
            filamentNum = 0
            #DEBUG
            if dbg["Filament"]:
                if clo.doVessels:
                    print("  WARNING: VESSELS NOT IMPLEMENTED")
                #tree option
                else:
                    filaments = rdr.readFilamentsData(file, filamentNum)
                    while (True):
                        if filaments is None:
                            break
                        else:
                            for filament in range(len(filaments)):
                                filamentstr += wrt.xmlTreeBlock(filaments[filament], "FIL: " + rdr.readFilamentsName(file, filamentNum), rgbToHex(colors["Trees"][colorID["Trees"]]))
                            print("\n")
                            incColorID("Trees")
                            filamentNum += 1
                            filaments = rdr.readFilamentsData(file, filamentNum)
                    if filaments is None and filamentNum == 0:
                        print("  WARNING: NO FILAMENT DATA FOUND")
                    else:
                        print("  WARNING: FILAMENT " + str(filamentNum) + " DATA MAY BE EMPTY")
            
            #read surface info
            surfStr = ""
            surfNum = 0
            #DEBUG
            if dbg["Surface"]:
                #spine option
                if clo.doSpines:
                    print("  WARNING: SPINES NOT IMPLEMENTED")
                #contour option
                else:
                    surfaces = rdr.readSurfacesData(file, surfNum)
                    while (True):
                        if surfaces is None:
                            break
                        else:
                            surfStr += wrt.xmlSurfaceToContour(surfaces, "SRF: " + rdr.readSurfacesName(file, surfNum), scaling, rgbToHex(colors["Contours"][colorID["Contours"]]))
                            surfNum += 1
                            incColorID("Contours")
                            surfaces = rdr.readSurfacesData(file, surfNum)
                    if surfaces is None and surfNum == 0:
                        print("  WARNING: NO SURFACE DATA FOUND")
            
            mgsfStr = ""
            mgsfNum = 0
            #DEBUG
            if dbg["MegaSurface"]:
                mgsfs = rdr.readMgsfData(file, mgsfNum)
                while (True):
                    if mgsfs is None:
                        break
                    else:
                        mgsfStr += wrt.xmlMarkerBlock(mgsfNum + 1, mgsfs, setName = "MGS: " + rdr.readMgsfName(file, mgsfNum), color = rgbToHex(colors["MegaSurfaces"][colorID["MegaSurfaces"]]))
                        mgsfNum += 1
                        incColorID("MegaSurfaces")
                        mgsfs = rdr.readMgsfData(file, mgsfNum)
                if mgsfs is None and mgsfNum == 0:
                    print("  WARNING: NO MEGASURFACE DATA FOUND")

            #write file
            filestr = wrt.xmlHeaderStr() + wrt.xmlFilefactsBlock(0) + imageStr + pointsStr + filamentstr + surfStr + mgsfStr + wrt.xmlFooterStr()
            wrt.writeFile(filename[:filename.rfind(".") + 1].replace("IMS","XML",1) + "xml", filestr)
            
            if clo.doLog:
                logStr += filename[filename.rfind("\\")+1 : filename.rfind(".")]
                logStr += "\t"
                if len(imageStr) > 0:
                    logStr += "Yes"
                else:
                    logStr += "No"
                logStr += "\t"
                logStr += str(pointsNum) + "\t" + str(filamentNum) + "\t" + str(surfNum) + "\n"
            
            file.close()
            print()
            
    else:
        print("No IMS folder - fill C:\\ProgramData\\MBF Bioscience\\ImarisConvert\\IMS .ims files to convert, and retrieve .xml files at C:\\ProgramData\\MBF Bioscience\\ImarisConvert\\XML")
        mkdir(projectPath + "\\IMS")
        mkdir(projectPath + "\\XML")
        if clo.doLog:
            logStr = "No IMS folder - fill C:\\ProgramData\\MBF Bioscience\\ImarisConvert\\IMS .ims files to convert, and retrieve .xml files at C:\\ProgramData\\MBF Bioscience\\ImarisConvert\\XML\n"

    if clo.doLog:
        wrt = Writer()
        print("Writing log file..")
        wrt.writeFile(projectPath + "\\log.txt", logStr)
    input("Press enter to close...")