import vtk

def main():
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetHeight(3.0)
    cylinder.SetRadius(1.0)
    cylinder.SetResolution(10)
    clmapper=vtk.vtkPolyDataMapper()
    clmapper.SetInputConnection(cylinder.GetOutputPort())
    cyactor=vtk.vtkActor()
    cyactor.SetMapper(clmapper)

    renderer=vtk.vtkRenderer()
    renderer.AddActor(cyactor)
    renderer.SetBackground(0.0,0.0,0.5)
    renWin=vtk.vtkRenderWindow()
    renWin.AddRenderer(renderer)
    renWin.SetSize(450,450)
    iren=vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    style=vtk.vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)
    iren.Initialize()
    iren.Start()
if __name__=='__main__':
    main()
