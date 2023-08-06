from vtk import vtkPolyData, vtkPoints, vtkCellArray, vtkDoubleArray
import h5py as h5


class Reader:
    
    def __init__(self):
        pass
    
    def readImageInfo(self, h5File):
        if "DataSetInfo/Image" in h5File:
            imageInfo = h5File["DataSetInfo/Image"]
            
            unitMult = 1.0
            if imageInfo.attrs["Unit"].tostring().decode('UTF8') == "mm":
                unitMult = 1000.0
            
            xPix = int(imageInfo.attrs["X"].tostring().decode('UTF8'))
            yPix = int(imageInfo.attrs["Y"].tostring().decode('UTF8'))
            zPix = int(imageInfo.attrs["Z"].tostring().decode('UTF8'))
            
            xMin = float(imageInfo.attrs["ExtMin0"].tostring().decode('UTF8')) * unitMult
            yMin = float(imageInfo.attrs["ExtMin1"].tostring().decode('UTF8')) * unitMult
            zMin = float(imageInfo.attrs["ExtMin2"].tostring().decode('UTF8')) * unitMult

            xMax = float(imageInfo.attrs["ExtMax0"].tostring().decode('UTF8')) * unitMult
            yMax = float(imageInfo.attrs["ExtMax1"].tostring().decode('UTF8')) * unitMult
            zMax = float(imageInfo.attrs["ExtMax2"].tostring().decode('UTF8')) * unitMult

            xSize = float(imageInfo.attrs["X"].tostring().decode('UTF8'))
            ySize = float(imageInfo.attrs["Y"].tostring().decode('UTF8'))
            zSize = float(imageInfo.attrs["Z"].tostring().decode('UTF8'))

            xScale = (xMax-xMin)/xSize
            yScale = (yMax-yMin)/ySize
            zScale = (zMax-zMin)/zSize            
            
            return (
                (xMin, xMax, xScale, xPix), 
                (-yMax, -yMin, yScale, yPix), 
                (-zMax, -zMin, zScale, zPix),
            )
            
        else:
            return None
    
    def readImageName(self, h5File):
        print(h5File.filename)
        strgrp = "DataSetInfo/Image"
        if strgrp in h5File:
            for att in h5File[strgrp].attrs:
                if att.lower == "filename":
                    #print("has filename")
                    return h5File[strgrp].attrs[att].tostring().decode('UTF8')
        return h5File.filename
            
    def readPointsName(self, h5File, keyNumber):
        strgrp = "Scene/Content/Points" + str(keyNumber)
        if strgrp in h5File:
            return h5File[strgrp].attrs["Name"].tostring().decode('UTF8')
        else:
            return None
    
    def readPointsData(self, h5File, keyNumber):
        strgrp = "Scene/Content/Points" + str(keyNumber)
        if strgrp in h5File:
            markerInfo = h5File[strgrp]
            ptMult = 1.0
            if markerInfo.attrs["Unit"].tostring().decode('UTF8') == "mm":
                ptMult = 1000.0
            markerCoords = h5File[strgrp + "/CoordsXYZR"]
            markerData = list()
            for x in range(len(markerCoords)):
                markerData.append((
                    markerCoords[x][0] * ptMult,
                    markerCoords[x][1] * ptMult, 
                    markerCoords[x][2] * ptMult, 
                    markerCoords[x][3] * ptMult
                ))
            return markerData
        else:
            return None
    
    def readFilamentsName(self, h5File, keyNumber):
        strgrp = "Scene/Content/Filaments" + str(keyNumber)+ "/Graphs"
        if strgrp in h5File:
            return h5File[strgrp].attrs["Name"].tostring().decode('UTF8')
        else:
            return None
    
    def readFilamentsData(self, h5File, keyNumber):
        strgrp = "Scene/Content/Filaments" + str(keyNumber)+ "/Graphs"
        #print("Graphs in file: " + str(strgrp in h5File))
        if strgrp in h5File:
            filamentInfo = h5File[strgrp]
            
            #adjust scaling according to unit (um vs mm)
            ptMult = 1.0
            if filamentInfo.attrs["Unit"].tostring().decode('UTF8') == "mm":
                ptMult = 1000.0
            
            #list of number of vertices and segments for each filament
            #    countData - list:
            #            countData[vertex number] - tuple:
            #                    (number of vertices, number of segments)
            #print("Mult: " + str(ptMult))
            countstr = strgrp + "/TimesNVerticesNEdgesRoots"
            if countstr not in h5File:
                return None
            filamentCounts = h5File[countstr]
            countData = list()
            for x in range(len(filamentCounts)):
                countData.append((
                    filamentCounts[x][1], 
                    filamentCounts[x][2]
                ))
            
            #dict maps filament ID to the vertex IDs which are nodes in that filament
            #print("Counts: " + str(len(countData)))
            filamentNodes = h5File["Scene/Content/Filaments" + str(keyNumber) + "/GraphTracks/GraphVertex"]
            nodeData = dict()
            for x in range(len(filamentNodes)):
                if filamentNodes[x][0] not in nodeData:
                    nodeData[filamentNodes[x][0]] = list()
                if filamentNodes[x][1] != 0:
                    nodeData[filamentNodes[x][0]].append(filamentNodes[x][1])
            
            #dict maps filament ID to vertex IDs in that filament:
            #    vertexData - dict:
            #            vertexData[tree number] - list:
            #                    vertex numbers in tree
            filamentVertices = h5File[strgrp + "/Vertices"]
            vertexData = dict()
            vertexOffset = 0
            for tree in range(len(countData)):
                for vertex in range(vertexOffset, countData[tree][0] + vertexOffset):
                    if tree not in vertexData:
                        vertexData[tree] = list()
                    vertexData[tree].append((
                        filamentVertices[vertex][0] * ptMult, 
                        filamentVertices[vertex][1] * ptMult, 
                        filamentVertices[vertex][2] * ptMult, 
                        filamentVertices[vertex][3] * ptMult
                    ))
                vertexOffset = vertex + 1

            #dict maps each tree to a list of lists, where each list is a branch containing vertex IDs for that branch:
            #    segmentData - dict:
            #            segmentData[tree number] - list:
            #                    segmentData[tree number][branch number] - list:
            #                            vertex numbers in branch
            filamentSegments = h5File[strgrp + "/Segments"]
            segmentData = dict()
            segmentOffset = 0
            for tree in range(len(countData)):
                #don't make a list if this tree has no segments
                if countData[tree][1] == 0:
                    segmentData[tree] = None
                else:
                    #check each segment that belongs to this tree
                    branch = 0
                    segment = segmentOffset
                    maxSegment = countData[tree][1] + segmentOffset
                    while segment < maxSegment:
                        ltV = filamentSegments[segment][0]
                        rtV = filamentSegments[segment][1]
                        #if tree doesn't exist, make a new tree
                        if tree not in segmentData:
                            segmentData[tree] = list()
                        #if tree is empty, make a new branch
                        if len(segmentData[tree]) ==0:
                            segmentData[tree].append(list())
                        #if branch is empty, add first two vertices
                        if len(segmentData[tree][branch]) == 0:
                            segmentData[tree][branch].append(ltV)
                            segmentData[tree][branch].append(rtV)
                        #else, add next vertex if this segment connects to the previous vertex
                        elif segmentData[tree][branch][-1] == ltV:
                                segmentData[tree][branch].append(rtV)
                        #if last vertex in this branch is a node and this isn't the last segment in the tree, make new branch
                        if segmentData[tree][branch][-1] in nodeData[tree] and segment < maxSegment - 1:
                            segmentData[tree].append(list())
                            branch += 1
                        segment += 1
                    segmentOffset = segment
            
            #dict mapping each tree to its nodes, which are mapped to their branches:
            #    branchData - dict: 
            #            branchData[tree number] - dict:
            #                    branchData[tree number][vertex number of node] - list:
            #                            vertex numbers in branch
            branchData = dict()
            for tree in range(len(countData)):
                #if tree has no segments, don't make it
                if segmentData[tree] is None:
                    branchData[tree] = None
                else:
                    #if tree doesn't exist, make it
                    if tree not in branchData:
                        branchData[tree] = dict()
                    for branch in range(len(segmentData[tree])):
                        #if node not mapped yet, make list of branches
                        branchNode = segmentData[tree][branch][0]
                        if branchNode not in branchData[tree]:
                            branchData[tree][branchNode] = list()
                        branchData[tree][branchNode].append(segmentData[tree][branch])
            
            def recMakeBranches(structure, parentBranch, node = 0):
                data = list()
                data.extend(structure[node][parentBranch][1:])
                checkNode = structure[node][parentBranch][-1]
                if (checkNode in structure.keys()):
                    for childBranch in range(len(structure[checkNode])):
                        data.append(recMakeBranches(structure, childBranch, checkNode))
                return data
            
            #recursive function for swapping vertex indices with data
            def recSwapVertexData(number, tree):
                branch = 0
                while branch < len(tree):
                    if type(tree[branch]) is not list:
                        tree[branch] = vertexData[number][tree[branch]]
                        branch += 1
                    else:
                        if len(tree[branch]) > 0:
                            recSwapVertexData(number, tree[branch])
                            branch += 1
                        else:
                            del tree[branch]
            
            #swap vertex indices with data for a linear branch
            def linSwapVertexData(number, tree):
                for point in range(len(tree)):
                    tree[point] = vertexData[number][tree[point]]
            
            #make tree structures
            trees = list()
            for tree in range(len(countData)):
                treeData = list()
                #only build structure past one point if the tree has at least one segment
                if branchData[tree] is not None:
                    #if root is a node, duplicate root and build from the root
                    if len(branchData[tree][0]) > 1:
                        treeData.append(0)
                        treeData.append(0)
                        #recursive building of branches
                        for branch in range(len(branchData[tree][0])):
                            rawBranches = recMakeBranches(branchData[tree], branch)
                            treeData.append(rawBranches)
                    #otherwise, copy until the end of the first branch is reached, then build the rest
                    else:
                        rawBranch = branchData[tree][0][0]
                        treeData.extend(rawBranch)
                        #check if the end of the first branch is a node, then build from it if it is
                        potentialNode = branchData[tree][0][0][-1]
                        if potentialNode in branchData[tree]:
                            for branch in range(len(branchData[tree][potentialNode])):
                                rawBranches = recMakeBranches(branchData[tree], branch, node = potentialNode)
                                treeData.append(rawBranches)
                trees.append(treeData)
            
            #recursive function to remove nodes with single branches
            def recPruneNodes(tree):
                nLists = 0
                for ind in range(len(tree)-1, -1, -1):
                    if type(tree[ind]) is list:
                        nLists += 1
                    else:
                        break
                if nLists == 1:
                    tree.extend(tree.pop())
                    recPruneNodes(tree)
                elif nLists > 1:
                    for ind in range(len(tree)-1, -1, -1):
                        if type(tree[ind]) is list:
                            recPruneNodes(tree[ind])
                        else:
                            break
            
            #swap vertex numbers for vertex data and remove single branch nodes
            for tree in range(len(trees)):
                recSwapVertexData(tree, trees[tree])
                recPruneNodes(trees[tree])
            
            return trees
            
        else:
            return None
    
    def readSurfacesName(self, h5File, keyNumber):
        strgrp = "Scene/Content/Surfaces" + str(keyNumber)
        if strgrp in h5File:
            return h5File[strgrp].attrs["Name"].tostring().decode('UTF8')
        else:
            return None
    
    def readSurfacesData(self, h5File, keyNumber):
        strgrp = "Scene/Content/Surfaces" + str(keyNumber)
        #print("  " + strgrp)
        if strgrp in h5File:
            surfaceInfo = h5File[strgrp]
            
            #adjust scaling according to unit (um vs mm)
            ptMult = 1.0
            if surfaceInfo.attrs["Unit"].tostring().decode('UTF8') == "mm":
                ptMult = 1000.0
                
            #list of number of vertices and triangles for each surface
            #    countData - list:
            #        countData[vertex number] - tuple:
            #            (number of vertices, number of triangles)
            countstr = strgrp + "/TimeNVerticesNTriangles"
            if countstr not in h5File:
                return None
            surfaceCounts = h5File[countstr]
            countData = list()
            for x in range(len(surfaceCounts)):
                countData.append((
                    surfaceCounts[x][1], 
                    surfaceCounts[x][2]
                ))
            
            #dict maps surface ID to vertex IDs in that surface:
            #    vertexData - dict:
            #        vertexData[surface number] - list:
            #            vertexData[surface number][vertex number] - list:
            #                [X, Y, Z]
            surfaceVertices = h5File[strgrp + "/Vertices"]
            vertexData = dict()
            vertexOffset = 0
            for surf in range(len(countData)):
                for vertex in range(vertexOffset, countData[surf][0] + vertexOffset):
                    if surf not in vertexData:
                        vertexData[surf] = list()
                    vertexData[surf].append([
                        surfaceVertices[vertex][0] * ptMult, 
                        surfaceVertices[vertex][1] * ptMult, 
                        surfaceVertices[vertex][2] * ptMult,
                        surfaceVertices[vertex][3],
                        surfaceVertices[vertex][4],
                        surfaceVertices[vertex][5]
                    ])
                vertexOffset = vertex + 1
            
            #dict maps surface ID to list of triangles with vertex IDs in that triangle:
            #    triangleData - dict:
            #        triangleData[surface number] - list:
            #            triangleData[surface number][triangle number] - list:
            #                (A, B, C)
            surfaceTriangles = h5File[strgrp + "/Triangles"]
            triangleData = dict()
            triangleOffset = 0
            for surf in range(len(countData)):
                for triangle in range(triangleOffset, countData[surf][1] + triangleOffset):
                    if surf not in triangleData:
                        triangleData[surf] = list()
                    triangleData[surf].append([
                        surfaceTriangles[triangle][0],
                        surfaceTriangles[triangle][1],
                        surfaceTriangles[triangle][2]
                    ])
                triangleOffset = triangle + 1
                
            #dict maps each surface ID to a vtkPoints object
            #dict maps each surface ID to a vtkCellArray
            vPts = dict()
            vNrms = dict()
            vTrs = dict()
            for surf in range(len(countData)):
                if surf not in vPts:
                    vPts[surf] = vtkPoints()
                if surf not in vNrms:
                    vNrms[surf] = vtkDoubleArray()
                    vNrms[surf].SetNumberOfComponents(3)
                if surf not in vTrs:
                    vTrs[surf] = vtkCellArray()
                for vertex in range(len(vertexData[surf])):
                    vPts[surf].InsertNextPoint(vertexData[surf][vertex][:3])
                    vNrms[surf].InsertNextTuple3(vertexData[surf][vertex][3],vertexData[surf][vertex][4],vertexData[surf][vertex][5])
                for triangle in range(len(triangleData[surf])):
                    vTrs[surf].InsertNextCell(3, triangleData[surf][triangle])
            vPD = dict()
            for surf in range(len(countData)):
                if surf not in vPD:
                    vPD[surf] = vtkPolyData()
                    vPD[surf].SetPoints(vPts[surf])
                    vPD[surf].GetPointData().SetNormals(vNrms[surf])
                    vPD[surf].SetPolys(vTrs[surf])
            
            return vPD
        else:
            return None

    def readMgsfName(self, h5File, keyNumber):
        strgrp = "Scene8/Content/MegaSurfaces" + str(keyNumber)
        if strgrp in h5File:
            return h5File[strgrp].attrs["Name"].tostring().decode('UTF8')
        else:
            return None
    
    def readMgsfData(self, h5File, keyNumber):
        strgrp = "Scene8/Content/MegaSurfaces" + str(keyNumber)
        if strgrp in h5File:
            
            mgsfInfo = h5File[strgrp]
            
            ptMult = 1.0
            if mgsfInfo.attrs["Unit"].tostring().decode('UTF8') == "mm":
                ptMult = 1000.0
            
            mgsfPoints = mgsfInfo["SurfaceModelInfo"]
            pointsList = list()
            for ind in range(len(mgsfPoints)):
                pointsList.append((
                    mgsfPoints[ind][8] * ptMult,
                    mgsfPoints[ind][9] * ptMult,
                    mgsfPoints[ind][10] * ptMult
                ))
            
            return pointsList
        
        else:
            return None
