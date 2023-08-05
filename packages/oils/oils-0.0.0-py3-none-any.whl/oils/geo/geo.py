import gmsh
import sys

# Gmsh initialization
class Init:
    def __init__(self,modelName):
        self.modelName   = modelName
        gmsh.initialize(modelName)
        
# CAD entities synchronizations
class Sync:
    def __init__():
        gmsh.model.occ.synchronize()

# Generate mesh
class Generate:
    def __init__(self, dim=2, viz=False):
        self.dim =dim
        self.viz =viz
        gmsh.model.mesh.generate(dim)
        if viz == True:
            gmsh.fltk.run()
        else:
            pass

              
# ---- Geometrical primitives creation -----

# Rectangle primitive
class Rectangle:
    def __init__(self, x, y, z, width, height, tag=None,roundedRadius=None):
        self.tag = tag
        self.roundedRadius = roundedRadius
        gmsh.model.occ.addRectangle(x, y, z, 
                                    width, height, 
                                    tag=self.tag, roundedRadius=None)


            
             