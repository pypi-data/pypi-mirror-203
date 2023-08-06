from numpy import sqrt
from vtk import vtkPlane, vtkCutter, vtkMath, vtkPolyDataWriter, vtkCubeSource, vtkContourTriangulator, vtkStripper, vtkCleanPolyData


debug = {
    "Write Image": False,
    "Write Planes": False,
    "Write Cuts": False,
    "Write Poly": False    
}

dbg_path = "C:\\ProgramData\\MBF Bioscience\\ImarisConvert\\Debug"

class Writer:
    #write a single XML string containing headers for MBF XML format
    def xmlHeaderStr(self):
        return str('<?xml version="1.0" encoding="ISO-8859-1"?>\r\n'
                     '<mbf version="4.0" xmlns="http://www.mbfbioscience.com/2007/neurolucida"'
                     ' xmlns:nl="http://www.mbfbioscience.com/2007/neurolucida" appname="Neurolucida"'
                     ' appversion="2019.1.4 (64-bit)">\r\n<description><![CDATA[]]></description>\r\n')
    
    #write a single XML string containing footers for MBF XML format
    def xmlFooterStr(self):
        return str('</mbf>\r\n')
    
    def xmlSetStr(self, setName):
        retstr = '<property name="Set"><s>'
        retstr += setName
        retstr += '</s></property>\r\n'
        return retstr
    
    #write a single XML string containing a point
    def xmlPointStr(self, coords):
        if len(coords) > 1:
            retstr = '<point x="'
            retstr += '{0:.2f}'.format(coords[0])
            retstr += '" y="'
            retstr += '{0:.2f}'.format(-coords[1])
            retstr += '" z="'
            if len(coords) > 2:
                retstr += '{0:.2f}'.format(-coords[2])
            else:
                retstr += '0.00'
            retstr += '" d="'
            if len(coords) > 3:
                retstr += '{0:.2f}'.format(coords[3])
            else:
                retstr += '1.00'
            retstr += '"/>'
            return retstr
        else:
            return ""

    #write a single XML string containing a point
    def xmlTreePointStr(self, coords):
        if len(coords) > 1:
            retstr = '<point x="'
            retstr += '{0:.2f}'.format(coords[0])
            retstr += '" y="'
            retstr += '{0:.2f}'.format(-coords[1])
            retstr += '" z="'
            if len(coords) > 2:
                retstr += '{0:.2f}'.format(-coords[2])
            else:
                retstr += '0.00'
            retstr += '" d="'
            if len(coords) > 3:
                retstr += '{0:.2f}'.format(coords[3])
            else:
                retstr += '1.00'
            retstr += '"/>'
            return retstr
        else:
            return ""

    #write a single XML string containing a marker
    def xmlMarkerStr(self, number, color = "#FFFFFF"):
        markerRef = {
            1: "Dot", 
            2: "OpenCircle", 
            3: "Cross", 
            4: "Plus", 
            5: "OpenUpTriangle", 
            6: "OpenDownTriangle", 
            7: "OpenSquare", 
            8: "Asterisk", 
            9: "OpenDiamond", 
            10: "FilledStar", 
            11: "FilledCircle", 
            12: "FilledUpTriangle", 
            13: "FilledDownTriangle", 
            14: "FilledSquare", 
            15: "FilledDiamond", 
            16: "Flower", 
            17: "OpenStar", 
            18: "DoubleCircle", 
            19: "Circle1", 
            20: "Circle2", 
            21: "Circle3", 
            22: "Circle4", 
            23: "Circle5", 
            24: "Circle6", 
            25: "Circle7", 
            26: "Circle8", 
            27: "Circle9", 
            28: "Flower2", 
            29: "SnowFlake", 
            30: "OpenFinial", 
            31: "FilledFinial", 
            32: "MalteseCross", 
            33: "FilledQuadStar", 
            34: "OpenQuadStar", 
            35: "Flower3", 
            36: "Pinwheel", 
            37: "TexacoStar", 
            38: "ShadedStar", 
            39: "SkiBasket", 
            40: "Clock", 
            41: "ThinArrow", 
            42: "ThickArrow", 
            43: "SquareGunSight", 
            44: "GunSight", 
            45: "TriStar", 
            46: "NinjaStar", 
            47: "KnightsCross", 
            48: "Splat", 
            49: "CircleArrow", 
            50: "CircleCross"
        }
        
        if (number >= 1 and
             number < len(markerRef)):
            retstr = '<marker type="'
            retstr += markerRef[number]
            retstr += '" color="'
            retstr += color
            retstr += '" name="Marker '
            retstr += str(number)
            retstr += '" varicosity="false">'
            return retstr
        else:
            return ""
    
    #write a single XML string containing a contour
    def xmlContourStr(self, name = None, closed = True, color = "#FFFFFF"):
        if name is None:
            name = "Unknown Contour"
        retstr = '<contour name="'
        retstr += str(name)
        retstr += '" color="'
        retstr += color
        retstr += '" closed="'
        if closed:
            retstr += 'true'
        else:
            retstr += 'false'
        retstr += '" shape="Contour">'
        return retstr

    def xmlSectionStr(self, number, spacing = 1, cut = None):
        if cut is None:
            cut = spacing
        if number >= 1:
            retstr = '<section sid="S'
            retstr += str(number)
            retstr += '" name="Section '
            retstr += str(number)
            retstr += '" top="'
            retstr += str((number - 1) * spacing)
            retstr += '" cutthickness="'
            retstr += str(spacing)
            retstr += '" mountedthickness="'
            retstr += str(spacing)
            retstr += '"/>'
            return retstr
        else:
            return "" 
    
    def xmlMarkerBlock(self, number, points, setName = None, color = "#FFFFFF"):
        if (number > 0 and
             type(points) is list and
             len(points) > 0 and
             type(points[0]) is tuple):
            headStr = self.xmlMarkerStr(number, color)
            headStr += '\r\n'
            footStr = '</marker>\r\n'
            retStr = ""
            
            if type(setName) is str:
                for point in range(len(points)):
                    bodyStr = '  '
                    bodyStr += self.xmlSetStr(setName)
                    bodyStr += '  '
                    bodyStr += self.xmlPointStr(points[point])
                    bodyStr += '\r\n'
                    retStr += headStr + bodyStr + footStr
            else:
                retStr += headStr
                for point in range(len(points)):
                    bodyStr = '  '
                    bodyStr += self.xmlPointStr(points[point])
                    bodyStr += '\r\n'
                    retStr += bodyStr
                retStr += footStr
                    
            return retStr
        else:
            return ""
    
    def xmlContourBlock(self, name, points, setName = None, color = "#FFFFFF"):
        if (type(points) is list and
             type(points[0]) is tuple):
            retstr = self.xmlContourStr(name, color = color)
            retstr += '\r\n'
            if type(setName) is str:
                retstr += '  '
                retstr += self.xmlSetStr(setName)
            retstr += str('  <property name="GUID"><s></s></property>\r\n'
                                     '  <property name="FillDensity"><n>0</n></property>\r\n'
                                     '  <resolution>1.000000</resolution>\r\n')
            for point in range(len(points)):
                retstr += '  '
                retstr += self.xmlPointStr(points[point])
                retstr += '\r\n'
            retstr += '</contour>\r\n'
            return retstr
        else:
            return ""
    
    def xmlFilefactsBlock(self, sections = 0, spacing = 1, cut = None):
        if cut is None:
            cut = spacing
        if sections > 0:
            retstr = '<filefacts>\r\n'
            for section in range(1, sections + 1):
                retstr += '  '
                retstr += self.xmlSectionStr(section, spacing, cut)
                retstr += '\r\n'
            retstr += '</filefacts>\r\n'
            return retstr
        else:
            return ""
    
    def xmlImageBlock(self, filenames, scaling, spacing = 0.0):
        #print(filenames)
        if (type(filenames) is list and
             type(filenames[0]) is str and
             type(scaling) is tuple):
            retstr = '<images>\r\n'
            for ind in range(len(filenames)):
                retstr += '  <image>\r\n'
                retstr += '    <filename>'
                retstr += filenames[ind]
                retstr += '</filename>\r\n'
                retstr += '    <scale x="'
                retstr += '{0:.5f}'.format(scaling[0][2])
                retstr += '" y="'
                retstr += '{0:.5f}'.format(scaling[1][2])
                retstr += '"/>\r\n'
                retstr += '    <coord x="0.00000" y="0.00000" z="'
                retstr += '{0:.5f}'.format(ind * spacing)
                retstr += '"/>\r\n'
                retstr += '  </image>\r\n'
            retstr += '</images>\r\n'
            return retstr
        else:
            return ""
    
    def xmlTreeBlock(self, tree, setName, color = "#FFFFFF"):
        if type(tree) is list and len(tree) > 0:
            retstr = '<tree color="' + color + '" type="Dendrite" leaf="Normal">\r\n'
            retstr += '  '
            retstr += self.xmlSetStr(setName)
            
            #recursive function to write branched structure properly
            def recBranchBlock(tree, tablevel = 1):
                treestr = str()
                for branch in range(len(tree)):
                    treestr += ('  ' * tablevel)
                    #if it's a point, write in this branch
                    if type(tree[branch]) is not list:
                        treestr += Writer.xmlTreePointStr(self, tree[branch]) + '\r\n'
                    #recur if new branch
                    else:
                        treestr += '<branch>\r\n'
                        treestr += recBranchBlock(tree[branch], tablevel + 1)
                        treestr += ('  ' * tablevel) + '</branch>\r\n'
                return treestr
            
            retstr += recBranchBlock(tree)
            retstr += '</tree>\r\n'
            return retstr
            
        else:
            return ""
    
    def xmlSurfaceToContour(self, surfaces, setName, scaling, color = "#FFFFFF"):
        if type(surfaces) is dict:
            retstr = ""
            vPDW_writer = vtkPolyDataWriter()
            vCT_tri = vtkContourTriangulator()
            
            #object that bounds the image stack
            vCS_image = vtkCubeSource()
            vCS_image.SetBounds(scaling[0][0], scaling[0][1], -scaling[1][1], -scaling[1][0], -scaling[2][1], -scaling[2][0])
            vCS_image.Update()
            vPD_imageblock = vCS_image.GetOutput()
            
            #DEBUG - check image bounds
            if debug["Write Image"]:
                vPDW_writer.SetInputData(vPD_imageblock)
                vPDW_writer.SetFileName(dbg_path + "\\image.vtk")
                vPDW_writer.Update()
            
            #Z plane cut function
            vP_cutplane = vtkPlane()
            vP_cutplane.SetOrigin(vCS_image.GetCenter())
            vP_cutplane.SetNormal(0, 0, 1)
            
            #parameters for cutting
            nValues = scaling[2][3]
            distMin = -(vPD_imageblock.GetCenter()[2] - vPD_imageblock.GetBounds()[4])
            distMax = vPD_imageblock.GetBounds()[5] - vPD_imageblock.GetCenter()[2]
            
            #cutter object
            vC_cutter = vtkCutter()
            vC_cutter.SetCutFunction(vP_cutplane)
            
            #DEBUG - check image planes
            if debug["Write Planes"]:
                vC_cutter.SetInputData(vPD_imageblock)
                vC_cutter.GenerateValues(nValues, distMin, distMax)
                vC_cutter.Update()
                vCT_tri.SetInputData(vC_cutter.GetOutput())
                vCT_tri.Update()
                vPDW_writer.SetInputData(vCT_tri.GetOutput())
                vPDW_writer.SetFileName(dbg_path + "\\planes.vtk")
                vPDW_writer.Update()

            #loop over all cells in this object and cut them
            contourMap = dict()
            for surf in range(len(surfaces)):
                
                #DEBUG - check poly
                if debug["Write Poly"]:
                    vPDW_writer.SetInputData(surfaces[surf])
                    vPDW_writer.SetFileName(dbg_path + "\\poly.vtk")
                    vPDW_writer.Update()
                
                #put poly through cutter
                vC_cutter.SetInputData(surfaces[surf])
                vC_cutter.GenerateValues(nValues, distMin, distMax)
                vC_cutter.Update()
                
                #DEBUG - check cuts
                if debug["Write Cuts"]:
                    vCT_tri.SetInputData(vC_cutter.GetOutput())
                    vCT_tri.Update()
                    vPDW_writer.SetInputData(vCT_tri.GetOutput())
                    vPDW_writer.SetFileName(dbg_path + "\\cuts.vtk")
                    vPDW_writer.Update()
                
                #get contour data from cutter
                vPD = vC_cutter.GetOutput()
                if vPD is not None:
                    vS = vtkStripper()
                    vS.SetInputConnection(vC_cutter.GetOutputPort())
                    vS.Update()
                    vCPD = vtkCleanPolyData()
                    vCPD.SetInputData(vS.GetOutput())
                    vCPD.Update()
                    vData = vCPD.GetOutput()
                    if vData is not None:
                        numPoints = vData.GetNumberOfPoints()
                        if surf not in contourMap:
                            contourMap[surf] = dict()
                        for pointID in range(numPoints):
                            pointZ = vData.GetPoint(pointID)[2]
                            if pointZ not in contourMap[surf]:
                                contourMap[surf][pointZ] = list()
                            contourMap[surf][pointZ].append(vData.GetPoint(pointID))
                    else:
                        contourMap[surf] = None
            
            #generate string
            for surf in range(len(contourMap)):
                for zpos in contourMap[surf]:
                    retstr += self.xmlContourBlock(setName + " - Cell" + str(surf), contourMap[surf][zpos], setName, color)
            
            return retstr
            
        else:
            return None
    
    def writeFile(self, filename, body):
        with open(filename, mode='w', newline='') as file:
            file.write(body)

    def __exportVtkPolyData(self, vPD, filename):
        vPDW = vtkPolyDataWriter()
        vPDW.SetInputData(vPD)
        vPDW.SetFileName(filename)
        vPDW.Update()
