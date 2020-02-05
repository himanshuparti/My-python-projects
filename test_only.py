import vtk

#print(vtk.VTK_MINOR_VERSION)

def main():
    filename = "catpyramid1a.stl"
    colors = vtk.vtkNamedColors()

    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)

    '''One render window, multiple viewports'''
    iren_list = []
    rw = vtk.vtkRenderWindow()
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(rw)
    # Define viewport ranges
    xmins = [0, .5, 0, .5]
    xmaxs = [0.5, 1, 0.5, 1]
    ymins = [0, 0, .5, .5]
    ymaxs = [0.5, 0.5, 1, 1]

    ren_bkg = ['AliceBlue', 'GhostWhite', 'WhiteSmoke', 'Seashell']

    for i in range(4):
        if( i == 2 ):
            ren = vtk.vtkRenderer()
            rw.AddRenderer(ren)
            ren.SetViewport(xmins[i], ymins[i], xmaxs[i], ymaxs[i])

            # Create a mapper and actor
            mapper = vtk.vtkPolyDataMapper()
            if vtk.VTK_MAJOR_VERSION <= 5:
                mapper.SetInput(reader.GetOutput())
            else:
                mapper.SetInputConnection(reader.GetOutputPort())

            actor = vtk.vtkActor()
            actor.GetProperty().SetRepresentationToWireframe()
            actor.SetMapper(mapper)

            ren.AddActor(actor)
            ren.SetBackground(colors.GetColor3d(ren_bkg[i]))

            ren.ResetCamera()
        elif( i == 3 ):
            ren = vtk.vtkRenderer()
            rw.AddRenderer(ren)
            ren.SetViewport(xmins[i], ymins[i], xmaxs[i], ymaxs[i])

            # Create a mapper and actor
            mapper = vtk.vtkPolyDataMapper()
            if vtk.VTK_MAJOR_VERSION <= 5:
                mapper.SetInput(reader.GetOutput())
            else:
                mapper.SetInputConnection(reader.GetOutputPort())

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetInterpolationToFlat()
            """
            actor.GetProperty().SetAmbient(1)
            actor.GetProperty().SetDiffuse(0)
            actor.GetProperty().SetSpecular(0)
            actor.GetProperty().SetColor(1,0,0)
            """
            ren.AddActor(actor)
            ren.SetBackground(colors.GetColor3d(ren_bkg[i]))

            ren.ResetCamera()
        elif(i == 0):
            ren = vtk.vtkRenderer()
            rw.AddRenderer(ren)
            ren.SetViewport(xmins[i], ymins[i], xmaxs[i], ymaxs[i])

            # Create a mapper and actor
            mapper = vtk.vtkPolyDataMapper()
            if vtk.VTK_MAJOR_VERSION <= 5:
                mapper.SetInput(reader.GetOutput())
            else:
                mapper.SetInputConnection(reader.GetOutputPort())

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetInterpolationToGouraud()

            ren.AddActor(actor)
            ren.SetBackground(colors.GetColor3d(ren_bkg[i]))

            ren.ResetCamera()
        else:
            ren = vtk.vtkRenderer()
            rw.AddRenderer(ren)
            ren.SetViewport(xmins[i], ymins[i], xmaxs[i], ymaxs[i])

            # Create a mapper and actor
            mapper = vtk.vtkPolyDataMapper()
            if vtk.VTK_MAJOR_VERSION <= 5:
                mapper.SetInput(reader.GetOutput())
            else:
                mapper.SetInputConnection(reader.GetOutputPort())

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.GetProperty().SetInterpolationToPhong()

            ren.AddActor(actor)
            ren.SetBackground(colors.GetColor3d(ren_bkg[i]))

            ren.ResetCamera()
    rw.Render()
    rw.SetWindowName('RW: Multiple ViewPorts')
    iren.Start()

    # FOR OUTPUTTING IMAGE
    writer = vtk.vtkJPEGWriter()
    fileName = "imageoutput.jpeg"

    windowto_image_filter = vtk.vtkWindowToImageFilter()
    windowto_image_filter.SetInput(rw)
    windowto_image_filter.SetScale(1)  # image quality
    windowto_image_filter.SetInputBufferTypeToRGBA()

    writer.SetFileName(fileName)
    writer.SetInputConnection(windowto_image_filter.GetOutputPort())
    writer.Write()

if __name__ == '__main__':
    main()